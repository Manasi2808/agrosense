# Rule-based vegetable recommendation data
# Each vegetable has ideal NPK, climate ranges and attributes for scoring

vegetable_data = {
    'tomato': {
        'ideal': {
            'N': (60, 80), 'P': (55, 80), 'K': (55, 80),
            'temperature': (20, 27), 'humidity': (60, 75),
            'ph': (6.0, 7.0), 'rainfall': (400, 600)
        },
        'attributes': {'categories': ['Vegetables'], 'duration': 'Short'},
    },
    'potato': {
        'ideal': {
            'N': (80, 120), 'P': (50, 80), 'K': (80, 120),
            'temperature': (15, 20), 'humidity': (60, 80),
            'ph': (5.0, 6.5), 'rainfall': (400, 600)
        },
        'attributes': {'categories': ['Vegetables'], 'duration': 'Short'},
    },
    'onion': {
        'ideal': {
            'N': (60, 80), 'P': (40, 60), 'K': (60, 80),
            'temperature': (13, 24), 'humidity': (60, 70),
            'ph': (6.0, 7.5), 'rainfall': (200, 400)
        },
        'attributes': {'categories': ['Vegetables'], 'duration': 'Short'},
    },
    'spinach': {
        'ideal': {
            'N': (80, 100), 'P': (30, 50), 'K': (40, 60),
            'temperature': (10, 20), 'humidity': (50, 70),
            'ph': (6.0, 7.0), 'rainfall': (200, 400)
        },
        'attributes': {'categories': ['Vegetables'], 'duration': 'Short'},
    },
    'cauliflower': {
        'ideal': {
            'N': (80, 120), 'P': (40, 60), 'K': (60, 80),
            'temperature': (14, 18), 'humidity': (60, 80),
            'ph': (6.0, 7.0), 'rainfall': (400, 500)
        },
        'attributes': {'categories': ['Vegetables'], 'duration': 'Medium'},
    },
    'brinjal': {
        'ideal': {
            'N': (60, 80), 'P': (40, 60), 'K': (60, 80),
            'temperature': (22, 30), 'humidity': (60, 70),
            'ph': (5.5, 6.5), 'rainfall': (500, 700)
        },
        'attributes': {'categories': ['Vegetables'], 'duration': 'Medium'},
    },
}


def score_vegetable(veg_ideal, N, P, K, temp, hum, ph, rainfall):
    """
    Compute a 0-100 fit score based on how close user inputs are to ideal ranges.
    Returns 100 if perfectly within range, decreases linearly outside it.
    """
    def proximity(value, low, high):
        if low <= value <= high:
            return 1.0
        span = (high - low) / 2 + 1
        dist = min(abs(value - low), abs(value - high))
        return max(0.0, 1.0 - dist / (span * 2))

    scores = [
        proximity(N,        *veg_ideal['N']),
        proximity(P,        *veg_ideal['P']),
        proximity(K,        *veg_ideal['K']),
        proximity(temp,     *veg_ideal['temperature']),
        proximity(hum,      *veg_ideal['humidity']),
        proximity(ph,       *veg_ideal['ph']),
        proximity(rainfall, *veg_ideal['rainfall']),
    ]
    # Cap at 70 so ML model crops (which are more authoritative) take priority in All Categories
    raw = (sum(scores) / len(scores)) * 100
    return round(min(raw, 70.0), 2)
