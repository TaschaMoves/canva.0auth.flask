from flask import Flask, redirect, request
import os
import requests

app = Flask(__name__)

REDIRECT_URI = 'https://taschamoves-oauth.onrender.com/callback'

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

@app.route('/')
def home():
    return '✅ Server läuft! Klicke <a href="/login">hier</a>, um dich mit Canva zu verbinden.'

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
    token_response = requests.post(
        'https://www.canva.com/oauth/token',
        data={
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
    )
    return token_response.json()

@app.route('/callback/')
def callback_slash():
    return callback()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
