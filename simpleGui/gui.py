# simple gui with labels and buttons


from Tkinter import *

#create the window

root = Tk()

#modify root window

root.title("labels and buttons")
root.geometry("200x200")

app = Frame(root)
app.grid()

label = Label(app, text = "this is a label!")
label.grid()

button = Button(app, text = "this is a button!")
button.grid()

#kick off the event loop

root.mainloop()
