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
            box-sizing: border-box; /* Ensure padding and border are included in the width */
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
            justify-content: center; /* Center align the tracks */
        }

        .track {
            flex: 1 1 calc(33.333% - 20px); /* 3 items per row on larger screens */
            box-sizing: border-box;
            max-width: 300px; /* Max width for each track box */
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

        /* Responsive Design for Mobile Devices */
        @media (max-width: 768px) {
            .track {
                flex: 1 1 calc(50% - 20px); /* 2 items per row on medium screens */
            }
        }

        @media (max-width: 480px) {
            .track {
                flex: 1 1 100%; /* 1 item per row on small screens */
            }
        }
    </style>
</head>
<body>
    <h1>Check out my Spotify Tracks and Playlists! oh and btw Yes this is Antons website Whatever you do DO NOT CLICK THE RELOAD SERVER OR IT WILL CRASH THE SERVER</h1>

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

        <div class="track" data-title="gegage">
            <iframe src="https://open.spotify.com/embed/track/7LnI49wTeiBIwaCJjc07vS" allowfullscreen></iframe>
        </div>

        <div class="track" data-title="Wii shop channel">
            <iframe src="https://open.spotify.com/embed/track/6d031ugbPZHSYTsY2sTDJT" allowfullscreen></iframe>
        </div>

        <div class="track" data-title="All star">
            <iframe src="https://open.spotify.com/embed/track/3cfOd4CMv2snFaKAnMdnvK" allowfullscreen></iframe>
        </div>

        <div class="track" data-title="Gangstas paradise">
            <iframe src="https://open.spotify.com/embed/track/1DIXPcTDzTj8ZMHt3PDt8p" allowfullscreen></iframe>
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
