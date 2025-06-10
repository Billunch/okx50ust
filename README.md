# tv-okx-bot-telegram-v2

## 📌 功能簡介
這是一個自動化交易機器人，用於接收 TradingView 發出的 webhook 訊號，並透過 OKX API 自動下單，同時將下單結果即時傳送到 Telegram。

---

## ⚙️ 使用技術
- Python 3
- Flask（Webhook Server）
- OKX REST API（下單）
- Telegram Bot API（推播通知）
- Render（免費雲端部署）

---

## 🚀 如何使用

### 1️⃣ 建立 Telegram Bot
1. 在 Telegram 中與 [@BotFather](https://t.me/BotFather) 對話，建立新 Bot 並取得 Bot Token。
2. 傳送訊息給你的 Bot，並透過以下網址取得 Chat ID：
   ```
   https://api.telegram.org/bot<你的BotToken>/getUpdates
   ```

### 2️⃣ 設定 OKX API
前往 OKX → 個人帳戶 → API 設定，建立 API 金鑰，並記下：
- `OKX_API_KEY`
- `OKX_SECRET`
- `OKX_PASSPHRASE`

### 3️⃣ 修改 `main.py`
打開 `main.py`，修改以下變數為你的實際資訊：
```python
OKX_API_KEY = "YOUR_API_KEY"
OKX_SECRET = "YOUR_SECRET"
OKX_PASSPHRASE = "YOUR_PASSPHRASE"
TELEGRAM_TOKEN = "你的 Bot Token"
TELEGRAM_CHAT_ID = "你的 Chat ID"
```

### 4️⃣ 部署到 Render
1. 推送此專案到你的 GitHub。
2. 前往 [https://render.com](https://render.com)，建立 Web Service：
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
   - Plan: Free
3. Render 部署完成後會提供一個 URL，複製該網址作為 TradingView 的 webhook 目標。

### 5️⃣ 設定 TradingView
在 TradingView 策略 alert 設定中填入：
- **Webhook URL**：Render 給你的網址
- **Alert message**：
```json
{ "signal": "buy", "symbol": "BTC-USDT" }
```

---

## 🔐 安全建議
- Render 僅用於個人用途時再使用免費版
- 可於 server 加上驗證 token 或 IP 白名單來限制訪問權限
- 不要公開分享你的 `main.py` 或 `.env` 金鑰內容

---

## 📞 訊息通知範例

| 狀況 | Telegram 訊息 |
|------|----------------|
| 成功下單 | ✅ BUY 0.001 BTC at 68000 USDT |
| 下單失敗 | ❌ Failed to place order: {...} |
| 無效訊號 | ⚠️ Unknown signal: hold |

---

## 🧠 延伸功能建議
- ✅ 支援多幣種自動下注
- ✅ 加入凱利公式動態下注比率
- ✅ 加入日誌記錄、錯誤回傳強化
- ✅ 每日績效報表推送

---

## 🛠 作者說明
此專案由 ChatGPT 根據使用者需求自動生成，請依實際需求調整後使用。