from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk

def buttonpress():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("Here's what you typed", entrytxt)

def addtolist():
    entrytxt = entry1.get()
    if checklist() == False:
        listbox1.insert(END, entrytxt)
        findsize()
    entry1.delete(0, END)
    
def addtolist2(event):
    entrytxt = entry1.get()
    if checklist() == False:
        listbox1.insert(END, entrytxt)
        findsize()
    entry1.delete(0, END)
    
def clearlist(event):
    listbox1.delete(0, END)
    findsize()

def clearlist2():
    listbox1.delete(0, END)
    findsize()

def checklist():
    name = listbox1.get(0, END)
    if entry1.get() in name:
        return True
    else:
        return False

def findsize():
    label1.config(text=listbox1.size())

def openfileR():
    clearlist2()
    f = open("README.txt", 'r')
    for line in f:
        name = line[0:-1]
        listbox1.insert(END, name)
    f.close()
    findsize()
    
def openfileW():
    f = open("README.txt", 'w')
    names = listbox1.get(0, END)
    for i in names:
        f.write(i+"\n")
        
    f.close()

root = Tk() #gives us a blank canvas object to work with
root.title = ("My first jungleboys purchase")

button1 = Button(root, text="Button", command=checklist, anchor=W)
button1.grid(row=1, column=1, sticky=W)

entry1 = Entry(root)
entry1.grid(row=1, column=0)
entry1.bind("<Return>", addtolist2)

label1 = Label(root, text="cookies", bg="pink", anchor=W)
label1.grid(row=0, column=0, sticky=EW, columnspan=2)

label1 = Label(root, text="jungleboys", bg="pink", anchor=W)
label1.grid(row=0, column=0, sticky=EW, columnspan=2)

scrollbar = Scrollbar(root, orient=VERTICAL)
listbox1 = Listbox(root, yscrollcommand=scrollbar.set)
listbox1.config(command=listbox1.yview)
scrollbar.grid(row=1, column=10, rowspan=11)
listbox1.grid(row=2, column=0, columnspan=2, sticky=EW, rowspan=10)
listbox1.bind("<Button-3>", clearlist)

#listbox1.insert(END, "purple punch")
#listbox1.insert(END, "berners cookies")
#listbox1.insert(END, "sherbert gelato")

findsize()

image = Image.open("Documents\Tkinter\jb.png")
image = image.resize((250, 166))
photo = ImageTk.PhotoImage(image)

label2 = Label(image=photo)
label2.image = photo # keep a reference!
label2.grid(row=3, column=1, rowspan=10)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="open", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="save", command=openfileW)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)


mainloop() #causes the windows to display on the screen until program closes