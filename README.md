# AgroSense - AI-Powered Agricultural Assistant

AgroSense is an intelligent agricultural recommendation system built with Python and Flask. It combines crop recommendation, plant disease detection, fertilizer advice, and crop insights to help farmers and agronomists make better decisions.

## Features

- **Crop Recommendation**
  - Predicts the best crop based on soil data and weather conditions
  - Uses a Random Forest model loaded from `models/RandomForest.pkl`
  - Inputs: Nitrogen (N), Phosphorous (P), Potassium (K), temperature, humidity, pH, and rainfall

- **Plant Disease Detection**
  - Detects plant diseases from uploaded leaf images
  - Uses a `ResNet9` model loaded from `models/plant_disease_model.pth`
  - Supports 38 disease classes across multiple crops

- **Fertilizer Recommendation**
  - Suggests fertilizer requirements based on soil N-P-K values and crop choice
  - Computes recommended quantities for Urea, SSP, and MOP
  - Uses fertilizer data from `Data/fertilizer.csv`

- **Crop Insights**
  - Displays crop profiles and growing calendars from `utils/crop_database.py`
  - Provides details on nutrient requirements, moisture, pH, and seasonal guidance

- **Weather Integration**
  - Fetches live temperature and humidity using the OpenWeatherMap API
  - Supports city-based weather lookup and coordinate-based weather lookup

## Technology Stack

- Python
- Flask
- PyTorch
- scikit-learn
- Pandas
- NumPy
- Pillow
- Requests
- HTML, CSS, JavaScript
- Bootstrap
- Font Awesome

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

`requirements.txt` includes:

- numpy
- pandas
- Flask
- scikit-learn
- requests
- Pillow
- gunicorn == 20.0.4

> Note: The repository does not include a pinned CPU-only PyTorch wheel in `requirements.txt`. Install the correct `torch` and `torchvision` packages separately if needed.

## Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/AgroSense.git
cd AgroSense
```

2. Create and activate a Python virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure your OpenWeatherMap API key in `config.py`:

```python
weather_api_key = "your_api_key_here"
```

5. Ensure model files are present in `models/`:

- `plant_disease_model.pth`
- `pytorch_model.pth`
- `RandomForest.pkl`

## Project Structure

```
app.py
config.py
generate_html_word.py
Procfile
README.md
requirements.txt
Runtime.txt
Data/
  fertilizer.csv
models/
  plant_disease_model.pth
  pytorch_model.pth
  RandomForest.pkl
static/
  css/
    bootstrap.css
    font-awesome.min.css
    modern.css
    style.css
  images/
    download.jfif
  scripts/
    cities.js
templates/
  crop-insights-result.html
  crop-insights.html
  crop-result.html
  crop.html
  disease-result.html
  disease.html
  fertilizer-result.html
  fertilizer.html
  index.html
  layout.html
  try_again.html
utils/
  crop_calendar.py
  crop_database.py
  disease.py
  fertilizer.py
  model.py
```

## Usage

Run the application:

```bash
python app.py
```

Open your browser at `http://localhost:5000`.

### Application Pages

- **Home**: entry point for AgroSense
- **Crop Recommendation**: choose crops based on soil and weather inputs
- **Disease Detection**: upload a leaf image and detect plant disease
- **Fertilizer Suggestion**: get fertilizer recommendations for a crop
- **Crop Insights**: view crop profiles and cultivation calendars

## Configuration

`config.py` stores your OpenWeatherMap API key:

```python
weather_api_key = "your_openweathermap_api_key"
```

For production, disable debug mode in `app.py`:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

## Supported Plant Disease Classes

The disease model supports the following classes:

- Apple: `Apple___Apple_scab`, `Apple___Black_rot`, `Apple___Cedar_apple_rust`, `Apple___healthy`
- Blueberry: `Blueberry___healthy`
- Cherry: `Cherry_(including_sour)___Powdery_mildew`, `Cherry_(including_sour)___healthy`
- Corn: `Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot`, `Corn_(maize)___Common_rust_`, `Corn_(maize)___Northern_Leaf_Blight`, `Corn_(maize)___healthy`
- Grape: `Grape___Black_rot`, `Grape___Esca_(Black_Measles)`, `Grape___Leaf_blight_(Isariopsis_Leaf_Spot)`, `Grape___healthy`
- Orange: `Orange___Haunglongbing_(Citrus_greening)`
- Peach: `Peach___Bacterial_spot`, `Peach___healthy`
- Pepper, bell: `Pepper,_bell___Bacterial_spot`, `Pepper,_bell___healthy`
- Potato: `Potato___Early_blight`, `Potato___Late_blight`, `Potato___healthy`
- Raspberry: `Raspberry___healthy`
- Soybean: `Soybean___healthy`
- Squash: `Squash___Powdery_mildew`
- Strawberry: `Strawberry___Leaf_scorch`, `Strawberry___healthy`
- Tomato: `Tomato___Bacterial_spot`, `Tomato___Early_blight`, `Tomato___Late_blight`, `Tomato___Leaf_Mold`, `Tomato___Septoria_leaf_spot`, `Tomato___Spider_mites Two-spotted_spider_mite`, `Tomato___Target_Spot`, `Tomato___Tomato_Yellow_Leaf_Curl_Virus`, `Tomato___Tomato_mosaic_virus`, `Tomato___healthy`
