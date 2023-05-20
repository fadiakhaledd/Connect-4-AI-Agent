import tkinter as tk
from tkinter import ttk
import game

# Create a new tkinter window
game_window = tk.Tk()

# Set the window title and icon
game_window.title("Connect 4 Game")

# Set the window size and disable resizing
game_window.geometry("500x400")
game_window.resizable(False, False)

bg_image = tk.PhotoImage(file="background.png")
bg_label = tk.Label(game_window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add a label to the window
label = tk.Label(game_window, text="Welcome to Connect 4!",
                 fg="#4169e1", font=("Arial", 24, "bold"))
label.pack(pady=35)

# Add the first dropdown list title to the window
algo_choice = tk.Label(
    game_window, text="Choose Algorithm:", font=("Helvetica", 16))
algo_choice.pack()

# Add the first dropdown list to the window
algo_options = ["Minimax", "Alpha-Beta Pruning"]
default_algo = tk.StringVar()
default_algo.set(algo_options[0])
dropdown_algo = ttk.Combobox(game_window, values=algo_options, textvariable=default_algo, font=("Helvetica", 13),
                             state="readonly")
dropdown_algo.pack(pady=10)

# Add the second dropdown list title to the window
difficulty_choice = tk.Label(
    game_window, text="Choose Difficulty Level:", font=("Helvetica", 16))
difficulty_choice.pack()

# Add the second dropdown list to the window
difficulty_options = ["Easy", "Medium", "Hard"]
default_difficulty = tk.StringVar()
default_difficulty.set(difficulty_options[0])
dropdown_difficulty = ttk.Combobox(game_window, values=difficulty_options, textvariable=default_difficulty,
                                   font=("Helvetica", 13), state="readonly")
dropdown_difficulty.pack(pady=10)


# Define the function to be called when the button is clicked
def on_start_game():
    algorithm = dropdown_algo.get()
    levels = {"Easy": 3, "Medium": 4, "Hard": 6}
    difficulty = levels[dropdown_difficulty.get()]
    game_window.destroy()
    game.play(algorithm, difficulty)


# Add the button to the window
button = tk.Button(game_window, text="Start Game", bg="#0b36f6", fg="#ffffff",
                   font=("Helvetica", 14), command=on_start_game)
button.pack(pady=30)

# Start the main tkinter event loop
game_window.mainloop()
