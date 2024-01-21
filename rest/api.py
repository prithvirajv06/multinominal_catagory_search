from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS
app = Flask(__name__)

# Load the saved vectorizer and classifier
vectorizer = joblib.load('./model/tfidf_vectorizer.joblib')
clf = joblib.load('./model/naive_bayes_classifier.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input text from the request
        input_text = request.json['text']

        # Preprocess and vectorize the input text
        input_tfidf = vectorizer.transform([input_text])

        # Make a prediction
        predicted_category = clf.predict(input_tfidf)[0]

        # Return the predicted category as JSON
        return jsonify({'predicted_category': predicted_category})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)
