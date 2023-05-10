import tensorflow as tf
from tensorflow import keras
import os
import numpy as np
import PIL
from PIL import Image
from PIL import ImageTk
import tkinter as tk
from tkinter import *
from tkinter import filedialog


model = tf.keras.models.load_model('./digitdetect.h5')
#model.summary()

root = Tk()

# Define functions for image upload and prediction
def upload_image():
    file_path = filedialog.askopenfilename()
    img = PIL.Image.open(file_path)
    show_image(img)
    img = img.resize((28, 28)).convert('L')
    img = np.array(img).astype('float32') / 255.0
    img = np.reshape(img, (1, 28, 28, 1)) 

    return img

def show_image(img):
    img = img.resize((300,300))
    photo_img = ImageTk.PhotoImage(img)
    image_label.config(image=photo_img)
    image_label.image = photo_img

def predict_digit():
    img = upload_image()
    pred = model.predict(img)
    digit = np.argmax(pred)
    result_label.config(text=f"Predicted digit: {digit}")

# Add GUI elements
upload_button = Button(root, text="Upload image", command=upload_image)
upload_button.pack()

image_label = Label(root)
image_label.pack()

predict_button = Button(root, text="Predict digit", command=predict_digit)
predict_button.pack()

result_label = Label(root)
result_label.pack()

# Run the GUI
root.mainloop()