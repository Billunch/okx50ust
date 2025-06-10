# tv-okx-bot (Render 安全環境變數版)

## ✅ Render 環境變數設定（Environment Variables）

請在 Render 後台加入以下 5 組環境變數：

| 名稱               | 說明                            |
|--------------------|---------------------------------|
| OKX_API_KEY        | 你的 OKX API Key                |
| OKX_SECRET         | 你的 OKX Secret                 |
| OKX_PASSPHRASE     | 建立 OKX API 金鑰時設定的密碼    |
| TELEGRAM_TOKEN     | 你的 Telegram Bot Token         |
| TELEGRAM_CHAT_ID   | 你的 Telegram 個人 Chat ID      |

## 🛠️ Render 設定方式

1. 推送此專案到 GitHub
2. Render 建立 Web Service
   - Runtime: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
3. 在環境變數設定區加入上表內容
4. TradingView Webhook 使用 Render 的網址 + JSON 訊號即可

    ```json
    { "signal": "buy", "symbol": "BTC-USDT" }
    ```

建議使用 `.gitignore` 忽略任何 .env 檔案，避免關鍵資訊洩露。