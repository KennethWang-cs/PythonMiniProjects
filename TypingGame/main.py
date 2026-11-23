import tkinter as tk
from game import load_words, get_random_word

# Load words
words = load_words()

# Game variables
score = 0
time_left = 10
elapsed_time = 0
submitted_chars = 0
game_running = False
timer_id = None

# Create the window
root = tk.Tk()
root.title("Typing Game")
root.geometry("500x450")

# Timer selection
duration = tk.StringVar(value="10")

timer_label = tk.Label(
    root,
    text="Time: 10",
    font=("Arial", 16)
)
timer_label.pack(pady=10)

duration_menu = tk.OptionMenu(
    root,
    duration,
    "10",
    "20",
    "30"
)
duration_menu.pack()

# Current word
word_label = tk.Label(
    root,
    text=get_random_word(words),
    font=("Arial", 24)
)
word_label.pack(pady=20)

# Input box
input_box = tk.Entry(root, font=("Arial", 18))
input_box.pack(pady=10)

# Feedback
feedback_label = tk.Label(
    root,
    text="Choose a time and press Start!",
    font=("Arial", 12)
)
feedback_label.pack(pady=5)

# Score
score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 14)
)
score_label.pack(pady=5)

# WPM
wpm_label = tk.Label(
    root,
    text="WPM: 0",
    font=("Arial", 14)
)
wpm_label.pack(pady=5)


# Calculate WPM
def calculate_wpm():
    if elapsed_time == 0:
        return 0

    total_chars = submitted_chars + len(input_box.get())

    wpm = (total_chars / 5) * (60 / elapsed_time)

    return round(wpm)


# Update the WPM display
def update_wpm(event=None):
    if game_running:
        wpm = calculate_wpm()
        wpm_label.config(text=f"WPM: {wpm}")


# Update the timer
def update_timer():
    global time_left, elapsed_time, timer_id

    elapsed_time += 1
    time_left -= 1

    timer_label.config(text=f"Time: {time_left}")

    update_wpm()

    if time_left > 0:
        timer_id = root.after(1000, update_timer)
    else:
        end_game()


# Start the game
def start_game():
    global score, time_left, elapsed_time
    global submitted_chars, game_running

    if game_running:
        return

    score = 0
    time_left = int(duration.get())
    elapsed_time = 0
    submitted_chars = 0
    game_running = True

    score_label.config(text="Score: 0")
    wpm_label.config(text="WPM: 0")
    timer_label.config(text=f"Time: {time_left}")

    feedback_label.config(text="Go!", fg="black")
    word_label.config(text=get_random_word(words))

    input_box.config(state="normal")
    input_box.delete(0, tk.END)
    input_box.focus()

    start_button.config(state="disabled")
    duration_menu.config(state="disabled")

    timer_id = root.after(1000, update_timer)

def start_with_key(event=None):
    if not game_running:
        start_game()
        return "break"

# End the game
def end_game():
    global game_running, timer_id

    game_running = False
    timer_id = None

    input_box.config(state="disabled")
    start_button.config(state="normal")
    duration_menu.config(state="normal")

    final_wpm = calculate_wpm()

    feedback_label.config(
        text=f"Time's up! Final score: {score}",
        fg="blue"
    )

    wpm_label.config(text=f"Final WPM: {final_wpm}")


# Check the player's answer
def check_word(event=None):
    global score, submitted_chars

    if not game_running:
        return

    typed_word = input_box.get()
    current_word = word_label["text"]

    # Count characters from this attempt
    submitted_chars += len(typed_word)

    if typed_word == current_word:
        score += 1

        score_label.config(text=f"Score: {score}")
        feedback_label.config(text="Correct!", fg="green")

        word_label.config(text=get_random_word(words))

    else:
        feedback_label.config(text="Try again!", fg="red")

    input_box.delete(0, tk.END)

    update_wpm()


# Start button
start_button = tk.Button(
    root,
    text="Start Game",
    command=start_game,
    font=("Arial", 14)
)
start_button.pack(pady=10)

# Enter checks the word
input_box.bind("<Return>", check_word)

# Update WPM while typing
input_box.bind("<KeyRelease>", update_wpm)

# Disable typing until game starts
input_box.config(state="disabled")

# Start the game with Space or Enter
root.bind_all("<space>", start_with_key)
root.bind_all("<Return>", start_with_key)

root.mainloop()