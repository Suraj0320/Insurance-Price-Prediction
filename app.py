from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

# Load the trained model
with open('svr_pipeline.pkl', 'rb') as f:
    svr_pipeline = pickle.load(f)

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_expenses():
    try:
        # Get the data from the POST request
        data = request.get_json()
        
        # Ensure all required keys are in the data
        required_keys = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
        if not all(key in data for key in required_keys):
            return jsonify({'error': 'Missing data'}), 400
        
        # Create a DataFrame from the data
        df = pd.DataFrame([data])
        
        # Predict the expenses
        prediction = svr_pipeline.predict(df)
        
        # Return the prediction as a JSON response
        return jsonify({'predicted_expenses': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
