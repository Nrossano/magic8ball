"""
Filename: magic8ball.py
Created by: Nicholas Rossano
Date: 4/1/2019

GUI-based "Magic 8 ball" program. Must have breezypythongui.py and 8ball.png in cwd. Requires and pip install Pillow.
"""

from breezypythongui import EasyFrame
import random
from tkinter import PhotoImage
from tkinter.font import Font
from PIL import ImageTk,Image

class MagicBall(EasyFrame):

	def __init__(self):
		#Create the main frame
		EasyFrame.__init__(self, title = "Magic 8 ball")

		#Image and text labels
		self.setResizable(False)
		imageLabel = self.addLabel(text="", row = 4, column = 0, sticky = "NSEW")
		textLabel = self.addLabel(text="The Magic 8-Ball Knows All!", row = 0, column = 0, sticky = "NSEW")
		textLabel2 = self.addLabel(text="What is your question?", row = 1, column = 0, sticky = "NSEW")
		textLabel3 = self.addLabel(text="You asked:", row = 5, column = 0, sticky = "NSEW")
		textLabel4 = self.addLabel(text="My reply:", row = 7, column = 0, sticky = "NSEW")

		#Load the image and associate it with the image label
		self.image = PhotoImage(file = "8ball.png")
		imageLabel["image"] = self.image

		#Set the font and color of the captions
		myFont = Font(family = "Arial", size = 25)
		textLabel["font"] = myFont
		textLabel["foreground"] = "black"

		myFont2 = Font(family = "Arial", size = 23)
		textLabel2["font"] = myFont2
		textLabel2["foreground"] = "black"

		myFont3 = Font(family = "Arial", size = 13)
		textLabel3["font"] = myFont3
		textLabel3["foreground"] = "black"

		textLabel4["font"] = myFont3
		textLabel4["foreground"] = "black"

		#Input
		self.inputField = self.addTextField(text = "", row = 2, column = 0, sticky = "NSEW")

		#Button
		self.askButton = self.addButton(text = "Ask your question!", row = 3, column = 0, columnspan = 3, command = self.ask)

		#Outputs
		self.outputField1 = self.addTextField(text = "", row = 6, column = 0, state = "readonly", sticky = "NSEW")
		self.outputField = self.addTextField(text = "", row = 8, column = 0, state = "readonly", sticky = "NSEW")

	#Function for the button
	def ask(self):

		#Takes user entry from inputField and puts it in outputField1
		text = self.inputField.getText()
		self.outputField1.setText(text)

		#Randomly generates a response on button press
		answers = random.randint(1,8)

		if answers == 1:
			self.outputField.setText("It is certain.")

		elif answers == 2:
			self.outputField.setText("Without a doubt.")

		elif answers == 3:
			self.outputField.setText("Signs point to yes.")

		elif answers == 4:
			self.outputField.setText("Outlook good.")

		elif answers == 5:
			self.outputField.setText("Concentrate and ask again.")

		elif answers == 6:
			self.outputField.setText("Cannot predict now.")

		elif answers == 7:
			self.outputField.setText("My sources say no.")

		elif answers == 8:
			self.outputField.setText("Very doubtful.")

def main():
	MagicBall().mainloop()

main()

