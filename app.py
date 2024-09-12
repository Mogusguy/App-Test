from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

# HTML and CSS embedded in a single string
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Spotify Playlist and Emulator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #008080;
            color: white;
        }

        h1, h2 {
            text-align: center;
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

        .tracks-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: space-around;
            margin-top: 20px;
        }

        .track {
            text-align: center;
            flex: 1 1 calc(33.333% - 20px);
            box-sizing: border-box;
        }

        .track-title {
            margin-top: 10px;
            font-size: 18px;
            color: white;
        }

        .restart-button {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: red;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="menu">☰ Menu</div>
    <div class="menu-items">
        <a href="#" onclick="launchEmulator()">Launch Emulator</a>
    </div>

    <h1>Check out my Spotify Tracks and Playlists!</h1>
    <h2>Enjoy Some Music While You Play</h2>

    <!-- Reload Button -->
    <form action="/reload" method="post">
        <button class="restart-button" type="submit">Reload Server</button>
    </form>

    <div class="search-container">
        <input type="text" id="searchInput" placeholder="Search for songs..." oninput="filterTracks()">
    </div>

    <!-- Tracks -->
    <div class="tracks-container" id="tracksContainer">
        <div class="track" data-title="My Name Is">
            <iframe src="https://open.spotify.com/embed/track/75IN3CtuZwTHTnZvYM4qnJ" allowfullscreen></iframe>
            <div class="track-title">My Name Is - Eminem</div>
        </div>

        <div class="track" data-title="The Real Slim Shady">
            <iframe src="https://open.spotify.com/embed/track/3yfqSUWxFvZELEM4PmlwIR" allowfullscreen></iframe>
            <div class="track-title">The Real Slim Shady - Eminem</div>
        </div>

        <div class="track" data-title="Double Life">
            <iframe src="https://open.spotify.com/embed/track/07oO1U722crtVcavi6frX6" allowfullscreen></iframe>
            <div class="track-title">Double Life - Unknown Artist</div>
        </div>

        <div class="track" data-title="gegage">
            <iframe src="https://open.spotify.com/embed/track/7LnI49wTeiBIwaCJjc07vS" allowfullscreen></iframe>
            <div class="track-title">gegage - Unknown Artist</div>
        </div>

        <div class="track" data-title="Wii Shop Channel">
            <iframe src="https://open.spotify.com/embed/track/6d031ugbPZHSYTsY2sTDJT" allowfullscreen></iframe>
            <div class="track-title">Wii Shop Channel - Unknown Artist</div>
        </div>

        <div class="track" data-title="All Star">
            <iframe src="https://open.spotify.com/embed/track/3cfOd4CMv2snFaKAnMdnvK" allowfullscreen></iframe>
            <div class="track-title">All Star - Smash Mouth</div>
        </div>

        <div class="track" data-title="Gangsta's Paradise">
            <iframe src="https://open.spotify.com/embed/track/1DIXPcTDzTj8ZMHt3PDt8p" allowfullscreen></iframe>
            <div class="track-title">Gangsta's Paradise - Coolio</div>
        </div>
    </div>

    <script>
        function filterTracks() {
            const searchInput = document.getElementById('searchInput').value.toLowerCase();
            const tracks = document.querySelectorAll('.track');

            tracks.forEach(track => {
                const title = track.getAttribute('data-title').toLowerCase();
                if (title.includes(searchInput)) {
                    track.style.display = 'block';
                } else {
                    track.style.display = 'none';
                }
            });
        }

        function launchEmulator() {
            window.open('/emulator', '_blank');
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_content)

@app.route('/reload', methods=['POST'])
def reload():
    # Reload the page (client-side action)
    return redirect(url_for('index'))

@app.route('/emulator')
def emulator():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Emulator</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background-color: #f0f0f0;
                }
                .emulator-container {
                    width: 100%;
                    max-width: 800px;
                    margin: 0 auto;
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                .close-button {
                    background-color: red;
                    color: white;
                    border: none;
                    padding: 10px;
                    border-radius: 5px;
                    cursor: pointer;
                    float: right;
                }
                .emulator-content {
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <div class="emulator-container">
                <button class="close-button" onclick="window.close()">Close Emulator</button>
                <div class="import os
import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry
from PIL import Image, ImageTk
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Global variables for game parameters
score = 0
initial_green_score_increment = 1
initial_green_box_cost = 10
initial_red_box_base_cost = 20
initial_red_box_increment_per_purchase = 1
initial_red_box_increment_per_second = 1
green_score_increment = initial_green_score_increment
green_box_cost = initial_green_box_cost
red_boxes = []
red_box_base_cost = initial_red_box_base_cost
red_box_increment_per_purchase = initial_red_box_increment_per_purchase
red_box_increment_per_second = initial_red_box_increment_per_second
red_box_active = False
red_box_increment_running = False
high_scores = []

# Google Sheets setup
def connect_to_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Get the current working directory
    cwd = os.getcwd()
    
    # Construct the full file path for the JSON key file
    key_file = "southern-list-427519-i3-7eb54cc55407.json"
    key_path = os.path.join(cwd, key_file)
    
    # If the environment variable is set, use its value
    env_key_path = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    if env_key_path:
        key_path = env_key_path

    creds = ServiceAccountCredentials.from_json_keyfile_name(key_path, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key("1A1uHm9iCPH_bPJWZRlxzh9wdgFdyzU2paw9f-Hu0c6A").sheet1
    return sheet

def update_high_scores():
    sheet = connect_to_google_sheets()
    sheet.clear()  # Clear existing high scores in the sheet
    header = ['Player', 'Score']  # Header labels
    sheet.insert_row(header, 1)  # Insert header at first row
    for idx, (player, score) in enumerate(high_scores):
        sheet.insert_row([player, score], idx + 2)  # Insert data starting from row 2, column A

def open_high_scores():
    high_scores_window = Toplevel(root)
    high_scores_window.title("High Scores")
    header_label = Label(high_scores_window, text="High Scores", font=("Arial", 20))
    header_label.pack(padx=20, pady=20)
    for idx, (player, score) in enumerate(high_scores, start=1):
        score_label = Label(high_scores_window, text=f"{idx}. {player}: {score}", font=("Arial", 14))
        score_label.pack()

def open_save_score_window():
    save_score_window = Toplevel(root)
    save_score_window.title("Save Score")
    username_label = Label(save_score_window, text="Enter your username:")
    username_label.pack(padx=20, pady=10)
    username_entry = Entry(save_score_window)
    username_entry.pack(padx=20, pady=5)

    def save_score():
        global score, green_score_increment, green_box_cost, red_box_base_cost, red_box_increment_per_second, red_box_increment_running
        username = username_entry.get()
        if username:
            existing_index = None
            for idx, (existing_player, existing_score) in enumerate(high_scores):
                if existing_player == username:
                    existing_index = idx
                    break
            if existing_index is not None:
                if score > high_scores[existing_index][1]:
                    high_scores[existing_index] = (username, score)
            else:
                high_scores.append((username, score))
            high_scores.sort(key=lambda x: x[1], reverse=True)
            update_high_scores()
            open_high_scores()
            score = 0
            green_score_increment = initial_green_score_increment
            green_box_cost = initial_green_box_cost
            red_box_base_cost = initial_red_box_base_cost
            red_box_increment_per_second = initial_red_box_increment_per_second
            red_box_increment_running = False
            update_score_display()
            save_score_window.destroy()

    save_button = Button(save_score_window, text="Save", command=save_score)
    save_button.pack(padx=20, pady=10)

def on_green_box_click(event):
    global score, green_score_increment, green_box_cost
    if score >= green_box_cost:
        score -= green_box_cost
        green_score_increment += 1
        green_box_cost = int(green_box_cost * 1.5)
        update_score_display()

def on_red_box_click(event):
    global score, red_box_base_cost, red_boxes, red_box_active
    if score >= red_box_base_cost:
        score -= red_box_base_cost
        # Calculate the new cost for the next red box
        red_box_cost = int(red_box_base_cost * (1.6 ** len(red_boxes)))
        red_boxes.append({
            'cost': red_box_cost,
            'last_update_time': int(time.time()),
            'increment_per_purchase': red_box_increment_per_purchase,
            'click_increase': 1
        })
        # Update the base cost for the next purchase
        red_box_base_cost = red_box_cost
        start_red_box_incrementing()
        update_score_display()

def start_red_box_incrementing():
    global red_box_active, red_box_increment_running
    if not red_box_active:
        red_box_active = True
        red_box_increment_running = True
        increment_red_score()

def increment_red_score():
    global score, red_boxes, red_box_increment_per_second, red_box_increment_running
    if red_box_increment_running:
        current_time = int(time.time())
        total_increment = 0
        for box in red_boxes:
            time_diff = current_time - box['last_update_time']
            if time_diff >= 1:
                increments_per_second = box['increment_per_purchase'] * red_box_increment_per_second
                total_increment += increments_per_second
                box['last_update_time'] = current_time
        score += total_increment
        update_score_display()
        score_label.after(1000, increment_red_score)

def update_score_display():
    score_label.config(text=f"Score: {score}", font=("Arial", 30))
    green_box_text.config(text=f"Click to add more score per click\nCost: {green_box_cost} score", font=("Arial", 12))
    if red_boxes:
        total_increment_per_second = sum(
            box['increment_per_purchase'] * red_box_increment_per_second for box in red_boxes)
        red_box_cost = red_box_base_cost  # This should reflect the updated cost
        red_box_text.config(
            text=f"Increment per second: +{total_increment_per_second} score\nCost: {red_box_cost} score",
            font=("Arial", 12))

def on_button_click():
    global score
    score += green_score_increment
    update_score_display()

def initialize_high_scores():
    global high_scores
    sheet = connect_to_google_sheets()
    if sheet:
        try:
            records = sheet.get_all_records()
            print(f"Fetched records: {records}")  # Debug: print fetched records
            high_scores = [(record['Player'], int(record['Score'])) for record in records]
            print(f"Initialized high scores: {high_scores}")  # Debug: print initialized high scores
        except Exception as e:
            print(f"Failed to initialize high scores from Google Sheets: {str(e)}")

def main():
    global root, score_label, green_box_text, red_box_text

    root = tk.Tk()
    root.title("Click Event App")

    # Get the current working directory
    cwd = os.getcwd()

    # Construct the full file paths for the images
    green_box_image_path = os.path.join(cwd, "Green_Button.png")
    red_box_image_path = os.path.join(cwd, "Red_Button.png")
    button_image_path = os.path.join(cwd, "OIP.jpg")

    # Load textures (ensure the images are resized to 100x100 pixels)
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
    green_box.bind("<Button-1>", on_green_box_click)  # Bind click event

    red_box = Label(root, image=red_box_image, borderwidth=0)
    red_box.grid(row=2, column=2, padx=10, pady=10)
    red_box.bind("<Button-1>", on_red_box_click)  # Bind click event

    button = Button(root, image=button_image, command=on_button_click, borderwidth=0)
    button.grid(row=2, column=1, padx=10, pady=10)

    high_scores_button = Button(root, text="High Scores", command=open_high_scores)
    high_scores_button.grid(row=3, column=0, padx=10, pady=10)

    save_score_button = Button(root, text="Save Score", command=open_save_score_window)
    save_score_button.grid(row=3, column=2, padx=10, pady=10)

    initialize_high_scores()  # Initialize high scores from Google Sheets

    root.mainloop()

if __name__ == "__main__":
    main()
">
                    <!-- Insert your emulator content here -->
                    <h1>Emulator</h1>
                    <p>This is where your emulator will be displayed.</p>
                    <!-- For example, if you have an actual iframe or embedded emulator, insert it here -->
                </div>
            </div>
        </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
