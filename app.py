from flask import Flask, render_template_string, url_for, redirect
import os
import threading
import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry
from PIL import Image, ImageTk
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# HTML and CSS embedded in a single string
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Spotify Playlist</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #008080;
            color: white;
        }

        iframe {
            width: 100%;
            max-width: 300px;
            height: 380px;
            border: none;
        }

        .menu {
            position: fixed;
            top: 10px;
            left: 10px;
            background-color: #333;
            padding: 10px;
            color: white;
            cursor: pointer;
            border-radius: 5px;
        }

        .menu-items {
            display: none;
            flex-direction: column;
            position: fixed;
            top: 50px;
            left: 10px;
            background-color: #555;
            padding: 10px;
            border-radius: 5px;
        }

        .menu:hover + .menu-items,
        .menu-items:hover {
            display: flex;
        }

        .menu-items a {
            color: white;
            text-decoration: none;
            margin-bottom: 10px;
        }

        .menu-items a:hover {
            text-decoration: underline;
        }

    </style>
</head>
<body>
    <div class="menu">☰ Menu</div>
    <div class="menu-items">
        <a href="#" onclick="launchEmulator()">Launch Emulator</a>
    </div>

    <h1>Check out my Spotify Tracks!</h1>

    <div class="tracks-container" id="tracksContainer">
        <div class="track">
            <iframe src="https://open.spotify.com/embed/track/75IN3CtuZwTHTnZvYM4qnJ" allowfullscreen></iframe>
        </div>
    </div>

    <script>
        function launchEmulator() {
            fetch('/start-emulator').then(() => alert("Emulator launched!"));
        }
    </script>
</body>
</html>
"""

# Route to serve the main page
@app.route('/')
def index():
    return render_template_string(html_content)

# Route to start the emulator (Tkinter)
@app.route('/start-emulator')
def start_emulator():
    threading.Thread(target=main).start()  # Run Tkinter app in a separate thread
    return redirect(url_for('index'))

# Your full Tkinter program here
def main():
    global root, score_label, green_box_text, red_box_text

    root = tk.Tk()
    root.title("Click Event App")

    cwd = os.getcwd()  # Get the current working directory (where the script and images are stored)

    # Load images from the current directory
    green_box_image_path = os.path.join(cwd, "Green_Button.png")
    red_box_image_path = os.path.join(cwd, "Red_Button.png")
    button_image_path = os.path.join(cwd, "OIP.jpg")

    # Load images using PIL and resize them
    green_box_image = ImageTk.PhotoImage(Image.open(green_box_image_path).resize((100, 100), Image.LANCZOS))
    red_box_image = ImageTk.PhotoImage(Image.open(red_box_image_path).resize((100, 100), Image.LANCZOS))
    button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((100, 100), Image.LANCZOS))

    # Create GUI elements
    score_label = Label(root, text="Score: 0", font=("Arial", 30))
    score_label.grid(row=0, column=1, padx=10, pady=10)

    green_box_text = Label(root, text="Click to add more score per click\nCost: 10 score", font=("Arial", 12))
    green_box_text.grid(row=1, column=0, padx=10, pady=10)

    red_box_text = Label(root, text="Increment per second: +0 score\nCost: 20 score", font=("Arial", 12))
    red_box_text.grid(row=1, column=2, padx=10, pady=10)

    green_box = Label(root, image=green_box_image, borderwidth=0)
    green_box.grid(row=2, column=0, padx=10, pady=10)
    green_box.bind("<Button-1>", on_green_box_click)

    red_box = Label(root, image=red_box_image, borderwidth=0)
    red_box.grid(row=2, column=2, padx=10, pady=10)
    red_box.bind("<Button-1>", on_red_box_click)

    button = Button(root, image=button_image, command=on_button_click, borderwidth=0)
    button.grid(row=2, column=1, padx=10, pady=10)

    high_scores_button = Button(root, text="High Scores", command=open_high_scores)
    high_scores_button.grid(row=3, column=0, padx=10, pady=10)

    save_score_button = Button(root, text="Save Score", command=open_save_score_window)
    save_score_button.grid(row=3, column=2, padx=10, pady=10)

    initialize_high_scores()
    root.mainloop()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
