import tensorflow as tf
from tensorflow import keras
import os
import numpy as np
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


model = tf.keras.models.load_model('./digitdetect.h5')

root = Tk()
root.title("Digit Recognition")
root.geometry("700x700")

# Define functions for image upload and prediction
def upload_image():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    show_image(img)
    img = img.resize((28, 28)).convert('L')
    img = np.array(img).astype('float32') / 255.0
    img = np.reshape(img, (1, 28, 28, 1)) 
    pred = model.predict(img)
    digit = np.argmax(pred)
    result_label.config(text=f"Predicted digit: {digit}", font = ("Arial Bold", 28), highlightthickness=0, bd=0)

def show_image(img):
    img = img.resize((300,300))
    photo_img = ImageTk.PhotoImage(img)
    image_label.config(image=photo_img)
    image_label.image = photo_img

def on_enter(e):
    predict_button.config(bg='green')

def on_leave(e):
    predict_button.config(bg='white')

# Add GUI elements
title_label = Label(root, text="Digit Detector", font=("Arial Bold", 50))
title_label.pack(pady=20)


# Load the first image
img1 = Image.open("digitalimagefinal-PhotoRoom.png-PhotoRoom.png")
img1 = ImageTk.PhotoImage(img1)

# Create a label for the first image and place it on the left
label1 = Label(root, image=img1)
label1.place(x=0, y= 200)

# Load the second image
img2 = Image.open("logo-no-background.png")
img2 = img2.resize((649, 102)) # Resize the image
img2 = ImageTk.PhotoImage(img2)

# Create a label for the second image and place it on the right
label2 = Label(root, image=img2)
label2.place(x= 30, y= 5)


image_label = Label(root)
image_label.pack()



predict_button = Button(root, text="Predict Digit", command=upload_image, font=("Arial", 16), padx=20, pady=10)
predict_button.pack(pady=50)

predict_button.bind("<Enter>", on_enter)
predict_button.bind("<Leave>", on_leave)


result_label = Label()
result_label.pack(pady=10)

# Run the GUI
root.mainloop()