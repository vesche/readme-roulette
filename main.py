import os, random
from flask import Flask, Response, send_file

app = Flask(__name__)
gifs = os.listdir('gifs')

@app.route('/bang', methods=['GET'])
def bang() -> Response:
    gif = os.path.join('gifs', random.choice(gifs))
    return send_file(gif, mimetype='image/gif')

if __name__ == '__main__':
    app.run()

