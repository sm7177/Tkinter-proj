from tkinter import *

window=Tk()
window.title("Website")
window.geometry("500x400")

greetings=Label(text="Hello,Welcome to my webpage",fg="white",bg="pink")

button=Button(text="Click me", bg="pink",fg="white", width=50, bd=3)



frame=Frame(master=window, relief=RAISED, borderwidth=5)

label=Label(master=frame, text="Please enter your remarks...")

text=Text(fg="white",bg="pink" ,height="20")



greetings.pack()


frame.pack()
label.pack()
text.pack()
button.pack()



window.mainloop()

