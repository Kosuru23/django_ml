# polss/views.py

from django.shortcuts import render
from .models import PredictionInput
import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), 'models.pkl')
model = joblib.load(model_path)

def index_views(request):
    return render(request, 'index.html')

def save_index(request):
    prediction = None

    if request.method == 'POST':
        income = float(request.POST.get('income'))
        children = int(request.POST.get('children'))
        home_owner = bool(int(request.POST.get('home_owner')))
        cars = int(request.POST.get('cars'))
        age = int(request.POST.get('age'))
        occupation = request.POST.get('occupation')
        education = request.POST.get('education')
        marital_status = bool(int(request.POST.get('marital_status')))
        gender = bool(int(request.POST.get('gender')))
        commute_lower = float(request.POST.get('commute_lower'))
        commute_upper = float(request.POST.get('commute_upper'))
        region = request.POST.get('region')

        user_input = PredictionInput.objects.create(
            income=income,
            children=children,
            home_owner=home_owner,
            cars=cars,
            age=age,
            occupation=occupation,
            education=education,
            marital_status=marital_status,
            gender=gender,
            commute_lower=commute_lower,
            commute_upper=commute_upper,
            region=region
        )

        input_vector = convert_to_model_input(user_input)
        prediction = model.predict([input_vector])[0]

    return render(request, 'index.html', {'prediction': prediction})

def convert_to_model_input(data):
    """
    Convert a PredictionInput instance to a feature vector for the ML model.
    This assumes one-hot encoding for occupation, education, and region.
    Update this based on your model's training setup!
    """
    # One-hot mappings
    occupation_map = {
        'Clerical': [1, 0, 0, 0, 0],
        'Management': [0, 1, 0, 0, 0],
        'Manual': [0, 0, 1, 0, 0],
        'Professional': [0, 0, 0, 1, 0],
        'Skilled Manual': [0, 0, 0, 0, 1],
    }

    education_map = {
        'Bachelors': [1, 0, 0, 0, 0],
        'Graduate Degree': [0, 1, 0, 0, 0],
        'High School': [0, 0, 1, 0, 0],
        'Partial College': [0, 0, 0, 1, 0],
        'Partial High School': [0, 0, 0, 0, 1],
    }

    region_map = {
        'Europe': [1, 0, 0],
        'North America': [0, 1, 0],
        'Pacific': [0, 0, 1],
    }

    # Base numeric and boolean features
    base_features = [
        data.income,
        data.children,
        int(data.home_owner),
        data.cars,
        data.age,
        int(data.marital_status),
        int(data.gender),
        data.commute_lower,
        data.commute_upper,
    ]

    # Final input vector
    return base_features + occupation_map[data.occupation] + education_map[data.education] + region_map[data.region]

