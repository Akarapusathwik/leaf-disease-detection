from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = load_model('final_model.keras')

# Class labels
class_labels = ['Early_Blight', 'Healthy', 'Late_Blight']

# Remedial tips
TIPS = {
    'Early_Blight': "Apply a protective fungicide containing chlorothalonil or mancozeb. Remove and destroy infected leaves. Rotate crops next season.",
    'Late_Blight':   "Use copper-based fungicides at the first sign. Ensure good air circulation and avoid overhead irrigation.",
    'Healthy':       "No treatment needed. Maintain good cultural practices and monitor regularly."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    # Save the uploaded file
    upload_folder = 'static/uploads'
    os.makedirs(upload_folder, exist_ok=True)
    filepath = os.path.join(upload_folder, file.filename)
    file.save(filepath)

    # Preprocess the image
    img = image.load_img(filepath, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    preds = model.predict(img_array)[0]
    pred_class = int(np.argmax(preds))
    predicted_label = class_labels[pred_class]
    confidence = round(float(preds[pred_class]) * 100, 2)

    # Prepare display values
    filename = file.filename
    tip = TIPS[predicted_label]

    return render_template(
        'result.html',
        prediction=predicted_label.replace('_', ' '),
        confidence=confidence,
        tip=tip,
        filename=filename
    )

if __name__ == '__main__':
    app.run(debug=True)
