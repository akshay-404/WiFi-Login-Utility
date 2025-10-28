import customtkinter as ctk
from backend import login
import sys
import os

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base_path, relative_path)
    
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("LoginLink - WiFi Auto Authenticator")
app.geometry("460x260")
app.resizable(False, False)
icon_path = resource_path("login.ico")
app.iconbitmap(default=icon_path)

exitcode = login()

frame = ctk.CTkFrame(app, corner_radius=20)
frame.pack(padx=20, pady=(20, 20), fill="both", expand=True)

ctk.CTkLabel(
    frame, text="Campus Internet Authenticator",
    font=("Open Sans", 24, "bold"),
    text_color="#e0e0e0"
).pack(pady=(20, 10))

ctk.CTkLabel(
    frame, text="Connecting you to the campus network...",
    font=("Consolas", 14, 'bold'),
    text_color='#b0b0b0'
).pack(pady=(0, 10))

status_box = ctk.CTkFrame(frame, corner_radius=12, fg_color="#202225")
status_box.pack(pady=10, padx=30, fill="x")

color = "green" if exitcode == 1 else "red" if exitcode == -1 else "orange"
text = "Connected successfully!" if exitcode == 1 else "Login failed!" if exitcode == -1 else "Already connected!"

ctk.CTkLabel(
    status_box, text=text,
    font=("Consolas", 16, 'bold'),
    text_color=color
).pack(pady=10)

ctk.CTkLabel(
    frame, text="CustomTkinter UI • Python \U0001F5A4",
    font=("Segoe UI", 9, "italic"),
    text_color="#b0b0b0"
).pack(side="bottom", pady=(20, 15))

app.bind("<Return>", lambda event: app.quit())
app.bind("<Button-1>", lambda event: app.quit())

app.after(2000, lambda: app.destroy())
app.mainloop()