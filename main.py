import requests
from flask import Flask, request, send_from_directory

# Replace "YOUR_API_KEY_HERE" with your actual API key.
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://www.alphavantage.co/query"

app = Flask(__name__)


@app.route("/")
def index():
  return "Hello world!  Your web application is working!"


@app.route('/stock', methods=['GET'])
def get_stock_data():
  symbol = request.args.get('symbol')

  params = {"function": "GLOBAL_QUOTE", "symbol": symbol, "apikey": API_KEY}

  response = requests.get(BASE_URL, params=params)
  return response.json()


@app.route('/.well-known/ai-plugin.json')
def serve_ai_plugin():
  return send_from_directory('.',
                             'ai-plugin.json',
                             mimetype='application/json')


@app.route('/openapi.yaml')
def serve_openapi_yaml():
  return send_from_directory('.', 'openapi.yaml', mimetype='text/yaml')


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)