import tkinter as tk
from tkinter import ttk
import time
import winsound

def remind():
    goal_liters = float(goal_entry.get())
    interval_hours = float(interval_entry.get())
    total_liters = 0
    
    while total_liters < goal_liters:
        reminder_label.config(text="Remember to drink water!", fg="blue")
        update_progress(total_liters / goal_liters)
        winsound.Beep(1000, 500)  # Play a beep sound as a reminder
        time.sleep(interval_hours * 3600)  # Convert hours to seconds
        ml_drunk = float(ml_entry.get())
        total_liters += ml_drunk / 1000  # Convert milliliters to liters
    
    reminder_label.config(text="Congratulations! You've met your hydration goal for the day!", fg="green")
    update_progress(1.0)

def update_progress(percentage):
    progress_bar["value"] = percentage * 100

# Create GUI window
window = tk.Tk()
window.title("Hydration Notifier")
window.geometry("300x250")

# Labels
goal_label = tk.Label(window, text="Enter daily water intake goal (liters):")
goal_label.pack()
goal_entry = tk.Entry(window)
goal_entry.pack()

interval_label = tk.Label(window, text="Enter reminder interval (hours):")
interval_label.pack()
interval_entry = tk.Entry(window)
interval_entry.pack()

ml_label = tk.Label(window, text="How many milliliters of water did you drink?")
ml_label.pack()
ml_entry = tk.Entry(window)
ml_entry.pack()

reminder_label = tk.Label(window, text="")
reminder_label.pack()

# Progress Bar
progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
progress_bar.pack()

# Button
start_button = tk.Button(window, text="Start Notifier", command=remind)
start_button.pack()

# Run GUI
window.mainloop()
