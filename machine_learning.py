from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
import numpy as np
import PIL.Image, PIL.ImageTk
from PIL import Image
import cv2 as cv

class Model:
    def __init__(self):
        self.scaler = StandardScaler()
        self.model = LinearSVC(dual=True, max_iter=5000)  
    
    def train_model(self, counters):
        img_list = []
        class_list = []

        for i in range(1, counters[0]):
            img = cv.imread(f'1/frame{i}.jpg')[:, :, 0]
            img = img.reshape(22500)
            img_list.append(img)
            class_list.append(1)

        for i in range(1, counters[1]):
            img = cv.imread(f'2/frame{i}.jpg')[:, :, 0]
            img = img.reshape(22500)
            img_list.append(img)
            class_list.append(2)

        img_list = np.array(img_list)
        class_list = np.array(class_list)

        img_list_scaled = self.scaler.fit_transform(img_list)
        
        self.model.fit(img_list_scaled, class_list)
        print("Model has been trained")

    def predict(self, frame):
        if frame.ndim == 2:
            gray_frame = frame 
        else:
            gray_frame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)

        cv.imwrite("frame.jpg", gray_frame)
        img = PIL.Image.open("frame.jpg")
        img = img.resize((150, 150), Image.BILINEAR)  
        img.save("frame.jpg")

        img = cv.imread('frame.jpg')[:, :, 0]
        img = img.reshape(22500)
        img_scaled = self.scaler.transform([img])
        
        prediction = self.model.predict(img_scaled)

        return prediction[0]


# StandardScaler:

# Imagine you have different types of fruits like apples, oranges, and bananas. Some are measured in grams, some in kilograms, and some in pounds. To make them all comparable, you decide to convert them to a common unit, like kilograms. That's what StandardScaler does for the features in your dataset. It makes sure they are all on the same scale, so they can be compared properly.
# So, StandardScaler takes your features and adjusts them so that they have a similar range of values. It doesn't change the shape of the data, just the scale.
# LinearSVC:

# Now, think of LinearSVC as a smart machine that learns to classify things. Let's say you want to teach it to differentiate between apples and oranges based on their size and weight. LinearSVC will look at a bunch of apples and oranges with known sizes and weights, and it will learn to draw a line that best separates them. This line helps it decide if a new fruit is an apple or an orange based on its size and weight.
# So, LinearSVC learns from examples and creates a "decision line" to classify new data. It's like a smart student learning from past examples to make predictions about new situations.
# In summary:

# StandardScaler makes sure all your data is measured in the same units, so it's easier to compare.
# LinearSVC is a smart algorithm that learns from examples to classify new data based on what it has learned. It's like a student studying past examples to make predictions about new situations.

# Think of fit_transform as a magic spell that makes your data ready for learning!

# Fit: First, it learns from your data. It figures out important stuff like the average and spread of each feature.

# Transform: Then, it applies what it learned to your data. It adjusts your data based on the things it figured out during the learning step.

# Imagine you're baking a cake. First, you learn the recipe and gather the ingredients (that's the fitting part). Then, you actually make the cake using those ingredients and following the recipe (that's the transforming part).

# So, fit_transform is like learning the recipe and baking the cake at the same time! It's a handy shortcut to get your data ready for learning without having to do multiple steps.










