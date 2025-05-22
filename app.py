from flask import Flask, redirect, request
import os

app = Flask(__name__)

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = 'https://taschamoves-oauth.onrender.com/callback'

@app.route('/')
def home():
    return 'Server läuft! → <a href="/login">Login</a>'

@app.route('/login')
def login():
    return redirect(
        f'https://www.canva.com/oauth/authorize'
        f'?client_id={CLIENT_ID}'
        f'&redirect_uri={REDIRECT_URI}'
        f'&response_type=code'
    )

@app.route('/callback')
def callback():
    code = request.args.get('code')
    return f'CALLBACK REACHED: code={code}', 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
