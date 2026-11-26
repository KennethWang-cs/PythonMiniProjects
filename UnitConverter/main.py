import tkinter as tk
from tkinter import messagebox


def convert_feet_to_meters():
	try:
		feet = float(feet_entry.get())
	except ValueError:
		messagebox.showerror("Invalid input", "Enter a valid number of feet.")
		return

	meters = feet * 0.3048
	result_label.config(text=f"{feet:g} feet = {meters:.4f} meters")


root = tk.Tk()
root.title("Feet to Meters Converter")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Feet:").grid(row=0, column=0, padx=(0, 8), pady=8)
feet_entry = tk.Entry(frame, width=18)
feet_entry.grid(row=0, column=1, pady=8)
feet_entry.focus()

tk.Button(frame, text="Convert to meters", command=convert_feet_to_meters).grid(
	row=1, column=0, columnspan=2, pady=8
)

result_label = tk.Label(frame, text="Enter a value to convert.")
result_label.grid(row=2, column=0, columnspan=2, pady=(8, 0))

root.bind("<Return>", lambda event: convert_feet_to_meters())
root.mainloop()
