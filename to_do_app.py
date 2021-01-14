from tkinter import *

def name():
	print("My name is Nidhin!")

class AddTask(Frame):
	def __init__(self, master):
		super(AddTask, self).__init__(master)
		self.grid()
		self.button_clicks = 0
		self.display_widgets()

		with open("tasks.txt", "r") as task_file:
			self.tasks = task_file.readlines()

			for i in range(len(self.tasks)):
				if self.tasks[i][-2:] == "\n":
					self.tasks[i] = self.tasks[i][:-2]
	
	def display_widgets(self):
		self.label1 = Label(self, text = "Enter task name to add, delete or check:")
		self.label1.grid(row=0, column=0, columnspan=2, sticky=W)

		self.task = Entry(self)
		self.task.grid(row=1, column=0, columnspan=2, sticky=W)

		self.button1 = Button(self, text="Add task")
		self.button1["command"] = self.addTask
		self.button1.grid(row=2, column=0, sticky=W)

		self.button2 = Button(self, text="Check task")
		self.button2["command"] = self.checkTask
		self.button2.grid(row=2, column=1, sticky=W)

		self.button3 = Button(self, text="Delete task")
		self.button3["command"] = self.deleteTask
		self.button3.grid(row=2, column=2, sticky=W)

		self.button4 = Button(self, text="Show all tasks")
		self.button4["command"] = self.showTask
		self.button4.grid(row=3, column=0, sticky=W)

		self.button5 = Button(self, text="Delete all tasks")
		self.button5["command"] = self.purgeTask
		self.button5.grid(row=3, column=1, sticky=W)
		
		self.textbox = Text(self, width = 35, height = 11, wrap=WORD)
		self.textbox.grid(row=4, column=0, columnspan=3, sticky=W)
	
	def addTask(self):
		to_add = self.task.get()
		self.task.delete(0, END)
		self.textbox.delete(0.0, END)

		if to_add == "":
			self.textbox.insert(0.0, "Type a task!")
			return

		with open("tasks.txt", "a") as task_file:
			task_file.write(to_add + "\n")

		self.tasks.append(to_add)
		self.textbox.insert(0.0, to_add + " has been added to the list of tasks.")
	
	def deleteTask(self):
		to_delete = self.task.get()
		self.task.delete(0, END)
		self.textbox.delete(0.0, END)

		if to_delete == "":
			self.textbox.insert(0.0, "Type a task!")
			return

		if to_delete not in self.tasks:
			self.textbox.insert(0.0, to_delete + " is not in the list of tasks.")

		else:
			self.tasks.remove(to_delete)
			with open("tasks.txt", "w") as task_file:
				for task in self.tasks:
					task_file.write(task + "\n")
			self.textbox.insert(0.0, to_delete + " has been removed from the list of tasks.")
	
	def checkTask(self):
		to_check = self.task.get()
		self.task.delete(0, END)
		self.textbox.delete(0.0, END)
		if to_check == "":
			self.textbox.insert(0.0, "Type a task!")
			return

		if to_check in self.tasks:
			message = to_check + " is in the list of tasks."
		else:
			message = to_check + " is not in the list of tasks."
		
		self.textbox.insert(0.0, message)
		
	def showTask(self):
		self.textbox.delete(0.0, END)

		if self.tasks == []:
			self.textbox.insert(0.0, "There are no tasks to show.")
			return

		for task in self.tasks:
			self.textbox.insert(END, task + "\n")
		self.textbox.yview_scroll(len(self.tasks), "units")
	
	def purgeTask(self):
		self.textbox.delete(0.0, END)

		self.tasks = []
		with open("tasks.txt", "w") as task_file:
			pass
		self.textbox.insert(0.0, "All tasks have been removed.")

if __name__ == "__main__":
	window = Tk()

	window.title("My ToDo App")
	window.geometry("300x320")

	app = AddTask(window)

	window.mainloop()
