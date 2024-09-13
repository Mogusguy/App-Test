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
            margin: 0;
            background-color: #008080;
            color: white;
        }

        h1, h2 {
            text-align: center;
            margin-top: 20px;
        }

        iframe {
            width: 100%;
            max-width: 300px;
            height: 380px;
            border: none;
        }

        .restart-button {
            display: block;
            width: 100%;
            max-width: 200px;
            margin: 20px auto;
            background-color: red;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-align: center;
        }

        .tracks-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
            margin-top: 20px;
        }

        .track {
            text-align: center;
            flex: 1 1 calc(100% - 40px);
            max-width: 300px;
            box-sizing: border-box;
        }

        .track-title {
            margin-top: 10px;
            font-size: 16px;
            color: white;
        }
    </style>
</head>
<body>
    <h1>Check out my Spotify Tracks and Playlists!</h1>
    <h2>Enjoy Some Music While You Play</h2>

    <!-- Reload Button -->
    <form action="/reload" method="post">
        <button class="restart-button" type="submit">Reload Server</button>
    </form>

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
                <h1>Emulator</h1>
                <p>This is where your emulator will be displayed.</p>
                <!-- Insert your emulator content here -->
            </div>
        </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
