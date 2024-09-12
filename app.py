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
    <h1>Check out my Spotify Tracks and Playlists!</h1>

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
        </div>

        <div class="track" data-title="The Real Slim Shady">
            <iframe src="https://open.spotify.com/embed/track/3yfqSUWxFvZELEM4PmlwIR" allowfullscreen></iframe>
        </div>

        <div class="track" data-title="Double life">
            <iframe src="https://open.spotify.com/embed/track/07oO1U722crtVcavi6frX6" allowfullscreen></iframe>
        </div>

        <div class="track" data-title="Test 1">
            <iframe src="https://open.spotify.com/embed/track/6jJ0s89eD6GaHleKKya26X" allowfullscreen></iframe>
        </div>

        <div class="track" data-title="Test 2">
            <iframe src="https://open.spotify.com/embed/track/1xznGGDReH1oQq0xzbwXa3" allowfullscreen></iframe>
        </div>

        <div class="track" data-title="Test 4">
            <iframe src="https://open.spotify.com/embed/track/4VqPOruhp5EdPBeR92t6lQ" allowfullscreen></iframe>
        </div>

        <div class="track" data-title="Test 4">
            <iframe src="https://open.spotify.com/embed/track/4VqPOruhp5EdPBeR92t6lQ" allowfullscreen></iframe>
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
