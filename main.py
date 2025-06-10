from flask import Flask, request, jsonify
import requests
import time
import hmac
import hashlib
import json

app = Flask(__name__)

# OKX API 資訊
OKX_API_KEY = "YOUR_API_KEY"
OKX_SECRET = "YOUR_SECRET"
OKX_PASSPHRASE = "YOUR_PASSPHRASE"
OKX_BASE_URL = "https://www.okx.com"
BET_AMOUNT_USDT = 50  # 每次下注金額

# Telegram 訊息通知
TELEGRAM_TOKEN = "7919123976:AAErKTsF6kGE0xON_jJ00e2xtKaCAwr8t7c"
TELEGRAM_CHAT_ID = "5140400544"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Telegram Error: {e}")

def sign_request(timestamp, method, path, body, secret):
    message = f'{timestamp}{method}{path}{body}'
    return hmac.new(secret.encode(), message.encode(), hashlib.sha256).hexdigest()

def get_price(symbol):
    url = f"{OKX_BASE_URL}/api/v5/market/ticker?instId={symbol}"
    r = requests.get(url)
    return float(r.json()["data"][0]["last"])

def place_order(symbol, side):
    price = get_price(symbol)
    size = round(BET_AMOUNT_USDT / price, 6)

    timestamp = str(time.time())
    method = "POST"
    path = "/api/v5/trade/order"
    url = OKX_BASE_URL + path

    body = {
        "instId": symbol,
        "tdMode": "cash",
        "side": side,
        "ordType": "market",
        "sz": str(size)
    }
    body_json = json.dumps(body)
    sign = sign_request(timestamp, method, path, body_json, OKX_SECRET)

    headers = {
        "OK-ACCESS-KEY": OKX_API_KEY,
        "OK-ACCESS-SIGN": sign,
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-PASSPHRASE": OKX_PASSPHRASE,
        "Content-Type": "application/json"
    }

    res = requests.post(url, headers=headers, data=body_json)
    res_json = res.json()

    if res.status_code == 200 and res_json.get("code") == "0":
        msg = f"✅ {side.upper()} {size} {symbol} at {price:.2f} USDT"
        send_telegram_message(msg)
    else:
        send_telegram_message(f"❌ Failed to place order: {res_json}")

    return res_json

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    signal = data.get("signal")
    symbol = data.get("symbol", "BTC-USDT")

    if signal in ["buy", "sell"]:
        return jsonify(place_order(symbol, signal))

    send_telegram_message(f"⚠️ Unknown signal: {signal}")
    return jsonify({"error": "invalid signal"})