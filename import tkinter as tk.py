import tkinter as tk

root = tk.Tk()
root.title('My Window')
root.geometry('400x400')

# Create a Textbox
textbox = tk.Text(root, height=10)
textbox.pack(pady=20)

# Create a frame to center the buttons
frame = tk.Frame(root)
frame.pack()

# Create a Button
button1 = tk.Button(frame, text='Button 1')
button1.pack(side=tk.LEFT, padx=10, pady=10)

# Create another Button
button2 = tk.Button(frame, text='Button 2')
button2.pack(side=tk.LEFT, padx=10, pady=10)

# Center the buttons vertically in the frame
frame.pack_propagate(0)  # Prevent the frame from resizing
button1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
button2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
