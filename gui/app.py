import tkinter as tk
from tkinter import messagebox
import sys
import os
from threading import Thread
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gui.components import StatusLabel, PositionLabel

class AutoClickerApp:
    def __init__(self, clicker):
        self.clicker = clicker
        self.root = tk.Tk()
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        self.root.title("AutoClicker with GUI")
        self.root.geometry("300x300")

    def create_widgets(self):
        self.status_label = StatusLabel(
            self.root, 
            text="Autoclicker is OFF", 
            fg="red", 
            font=("Arial", 14)
        )
        self.status_label.pack(pady=20)

        toggle_button = tk.Button(
            self.root,
            text="Toggle Autoclicker",
            command=self.toggle_autoclicker,
            font=("Arial", 12)
        )
        toggle_button.pack(pady=5)

        speed_label = tk.Label(
            self.root,
            text="Click Speed (seconds):",
            font=("Arial", 10)
        )
        speed_label.pack(pady=5)

        self.speed_entry = tk.Entry(self.root, font=("Arial", 10))
        self.speed_entry.insert(0, str(self.clicker.click_speed))
        self.speed_entry.pack(pady=5)

        update_button = tk.Button(
            self.root,
            text="Update Speed",
            command=self.update_speed,
            font=("Arial", 12)
        )
        update_button.pack(pady=5)

        
        self.position_label = PositionLabel(
            self.root,
            text="Random Click Position: OFF",
            fg="red",
            font=("Arial", 10)
        )
        self.position_label.pack(pady=5)

        random_position_button = tk.Button(
            self.root,
            text="Toggle Random Position",
            command=self.toggle_random_position,
            font=("Arial", 12)
        )
        random_position_button.pack(pady=5)

        stop_button = tk.Button(
            self.root,
            text="Stop Autoclicker",
            command=self.stop_autoclicker,
            font=("Arial", 12)
        )
        stop_button.pack(pady=10)

    def toggle_autoclicker(self):
        is_on = self.clicker.toggle()
        self.status_label.update_status(is_on)

    def update_speed(self):
        try:
            new_speed = float(self.speed_entry.get())
            self.clicker.set_speed(new_speed)
            messagebox.showinfo(
                "Click Speed Updated", 
                f"Click speed set to {new_speed} seconds per click."
            )
        except ValueError:
            messagebox.showerror(
                "Invalid Input", 
                "Please enter a valid number for the click speed."
            )

    def toggle_random_position(self):
        self.clicker.set_random_position(not self.clicker.random_position)
        self.position_label.update_status(self.clicker.random_position)

    def stop_autoclicker(self):
        self.clicker.stop()
        self.status_label.update_status(False)