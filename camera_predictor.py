import tkinter as tk
from tkinter import simpledialog
from tkinter import*
import cv2 as cv
import os
import PIL.Image, PIL.ImageTk
from PIL import Image
import machine_learning
import camera_capture

class App:

    def __init__(self, root_title="CamPredictor"):
        self.root = tk.Tk() 
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")
        self.root.title(root_title)
        self.root.configure(bg='black')

        self.img1 = PIL.Image.open('Images/camerapic2.png')
        self.rez1 = self.img1.resize((320,320))
        self.new1 = PIL.ImageTk.PhotoImage(self.rez1)
        self.image1 = Label(self.root, image=self.new1,bg='black')
        self.image1.image=self.new1
        self.image1.place(x=1020,y=200)

        self.img2 = PIL.Image.open('Images/camerapic1.png')
        self.rez2 = self.img2.resize((320,320))
        self.new2 = PIL.ImageTk.PhotoImage(self.rez2)
        self.image2 = Label(self.root, image=self.new2,bg='black')
        self.image2.image=self.new2
        self.image2.place(x=20,y=200)

        self.img3 = PIL.Image.open('Images/turtlelogo.png')
        self.rez3 = self.img3.resize((150,150))
        self.new3 = PIL.ImageTk.PhotoImage(self.rez3)
        self.image3 = Label(self.root, image=self.new3,bg='black')
        self.image3.image=self.new3
        self.image3.place(x=20,y=20)

        self.img4 = PIL.Image.open('Images/turtlelogo.png')
        self.rez4 = self.img4.resize((150,150))
        self.new4 = PIL.ImageTk.PhotoImage(self.rez4)
        self.image4 = Label(self.root, image=self.new4,bg='black')
        self.image4.image=self.new4
        self.image4.place(x=20,y=550)

        self.img5 = PIL.Image.open('Images/turtlelogo.png')
        self.rez5 = self.img5.resize((150,150))
        self.new5 = PIL.ImageTk.PhotoImage(self.rez5)
        self.image5 = Label(self.root, image=self.new5,bg='black')
        self.image5.image=self.new5
        self.image5.place(x=1180,y=20)

        self.img6 = PIL.Image.open('Images/turtlelogo.png')
        self.rez6 = self.img6.resize((150,150))
        self.new6 = PIL.ImageTk.PhotoImage(self.rez6)
        self.image6 = Label(self.root, image=self.new6,bg='black')
        self.image6.image=self.new6
        self.image6.place(x=1180,y=550)

        self.counters = [1, 1]
        self.model = machine_learning.Model()
        self.auto_predict = False
        self.camera = camera_capture.Camera()
        self.init_gui()
        self.delay = 1
        self.update()
        self.root.attributes('-topmost', True)
        self.root.mainloop()

    def init_gui(self):
        self.canvas = tk.Canvas(self.root, width=self.camera.width, height=self.camera.height)
        self.canvas.pack()

        self.classname_one = simpledialog.askstring("Classname One", "Enter the name of the first class:", parent=self.root)
        self.classname_two = simpledialog.askstring("Classname Two", "Enter the name of the second class:", parent=self.root)

        self.btn_toggleauto = tk.Button(self.root, text="Auto Prediction",font=('Arial',11,'bold'), width=50, command=self.auto_predict_toggle)
        self.btn_toggleauto.pack(anchor=tk.CENTER, expand=True)

        self.btn_class_one = tk.Button(self.root, text=self.classname_one, width=50, font=('Arial',11,'bold'),command=lambda: self.save_for_class(1))
        self.btn_class_one.pack(anchor=tk.CENTER, expand=True)

        self.btn_class_two = tk.Button(self.root, text=self.classname_two, width=50, font=('Arial',11,'bold'),command=lambda: self.save_for_class(2))
        self.btn_class_two.pack(anchor=tk.CENTER, expand=True)

        self.btn_train = tk.Button(self.root, text="Train Model", width=50, font=('Arial',11,'bold'),command=lambda: self.model.train_model(self.counters))
        self.btn_train.pack(anchor=tk.CENTER, expand=True)

        self.btn_predict = tk.Button(self.root, text="Predict", width=50, font=('Arial',11,'bold'),command=self.predict)
        self.btn_predict.pack(anchor=tk.CENTER, expand=True)

        self.btn_reset = tk.Button(self.root, text="Reset", width=50, font=('Arial',11,'bold'),command=self.reset)
        self.btn_reset.pack(anchor=tk.CENTER, expand=True)

        self.class_label = tk.Label(self.root, text="RESULT",font=('Arial',12,'bold'),bg='light blue')
        self.class_label.config(font=("Arial", 20))
        self.class_label.pack(anchor=tk.CENTER, expand=True)

    def auto_predict_toggle(self):
        self.auto_predict = not self.auto_predict
        if self.auto_predict:
            self.predict()


    def save_for_class(self, class_num):
        ret, frame = self.camera.get_frame()
        if not os.path.exists('1'):
            os.mkdir('1')
        if not os.path.exists('2'):
            os.mkdir('2')

        cv.imwrite(f"{class_num}/frame{self.counters[class_num - 1]}.jpg", cv.cvtColor(frame, cv.COLOR_RGB2GRAY))
        img = PIL.Image.open(f"{class_num}/frame{self.counters[class_num - 1]}.jpg")
        img = img.resize((150, 150), Image.BILINEAR)
        img.save(f"{class_num}/frame{self.counters[class_num - 1]}.jpg")
        self.counters[class_num - 1] += 1

    def reset(self):
        for folder in ['1', '2']:
            for file in os.listdir(folder):
                file_path = os.path.join(folder, file)
                if os.path.isfile(file_path):
                    os.unlink(file_path) # If the file is indeed a regular file, it deletes it using os.unlink() (which is equivalent to os.remove() but is also available on Unix-based systems)

        self.counters = [1, 1]
        self.model = machine_learning.Model()
        self.class_label.config(text='RESULT')

    def update(self):
        if self.auto_predict:
            self.predict()
        ret, frame = self.camera.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

            self.root.after(self.delay, self.update)

    def predict(self):
        ret, frame = self.camera.get_frame()
        if ret:
            prediction = self.model.predict(frame)

            if prediction == 1:
                self.class_label.config(text=self.classname_one)
            elif prediction == 2:
                self.class_label.config(text=self.classname_two)
            else:
                self.class_label.config(text="Unknown")
        else:
            self.class_label.config(text="Frame retrieval failed")


def main():
    App(root_title='Camera Classifier')


if __name__ == '__main__':
    main()
