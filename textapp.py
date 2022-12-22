import tkinter as tk
import pyperclip

# Create the main window
window = tk.Tk()
window.title("Text Message App")


root = tk.Tk()

# Create a frame to hold the text messages
frame = tk.Frame(root)
frame.pack()



# Create a function to be called when a button is clicked
def copy_text(text):
    pyperclip.copy(text)

# 
def add_message():
    message = input_field.get()
    label = tk.Label(frame, text=message)
    label.pack()
    label.bind("<Button-1>", lambda event: copy_to_clipboard(event, message))

# Create some buttons and labels
button1 = tk.Button(text="Message 1", command=lambda: copy_text("Message 1"))
button2 = tk.Button(text="Message 2", command=lambda: copy_text("Message 2"))
button3 = tk.Button(text="Message 3", command=lambda: copy_text("Message 3"))
label1 = tk.Label(text="Click a button to copy the message to the clipboard")

# Place the widgets in the window
button1.pack()
button2.pack()
button3.pack()
label1.pack()


# ... add more labels as needed

# Create an input field and "Add" button
input_field = tk.Entry(root)
input_field.pack()
add_button = tk.Button(root, text="Add", command=add_message)
add_button.pack()


# Run the main loop
window.mainloop()




