def load_model(model_path):
    import joblib
    return joblib.load(model_path)

def preprocess_input(input_data):
    import pandas as pd
    # Assuming input_data is a dictionary
    df = pd.DataFrame([input_data])
    # Add any necessary preprocessing steps here
    return df

def make_prediction(model, input_data):
    processed_data = preprocess_input(input_data)
    prediction = model.predict(processed_data)
    return prediction

if __name__ == "__main__":
    import sys
    import json

    model_path = "model.joblib"  # Path to the trained model
    model = load_model(model_path)

    # Example input data
    input_data = json.loads(sys.stdin.read())
    
    prediction = make_prediction(model, input_data)
    print(prediction)