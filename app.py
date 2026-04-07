# Importing essential libraries and modules

from flask import Flask, render_template, request, jsonify
from markupsafe import Markup
import numpy as np
import pandas as pd
from utils.fertilizer import fertilizer_dic
from utils.crop_calendar import crop_calendar_dict
from utils.crop_database import crop_database
import requests
import config
import pickle
# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------

# Loading crop recommendation model

crop_recommendation_model_path = 'models/RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))


# =========================================================================================

# Custom functions for calculations


def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = config.weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None


# ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)

# render home page


@ app.route('/')
def home():
    title = 'AgroSense - Home'
    return render_template('index.html', title=title)

# render crop recommendation form page


@ app.route('/crop-recommend')
def crop_recommend():
    title = 'AgroSense - Crop Recommendation'
    return render_template('crop.html', title=title)

# render fertilizer recommendation form page


@ app.route('/fertilizer')
def fertilizer_recommendation():
    title = 'AgroSense - Fertilizer Suggestion'

    return render_template('fertilizer.html', title=title)


# render crop insights dictionary page

@app.route('/crop-insights')
def crop_insights():
    title = 'AgroSense - Explore Crops'
    crops_list = sorted(list(crop_database.keys()))
    return render_template('crop-insights.html', crops=crops_list, title=title)

@app.route('/weather-by-coords', methods=['POST'])
def weather_by_coords():
    data = request.get_json()
    lat = data.get('lat')
    lon = data.get('lon')

    api_key = config.weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = f"{base_url}lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] == 200:
        y = x["main"]
        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return jsonify({"temperature": temperature, "humidity": humidity})
    else:
        return jsonify({"error": "Failed to fetch weather data"}), 400

# ===============================================================================================

# RENDER PREDICTION PAGES

# render crop recommendation result page


