import tkinter as tk
from datetime import datetime, timedelta
import pytz
import os
import pygame
import threading
import random

# === Set the path to your music folder ===
MUSIC_FOLDER = "songs"  # Make sure this folder exists in the same directory

# === Initialize pygame for music ===
pygame.init()
pygame.mixer.init()

# === Get Indian time zone ===
india = pytz.timezone('Asia/Kolkata')

# === Play music from folder ===
def play_music():
    if not os.path.isdir(MUSIC_FOLDER):
        print("Music folder not found!")
        return
    songs = [file for file in os.listdir(MUSIC_FOLDER) if file.endswith(('.mp3', '.wav'))]
    if not songs:
        print("No songs found in folder.")
        return
    while True:
        song = random.choice(songs)
        song_path = os.path.join(MUSIC_FOLDER, song)
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

# === Timer functionality ===
def start_timer(duration):
    end_time = datetime.now() + timedelta(seconds=duration)
    while datetime.now() < end_time:
        pass  # Just wait
    pygame.mixer.music.stop()

# === GUI setup ===
def main():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')
    
    time_label = tk.Label(root, text="", font=('Courier', 48), fg='white', bg='black')
    time_label.pack(expand=True)

    # Update time every 100 ms
    def update_time():
        now = datetime.now(india)
        formatted_time = now.strftime("%H:%M:%S") + f":{now.microsecond // 1000:03}"
        time_label.config(text=formatted_time)
        root.after(100, update_time)

    # Ask user for timer duration in seconds
    def ask_timer():
        def start():
            try:
                seconds = int(entry.get())
                entry_frame.destroy()
                threading.Thread(target=start_timer, args=(seconds,), daemon=True).start()
                threading.Thread(target=play_music, daemon=True).start()
            except ValueError:
                pass

        entry_frame = tk.Frame(root, bg='black')
        entry_frame.pack()
        tk.Label(entry_frame, text="Enter timer (seconds):", fg='white', bg='black', font=('Courier', 24)).pack()
        entry = tk.Entry(entry_frame, font=('Courier', 24))
        entry.pack()
        tk.Button(entry_frame, text="Start", font=('Courier', 18), command=start).pack()

    update_time()
    ask_timer()
    root.mainloop()

if __name__ == "__main__":
    main()
