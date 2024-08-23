import tkinter as tk
from PIL import Image, ImageTk
import random
from Score import Score

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

def load_images():
    images = {
        'rock-user': ImageTk.PhotoImage(Image.open(r"D:\Encryptix\Encryptix\rockpaperScissor\images\rock-user.png")),
        'rock-comp': ImageTk.PhotoImage(Image.open(r"D:\Encryptix\Encryptix\rockpaperScissor\images\rock-comp.png")),
        'scissors-user': ImageTk.PhotoImage(Image.open(r"D:\Encryptix\Encryptix\rockpaperScissor\images\scissors-user.png")),
        'scissors-comp': ImageTk.PhotoImage(Image.open(r"D:\Encryptix\Encryptix\rockpaperScissor\images\scissors-comp.png")),
        'paper-user': ImageTk.PhotoImage(Image.open(r"D:\Encryptix\Encryptix\rockpaperScissor\images\paper-user.png")),
        'paper-comp': ImageTk.PhotoImage(Image.open(r"D:\Encryptix\Encryptix\rockpaperScissor\images\paper-comp.png"))
    }
    return images

 

images = load_images()

score = Score()

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!"
    else:
        return "You lose!"

def play(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    score.update_score(result)
    user_score, computer_score = score.get_scores()

    user_image_label.config(image=images[f'{user_choice.lower()}-user'])
    comp_image_label.config(image=images[f'{computer_choice.lower()}-comp'])

    result_label.config(text=f"{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global score
    score = Score()  
    result_label.config(text="New Game! Choose Rock, Paper, or Scissors.")
    score_label.config(text="Score - You: 0 | Computer: 0")
    user_image_label.config(image='')
    comp_image_label.config(image='')

user_image_label = tk.Label(root)
user_image_label.pack(side="left", padx=20, pady=20)

comp_image_label = tk.Label(root)
comp_image_label.pack(side="right", padx=20, pady=20)

rock_button = tk.Button(root, text="Rock", command=lambda: play('Rock'))
paper_button = tk.Button(root, text="Paper", command=lambda: play('Paper'))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play('Scissors'))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors to start.")
result_label.pack()

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0")
score_label.pack()

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack()

root.mainloop()
