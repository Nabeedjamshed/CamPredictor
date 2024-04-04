import cv2 as cv

class Camera:

    def __init__(self):
        self.camera = cv.VideoCapture(0)
        if not self.camera.isOpened():
            raise ValueError("Unable to open a camera!")
        
        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()
    
    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:
                return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return None

# Importing OpenCV library:
# import cv2 as cv
# This line imports the OpenCV library with an alias 'cv'.

# Defining the Camera class:
# class Camera:
# Here, a class named 'Camera' is defined.

# Initializing the Camera object:
# def __init__(self):
#     self.camera = cv.VideoCapture(0)
#     if not self.camera.isOpened():
#         raise ValueError("Unable to open a camera!")
#     self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
#     self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)
# In the constructor __init__, an instance of VideoCapture is created using cv.VideoCapture(0). The argument 0 typically refers to the default camera.
# It checks if the camera is opened or not using self.camera.isOpened(). If it's not open, it raises a ValueError with a message "Unable to open a camera!".
# It gets the width and height of the video frames from the camera using self.camera.get(cv.CAP_PROP_FRAME_WIDTH) and self.camera.get(cv.CAP_PROP_FRAME_HEIGHT) respectively, and stores them in self.width and self.height attributes.
# Destructor:
# def __del__(self):
#     if self.camera.isOpened():
#         self.camera.release()
# This defines a destructor method __del__ to release the camera when the object is destroyed. It checks if the camera is opened using self.camera.isOpened() and if it is, it releases the camera using self.camera.release().

# Method to get frames from the camera:
# def get_frame(self):
#     if self.camera.isOpened():
#         ret, frame = self.camera.read()
#         if ret:
#             return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
#         else:
#             return (ret, None)
#     else:
#         return None
# This method named get_frame captures frames from the camera.
# It first checks if the camera is opened.
# It reads a frame from the camera using self.camera.read(), which returns a boolean value ret indicating whether a frame was successfully read and the frame itself.
# If a frame is read successfully (ret is True), it converts the frame from BGR to RGB color space using cv.cvtColor(frame, cv.COLOR_BGR2RGB) before returning it along with ret.
# If a frame is not read successfully (ret is False), it returns None.
# Overall, this code defines a class Camera that encapsulates functionality for interacting with a camera, including initialization, releasing resources, and capturing frames.

# self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
#     self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)

# explain above part deeply
# Certainly! The lines you mentioned are retrieving the width and height of the frames being captured by the camera. Let's break it down:

# Accessing Properties:
# self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
# self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)
# These lines use the get() method of the VideoCapture object self.camera to retrieve specific properties of the camera. In this case, the properties being retrieved are cv.CAP_PROP_FRAME_WIDTH and cv.CAP_PROP_FRAME_HEIGHT. These constants are provided by OpenCV and represent the width and height of the video frames respectively.

# Width and Height Assignment:
# self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
# self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)
# The values returned by self.camera.get(cv.CAP_PROP_FRAME_WIDTH) and self.camera.get(cv.CAP_PROP_FRAME_HEIGHT) are assigned to self.width and self.height respectively. These assignments allow easy access to the width and height of the frames throughout the Camera class.

# Frame Width and Height:
# These values represent the dimensions of each frame captured by the camera. The width and height are essential parameters when dealing with image processing tasks such as resizing, scaling, or displaying the captured frames.

# Usage:
# After these lines execute, self.width and self.height will hold the width and height of the frames being captured by the camera, respectively. These attributes can be accessed from any method within the Camera class or even from outside the class if the Camera object is instantiated. They provide convenient access to the frame dimensions, which can be crucial for various image processing tasks or setting up the camera display appropriately.

# if self.camera.isOpened():
#         ret, frame = self.camera.read()
#         if ret:
#             return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))

# deeply explain above code and what is cv.COLOR_BGR2RGB)?
# Sure, let's break down the code block:
# if self.camera.isOpened():
#     ret, frame = self.camera.read()
#     if ret:
#         return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
# self.camera.isOpened():

# This condition checks if the camera has been successfully opened. If the camera is opened successfully, the condition evaluates to True, allowing the subsequent code block to execute. If the camera is not opened, the code inside this block will not execute.
# ret, frame = self.camera.read():

# This line reads a frame from the camera.
# The read() method of VideoCapture object self.camera returns two values: ret and frame.
# ret is a boolean value indicating whether a frame was successfully read. If a frame is read successfully, ret will be True, otherwise False.
# frame contains the actual image data of the frame.
# if ret::

# This condition checks if ret is True, meaning that a frame has been successfully read from the camera. If ret is True, the code block inside this condition executes.
# cv.cvtColor(frame, cv.COLOR_BGR2RGB):

# This function converts the color space of the frame.
# frame is the image data read from the camera, typically in BGR (Blue, Green, Red) color space.
# cv.COLOR_BGR2RGB is a flag specifying the conversion from BGR to RGB color space.
# OpenCV represents colors in BGR format by default, but many other libraries (including ones for image display like Matplotlib) expect images in RGB format. So, this conversion is necessary for compatibility with other libraries or operations.
# Return Statement:

# If both conditions (self.camera.isOpened() and ret) are True, the function returns a tuple (ret, converted_frame).
# ret is the boolean indicating successful frame capture (True if successful, False otherwise).
# converted_frame is the frame data after conversion from BGR to RGB color space.
# Overall Functionality:

# This code block ensures that if the camera is opened and a frame is successfully read, the frame is converted from BGR to RGB color space before being returned along with the ret value. This ensures compatibility with other libraries or processes that expect RGB format frames. If any of the conditions fail, it returns None.