import tkinter as tk
from tkinter import messagebox

class StatusLabel(tk.Label):
    def update_status(self, is_on):
        self.config(
            text=f"Autoclicker is {'ON' if is_on else 'OFF'}", 
            fg="green" if is_on else "red"
        )

class PositionLabel(tk.Label):
    def update_status(self, is_random):
        self.config(
            text=f"Random Click Position: {'ON' if is_random else 'OFF'}", 
            fg="green" if is_random else "red"
        )