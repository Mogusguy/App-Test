from flask import Flask, render_template_string, redirect, url_for

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
            position: relative;
        }

        iframe {
            width: 100%;
            max-width: 300px;
            height: 380px;
            border: none;
        }

        .search-container {
            margin-bottom: 20px;
        }

        .search-container input[type="text"] {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            box-sizing: border-box;
        }

        .tracks-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: space-between;
        }

        .track {
            flex: 1 1 calc(33.333% - 20px);
            box-sizing: border-box;
        }

        h1 {
            color: white;
            text-align: center;
        }

        .restart-button, .menu-button, .close-emulator {
            position: absolute;
            background-color: red;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .menu-button {
            top: 10px;
            left: 10px;
        }

        .restart-button {
            top: 10px;
            right: 10px;
        }

        .emulator-container {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: white;
            color: black;
            z-index: 1000;
            padding: 20px;
            box-sizing: border-box;
        }

        .emulator-container iframe {
            height: calc(100% - 50px);
        }

        .emulator-container .close-emulator {
            top: 10px;
            right: 10px;
        }
    </style>
</head>
<body>
    <h1>Check out my Spotify Tracks and Playlists!</h1>

    <!-- Menu Button -->
    <button class="menu-button" onclick="toggleMenu()">Menu</button>

    <!-- Reload Button -->
    <form action="/reload" method="post" style="display: inline;">
        <button class="restart-button" type="submit">Reload Server</button>
    </form>
    
    <!-- Sidebar Menu -->
    <div id="sidebar" style="display: none;">
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/emulator">Open Emulator</a></li>
            <!-- Add other menu items here -->
        </ul>
    </div>

    <!-- Emulator Container -->
    <div id="emulatorContainer" class="emulator-container">
        <button class="close-emulator" onclick="closeEmulator()">Close Emulator</button>
        <iframe src="https://example.com/emulator" allowfullscreen></iframe>
    </div>

    <div class="search-container">
        <input type="text" id="searchInput" placeholder="Search for songs..." oninput="filterTracks()">
    </div>

    <!-- Tracks -->
    <div class="tracks-container" id="tracksContainer">
        <!-- Your Spotify tracks here -->
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

        function toggleMenu() {
            const sidebar = document.getElementById('sidebar');
            sidebar.style.display = sidebar.style.display === 'none' ? 'block' : 'none';
        }

        function openEmulator() {
            document.getElementById('emulatorContainer').style.display = 'block';
        }

        function closeEmulator() {
            document.getElementById('emulatorContainer').style.display = 'none';
        }
    </script>
</body>
</html>
"""

# Main page route
@app.route('/')
def index():
    return render_template_string(html_content)

# Reload page route
@app.route('/reload', methods=['POST'])
def reload():
    return redirect(url_for('index'))

# Emulator page route
@app.route('/emulator')
def emulator():
    emulator_html = """
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
                padding: 0;
                background-color: #f0f0f0;
                color: #333;
            }

            .emulator-container {
                position: relative;
                width: 100%;
                height: 100vh;
                padding: 20px;
                box-sizing: border-box;
            }

            .close-emulator {
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

            iframe {
                width: 100%;
                height: calc(100% - 50px);
                border: none;
            }
        </style>
    </head>
    <body>
        <button class="close-emulator" onclick="window.location.href='/'">Close Emulator</button>
        <!-- Embed your emulator here -->
        <iframe src="https://example.com/emulator" allowfullscreen></iframe>
    </body>
    </html>
    """
    return render_template_string(emulator_html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
