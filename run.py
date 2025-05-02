from tkinter import *
import os

def game_on():
    window.destroy()
    import main

def show_instructions():
    instructions = Toplevel(window)
    instructions.title("How to Play")
    instructions.config(bg="black")
    instructions.geometry("700x400")
    
    Label(instructions, text="HOW TO PLAY", font=('Roboto', 20, 'bold'), fg="white", bg="black").pack(pady=10)
    
    instruction_text = """
    • Use LEFT and RIGHT arrow keys to move the paddle
    • Break all the bricks to win
    • You have 3 lives
    • Press 'P' to pause the game
    • Press SPACE to resume
    
    Brick Points:
    • Top rows: 30 points
    • Middle rows: 20 points
    • Bottom rows: 10 points
    
    Good luck!
    """
    
    Label(instructions, text=instruction_text, font=('Courier', 14), fg="white", bg="black", justify=LEFT).pack(pady=20)
    
    Button(instructions, text="Close", command=instructions.destroy, font=('Roboto', 14), 
           fg="white", bg="black", bd=5).pack(pady=10)

# Create main window
window = Tk()
window.title("Breakout Game")
window.config(width=1024, height=1024, bg="black")
window.geometry("1000x700")

# Check if image file exists
if os.path.exists('breakout.png'):
    img = PhotoImage(file='breakout.png')
    window.label = Label(image=img)
    window.label.place(x=0, y=0)
else:
    # Create a title if image is not available
    title_label = Label(text="BREAKOUT", font=('Roboto', 50, 'bold'), fg="white", bg="black")
    title_label.pack(pady=100)
    
    subtitle = Label(text="Classic Arcade Game", font=('Roboto', 20), fg="white", bg="black")
    subtitle.pack(pady=20)

# Create buttons
button_frame = Frame(window, bg="black")
button_frame.pack(pady=50)

Start_Button = Button(button_frame, text="Start Game", command=game_on, 
                     font=('Roboto', 20, 'bold'), fg="white", bg="black")
Start_Button.config(bd=5, padx=20, pady=10)
Start_Button.pack(pady=20)

Instructions_Button = Button(button_frame, text="Instructions", command=show_instructions,
                           font=('Roboto', 16), fg="white", bg="black")
Instructions_Button.config(bd=5, padx=10, pady=5)
Instructions_Button.pack(pady=10)

Quit_Button = Button(button_frame, text="Quit", command=window.destroy,
                    font=('Roboto', 16), fg="white", bg="black")
Quit_Button.config(bd=5, padx=10, pady=5)
Quit_Button.pack(pady=10)

# Credits
credits = Label(window, text="Created by ansh.mn.soni", font=('Courier', 10), fg="white", bg="black")
credits.pack(side=BOTTOM, pady=20)

window.mainloop()