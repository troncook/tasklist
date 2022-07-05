import tkinter as tk
from datetime import datetime
#1
now = datetime.now()
print ("Current date and time : ")
print (now.strftime("employee-attendance-list-%Y-%m-%d.txt"))

filename = datetime.now().strftime('employee-attendance-list-%Y-%m-%d.txt')


root = tk.Tk()
root.title("List App")
root.geometry("400x400")

def handler(e):
   label= Label(win, text= "You Pressed Enter")
   label.pack()
    
def retrievedata():
    ''' get data stored '''
    global list_data
    list_data = []
    try:
      with open (filename, "r", encoding="utf-8") as file:
       for f in file:
        listbox.insert(tk.END, f.strip())
        list_data.append(f.strip())
        print(list_data)
    except:
        pass

def reload_data():
    listbox.delete(0, tk.END)
    for d in list_data:
        listbox.insert(0, d)


def add_item(event=1):
    global list_data
    if content.get() != "":
        listbox.insert(tk.END, content.get())
        list_data.append(content.get())
        content.set("")


def delete():
    global list_data
    listbox.delete(0, tk.END)
    list_data = []


def delete_selected():

    try:
        selected = listbox.get(listbox.curselection())
        listbox.delete(listbox.curselection())
        list_data.pop(list_data.index(selected))
        # reload_data()
        # # listbox.selection_clear(0, END)
        listbox.selection_set(0)
        listbox.activate(0)
        listbox.event_generate("&lt;&lt;ListboxSelect>>")
        print(listbox.curselection())
    except:
        pass



def quit():
 global root
 with open (filename, "w", encoding="utf-8") as file:
  for d in list_data:
   file.write(d + "\n")
 root.destroy()

# LISTBOX

content = tk.StringVar()
entry = tk.Entry(root, textvariable=content)
entry.pack()

button = tk.Button(root, text="Add Item", command=add_item)
button.pack()
entry.bind("<Return>", add_item)

button_delete = tk.Button(text="Delete", command=delete)
button_delete.pack()

button_delete_selected = tk.Button(text="Delete Selected", command=delete_selected)
button_delete_selected.pack()

listbox = tk.Listbox(root)
listbox.pack()
entry.bind("<Return>,", add_item)

bquit = tk.Button(root, text="Quit and save", command=quit)
bquit.pack()

retrievedata()
root.mainloop()