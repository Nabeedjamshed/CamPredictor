CamPredictor
CamPredictor is a simple Python application for real-time image classification using a webcam. It allows users to capture images, label them into different classes, train a machine learning model based on the labeled data, and make predictions on new images captured from the webcam.

Features:
Real-time Image Classification: The application captures images from the webcam and classifies them into predefined classes.

Interactive GUI: The user interface provides buttons for capturing images, labeling them into different classes, training the model, and making predictions.

Automatic Prediction Mode: Users can enable automatic prediction mode, where the application continuously predicts the class of images captured from the webcam without manual intervention.

Model Training: The application utilizes scikit-learn's LinearSVC model for training, allowing users to create a custom classifier based on their labeled data.

Components:
camera_capture.py: Defines the Camera class responsible for accessing the webcam and capturing frames.

machine_learning.py: Contains the Model class, which handles model training and prediction using scikit-learn's LinearSVC model.

camera_predictor.py: Implements the main application logic, including the graphical user interface (GUI) using Tkinter.

main.py: Entry point for running the application. Instantiates and launches the App class defined in camera_predictor.py.

Images/: Contains images used for GUI elements, such as buttons and logos.

Usage:
Run main.py to launch the application. Use the GUI to capture and label images, train the model, and make predictions. Optionally, enable automatic prediction mode for continuous image classification.

Requirements:
Python 3.x OpenCV (cv2) scikit-learn Pillow (PIL) Tkinter

Credits
Author: Nabeed Jamshed
