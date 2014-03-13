
from Tkinter import *

class Application(Frame):
	""" A GUI Application with 3 buttons """
	def __init__(self, master):
		""" Initialize the frame """
		Frame.__init__(self, master)
		self.grid()
		self.button_clicks = 0 # count the number of button clicks
		self.create_widgets()
	
	def create_widgets(self):
		self.button = Button(self) 
		self.button["text"] = "Total clicks: 0"
		self.button["command"] = self.update_count
		self.button.grid()
	
	def update_count(self):
		""" increase the click counts and display the new total """
		self.button_clicks += 1
		self.button["text"] = "Total clicks: " + str(self.button_clicks)
		
	
root = Tk()

root.title("OOP")	
root.geometry("200x200")

app = Application(root)

root.mainloop()
