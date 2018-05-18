from tkinter import * 
from tkinter import messagebox

root = Tk()
root.title("Bello")
root.geometry("400x400")


def donothing():
	print("Nothing")
	
todoList = ["Add some clazzy designs", "Learn Python", "Create some great softwares"]

def updateList():
	for item in todoList:
		print(item)
		# todoList.insert("end", item)
		
def close_window():
	root.destroy()

def aboutInfo():
	messagebox.showinfo("About Bello", "Bello is open source python application")

updateList()
# Menu Bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "New", command = donothing)
filemenu.add_command(label = "Add Task", command = donothing)
filemenu.add_command(label = "Save Task", command = donothing)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = close_window)

menubar.add_cascade(label = "File", menu = filemenu)

devmenu = Menu(menubar, tearoff = 0)
devmenu.add_command(label = "Contribute", command = donothing)
devmenu.add_command(label = "Source code", command = donothing)
menubar.add_cascade(label = "Development", menu = devmenu)

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "Help docs", command = donothing)
helpmenu.add_command(label = "About bello", command = aboutInfo)
menubar.add_cascade(label = "Help", menu = helpmenu)

# Body layouts


lb1 = Label(root, text = " Task name ")
lb1.grid(row=1, column=1)

lb1 = Entry(root)
lb1.grid(row=1, column=2)

btn = Button(root, text="Add task")
btn.grid(row=1, column=3)

delete_btn = Button(root, text="Delete")
delete_btn.grid(row=2, column=1)

delete_allbtn = Button(root, text="Delete all")
delete_allbtn.grid(row=2, column=2)

sort_ascbtn = Button(root, text="Sort (ASC)")
sort_ascbtn.grid(row=2, column=2)

sort_descbtn = Button(root, text="Sort (DESC)")
sort_descbtn.grid(row=3, column=2)

delete_allbtn = Button(root, text="Delete all")
delete_allbtn.grid(row=3, column=1)

task_btn = Button(root, text="Number of Tasks")
task_btn.grid(row=3, column=3)

random_btn = Button(root, text="Choose random")
random_btn.grid(row=2, column=3)

todoLists = Listbox(root)
todoLists.grid(row=5, column=2)

root.config(menu = menubar)
root.mainloop()