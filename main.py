import os, random, json
from flask import Flask, Response, send_file, request, jsonify

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
def boom() -> Response:
    highscores = sb.table("Highscores").select("*").execute()
    return jsonify(highscores), 200

if __name__ == '__main__':
    app.run()