@ app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'AgroSense - Crop Recommendation'

    if request.method == 'POST':
        temp = float(request.form['temperature'])
        hum = float(request.form['humidity'])
        N = float(request.form['nitrogen'])
        P = float(request.form['phosphorous'])
        K = float(request.form['pottasium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        target_category = request.form.get('category', 'All')
        duration_days_raw = request.form.get('duration', '').strip()

        # Convert days entered by user to a duration category
        if duration_days_raw and duration_days_raw.isdigit():
            duration_days = int(duration_days_raw)
            if duration_days <= 100:
                target_duration = 'Short'
            elif duration_days <= 150:
                target_duration = 'Medium'
            else:
                target_duration = 'Long'
        else:
            target_duration = 'All'

        data = np.array([[N, P, K, temp, hum, ph, rainfall]])
        
        probabilities = crop_recommendation_model.predict_proba(data)[0]
        classes = crop_recommendation_model.classes_
        
        crop_probs = sorted(zip(classes, probabilities), key=lambda x: x[1], reverse=True)
        
        from utils.crop_attributes import crop_attributes
        from utils.vegetable_data import vegetable_data, score_vegetable

        # Build unified pool: ML crops + rule-based vegetables
        all_candidates = []

        # 1. ML model crops
        for crop_name, prob in crop_probs:
            crop_attr = crop_attributes.get(crop_name.lower(), {})
            all_candidates.append({
                'name': crop_name,
                'score': round(prob * 100, 2),
                'attributes': crop_attr,
                'calendar': crop_calendar_dict.get(crop_name.lower(), [])
            })

        # 2. Rule-based vegetables (scored 0-100 based on proximity to ideal conditions)
        for veg_name, veg_info in vegetable_data.items():
            veg_score = score_vegetable(veg_info['ideal'], N, P, K, temp, hum, ph, rainfall)
            all_candidates.append({
                'name': veg_name,
                'score': veg_score,
                'attributes': veg_info['attributes'],
                'calendar': crop_calendar_dict.get(veg_name, [])
            })

        # Sort entire pool by score descending
        all_candidates.sort(key=lambda x: x['score'], reverse=True)

        # Apply category and duration filters
        filtered_crops = []
        for crop in all_candidates:
            crop_attr = crop['attributes']
            cat_match = (target_category == 'All') or (target_category in crop_attr.get('categories', []))
            dur_match = (target_duration == 'All') or (target_duration == crop_attr.get('duration', ''))
            if cat_match and dur_match:
                filtered_crops.append(crop)

        # Take up to top 3 matching crops
        top_crops = filtered_crops[:3]

        fallback = False
        if not top_crops:
            fallback = True
            top_crops = all_candidates[:3]

        return render_template('crop-result.html', top_crops=top_crops, fallback=fallback, title=title)

    else:
        return render_template('try_again.html', title=title)

# render fertilizer recommendation result page


@ app.route('/fertilizer-predict', methods=['POST'])
def fert_recommend():
    title = 'AgroSense - Fertilizer Suggestion'

    crop_name = str(request.form['cropname'])
    N = float(request.form['nitrogen'])
    P = float(request.form['phosphorous'])
    K = float(request.form['pottasium'])
    farm_size = float(request.form.get('farm_size', 1.0))

    df = pd.read_csv('Data/fertilizer.csv')

    nr = df[df['Crop'] == crop_name]['N'].iloc[0]
    pr = df[df['Crop'] == crop_name]['P'].iloc[0]
    kr = df[df['Crop'] == crop_name]['K'].iloc[0]

    n = nr - N
    p = pr - P
    k = kr - K
    
    n_def = max(0, n)
    p_def = max(0, p)
    k_def = max(0, k)
    
    # Calculate Precision Output
    urea_kg = max(0, round((n / 0.46) * farm_size, 1)) if n > 0 else 0
    ssp_kg = max(0, round((p / 0.16) * farm_size, 1)) if p > 0 else 0
    mop_kg = max(0, round((k / 0.60) * farm_size, 1)) if k > 0 else 0

    temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
    max_value = temp[max(temp.keys())]
    if max_value == "N":
        if n < 0:
            key = 'NHigh'
        else:
            key = "Nlow"
    elif max_value == "P":
        if p < 0:
            key = 'PHigh'
        else:
            key = "Plow"
    else:
        if k < 0:
            key = 'KHigh'
        else:
            key = "Klow"

    response = Markup(str(fertilizer_dic[key]))

    return render_template('fertilizer-result.html', 
                            recommendation=response, 
                            crop_name=crop_name,
                            farm_size=farm_size,
                            urea=urea_kg,
                            ssp=ssp_kg,
                            mop=mop_kg,
                            title=title)

# render crop insights result page

@app.route('/crop-insights-result', methods=['POST'])
def crop_insights_result():
    title = 'AgroSense - Explore Crops Profile'
    if request.method == 'POST':
        crop_name = request.form.get('cropname').strip().lower()
        
        db_entry = crop_database.get(crop_name, {})
        if not db_entry:
            crops_list = sorted(list(crop_database.keys()))
            error_msg = f"Sorry, '{crop_name.capitalize()}' is currently not fully documented in our database. Please check your spelling or try another crop!"
            return render_template('crop-insights.html', crops=crops_list, title=title, error=error_msg)
        
        calendar_data = db_entry.get("calendar", [])
        total_time = "Unknown"
        if calendar_data:
            last_dur = calendar_data[-1].get("duration", "")
            if "Days" in last_dur:
                total_time = f"Approx. {last_dur.split('-')[-1].strip()}" if "-" in last_dur else last_dur
            elif "Month" in last_dur:
                val = last_dur.split(" ")[-1] if " " in last_dur else last_dur
                total_time = f"{val} Months"
            else:
                total_time = "1 Full Season"
        
        return render_template('crop-insights-result.html', 
                               crop_name=crop_name, 
                               n=db_entry.get("n", "N/A"), 
                               p=db_entry.get("p", "N/A"), 
                               k=db_entry.get("k", "N/A"), 
                               ph=db_entry.get("ph", "N/A"), 
                               moisture=db_entry.get("moisture", "N/A"),
                               weather=db_entry,
                               calendar_data=calendar_data,
                               total_time=total_time,
                               title=title)
    return redirect(url_for('crop_insights'))



# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)
