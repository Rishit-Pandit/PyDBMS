from utils import *
from decoders import *
from tkinter import filedialog, Text
import tkinter as tk
import os


if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as saved:
        tempDatasets = saved.read()
        tempDatasets = tempDatasets.split(',')
        datasets = [x for x in tempDatasets if x.strip()]

file = ""

class ResultsView(tk.Frame):
	def __init__(self, master, name):
		super().__init__(master)
		self.pack()
		self.root = master
		self.name = name

		self.canvas = tk.Canvas(self.root, height=500, width=800, bg="#98f673")
		self.canvas.pack()
    
		self.frame = tk.Frame(self.canvas, bg="#fefefe")
		self.frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

		self.label3 = tk.Label(self.frame, text=name, fg="#010101")
		self.label3.pack()

		self.OutputLog = tk.Text(self.frame, height=20, fg="#010101")
		self.OutputLog.pack()


class MainView(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.pack()
		self.root = master
		self.OUTPUT = []

		self.canvas = tk.Canvas(self.root, height=500, width=800, bg="#98f673")
		self.canvas.pack()
    
		self.frame = tk.Frame(self.canvas, bg="#fefefe")
		self.frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

		self.label1 = tk.Label(self.frame, text="Input", fg="#010101")
		self.label1.pack()

		self.InputSpace = tk.Text(self.frame, height=4, fg="#010101")
		self.InputSpace.pack()

		self.ExecuteButton = tk.Button(self.frame, text="Execute", padx=10, pady=5, fg="#fefefe", bg="#936584",command=self.executeCommand)
		self.ExecuteButton.pack()

		self.label3 = tk.Label(self.frame, text="Output", fg="#010101")
		self.label3.pack()

		self.OutputLog = tk.Text(self.frame, height=8, fg="#010101")
		self.OutputLog.pack()

	def executeCommand(self):
		self.query = self.InputSpace.get("1.0", "end")
		commandStr = self.query.upper().replace("\n", " ")
		print(commandStr)

		commandArr = commandStr.split(' ')
		commandArr.remove('')
		if ArrayContains(commandArr, "QUIT"):
			self.OUTPUT.append("Exiting...")
			quit()
		elif ArrayContains(commandArr, "CREATE"):
			classType, name = DecodeCreateCommand(commandArr)
			self.OUTPUT.append(f"Created {classType} {name}...")
		elif ArrayContains(commandArr, "INSERT"):
			classType, name = DecodeInsertCommand(commandArr)
			self.OUTPUT.append(f"Inserted Values in {classType} {name}...")
		elif ArrayContains(commandArr, "SELECT"):
			classType, name, OUTPUT_ = DecodeSelectCommand(commandArr)
			self.OUTPUT.append(f"Displaying Values of {classType} {name}...")
			showResult(OUTPUT_, name)
		elif ArrayContains(commandArr, "SAVE"):
			classType, name, filename = DecodeSaveCommand(commandArr)
			self.OUTPUT.append(f"Saving Values of {classType} {name} in file {filename} ...")
		elif ArrayContains(commandArr, "ALTER"):
			Type, name, AlterType = DecodeAlterCommand(commandArr)
			self.OUTPUT.append(f"{AlterType}ing field(s) to/from {Type} {name} ...")



		self.OutputLog.delete("1.0", "end")
		self.OutputLog.pack()
		for i in range(len(self.OUTPUT)):
			self.OutputLog.insert(f"{i}.0", str(self.OUTPUT[-i]) + "\n")
			self.OutputLog.pack()

      
def showResult(OUTPUT, name):
		resRoot = tk.Tk()
		resRoot.title("Table View")
		resultView = ResultsView(resRoot, name)

		resultView.OutputLog.delete("1.0", "end")
		resultView.OutputLog.pack()

		for i in range(1, len(OUTPUT)):
			resultView.OutputLog.insert(f"{i}.0", str(OUTPUT[i]) + "\n")
			resultView.OutputLog.pack()

		resultView.OutputLog.insert(f"{0}.0", str(OUTPUT[0]) + "\n")
		resultView.OutputLog.pack()
		resultView.mainloop()


root = tk.Tk()
root.title("Py DBMS")
myapp = MainView(root)
myapp.mainloop()
