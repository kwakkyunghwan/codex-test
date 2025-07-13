from pathlib import Path
import json
from flask import Flask, jsonify
from .filter import apply_conditions

app = Flask(__name__)

ROOT = Path(__file__).resolve().parent.parent
STOCKS_PATH = ROOT / 'data' / 'stocks.json'
CONDITIONS_PATH = Path(__file__).resolve().parent / 'conditions.json'

@app.route('/scan')
def scan():
    with open(STOCKS_PATH) as f:
        stocks = json.load(f)
    with open(CONDITIONS_PATH) as f:
        conditions = json.load(f)
    result = apply_conditions(stocks, conditions)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
