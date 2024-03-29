import os, random, json
from flask import Flask, Response, send_file, request, jsonify
import supabase

app = Flask(__name__)
gifs = os.listdir('gifs')

sb = supabase.create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_KEY"],
)

@app.route('/bang', methods=['GET'])
def bang() -> Response:
    gif = os.path.join('gifs', random.choice(gifs))
    return send_file(gif, mimetype='image/gif')

@app.route('/boom', methods=['POST'])
def boom() -> Response:
    data = json.loads(request.data)
    _ = sb.table("Highscores").insert(data).execute()
    return "gotemcoach", 200

@app.route('/snag', methods=['GET'])
def snag() -> Response:
    highscores = sb.table("Highscores").select("*").execute()
    snag_response = jsonify(json.loads(highscores.json()))
    snag_response.headers.add('Access-Control-Allow-Origin', '*')
    return snag_response, 200

if __name__ == '__main__':
    app.run()
