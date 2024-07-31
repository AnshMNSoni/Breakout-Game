from tkinter import *


def game_on():
    window.destroy()
    import main


window = Tk()
window.title("Breakout Game")
window.config(width=1024, height=1024)


img = PhotoImage(file='breakout.png')
window.label = Label(image=img)
window.label.place(x=0, y=0)


Start_Button = Button(text="Start", command=game_on, font=('Roboto', 28, 'bold'), fg="white", bg="black")
Start_Button.config(bd=10)
Start_Button.place(x=445, y=935)








window.mainloop()