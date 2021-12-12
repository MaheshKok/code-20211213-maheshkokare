sample_data = [
    {"Gender": "Male", "HeightCm": 250, "WeightKg": 77},
    {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
    {"Gender": "Male", "HeightCm": 145, "WeightKg": 77},
    {"Gender": "Female", "HeightCm": 135, "WeightKg": 77},
    {"Gender": "Female", "HeightCm": 175, "WeightKg": 60},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
    {"Gender": "Female", "HeightCm": 164, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 155, "WeightKg": 70},
]


# for simplicity i have multiplied data set with 100000 to generate 1 million data set
data = sample_data * 100000


# BMI Category and the Health Risk.
category_health_risk = {
    (0, 18.4): ("Underweight", "below Malnutrition risk"),
    (18.5, 24.9): ("Normal weight", "Low risk"),
    (25, 29.9): ("Overweight", "Enhanced risk"),
    (30, 34.9): ("Moderately obese", "Medium risk"),
    (35, 39.9): ("Severely obese", "High risk"),
    (40, 100): ("Very severely obese", "above Very high risk"),
}
