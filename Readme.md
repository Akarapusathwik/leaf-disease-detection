# 🌿 Plant Disease Detection Web App using EfficientNet and Flask
:

📝 Abstract
This project presents a web-based system for detecting plant leaf diseases using deep learning. Leveraging the EfficientNetB0 architecture and trained on the PLD_3_Classes_256 dataset, the model classifies leaf images into Early Blight, Late Blight, or Healthy. The user-friendly Flask web interface allows farmers and researchers to upload images, view predictions with confidence scores, and receive actionable treatment tips. This tool aims to support early disease diagnosis and promote healthier crop management through accessible AI technology.

---

This project is a web-based application that detects **plant leaf diseases** using a deep learning model. Built with **Flask** and **EfficientNetB0**, it classifies uploaded images into one of three categories:

- ✅ Healthy
- 🍂 Early Blight
- 🍂 Late Blight

---

## 🚀 Features

- 📷 Upload plant leaf images through a simple web interface
- 🤖 Predicts disease class using a trained EfficientNetB0 model
- 📊 Displays confidence score and treatment tips
- 🎨 Beautiful, animated UI with HTML + CSS
- 🗂 Organized codebase (Flask, templates, static folders)

---

## 📁 Dataset

- **Name**: `PLD_3_Classes_256`
- **Source**: [Kaggle Dataset Link](https://www.kaggle.com/datasets/smaranjitghose/plant-disease-detection-dataset)
- **Classes**: `Early_Blight`, `Late_Blight`, `Healthy`
- **Image Size**: Resized to `128x128`

> 📌 **Note**: The dataset is **not included** in this repository due to size restrictions. Please download it manually from the above link and use it only for training/testing locally.

---

## 💾 Project Structure

leaf-disease-detection/
│
├── app.py # Flask backend
├── final_model.keras # Trained model (EfficientNetB0)
├── templates/
│ ├── index.html # Upload page
│ └── result.html # Result display page
├── static/
│ └── uploads/ # Uploaded images (auto-generated)
├── .gitignore # Files/folders to exclude from git
└── README.md # You're reading it!

---

## 🧠 Model Overview

- **Architecture**: EfficientNetB0
- **Input Shape**: 128x128x3
- **Output Classes**: 3
- **Training Details**:
  - Optimizer: Adam
  - Loss: Categorical Crossentropy
  - Augmentation: Flip, Rotate, Zoom
  - Epochs: ~15–30 (early stopping used)
- **Frameworks**: TensorFlow, Keras

---
