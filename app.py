from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the model
model = joblib.load('demand_forecasting_model.pkl')

# Initialize Flask app
app = Flask(__name__)

# Define a route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    data = request.get_json(force=True)
    
    # Convert data into DataFrame
    df = pd.DataFrame(data)
    
    # Make predictions
    predictions = model.predict(df)
    
    # Return predictions as JSON
    return jsonify(predictions.tolist())

# Run the app
if __name__ == '__main__':
    app.run(debug=True)