# 🚀 Crypto Price Bot

A clean and simple Telegram bot for fetching **crypto prices (IRR &
USDT)** and sending **chart images** using the `fast-creat.ir` API.

This project contains three main Python files:

-   **main.py** --- Telegram bot controller\
-   **apis.py** --- Crypto price API handler\
-   **chart_apis.py** --- Chart fetching handler

------------------------------------------------------------------------

## 📌 Features

-   Fetch live crypto price in **Toman (IRR)** and **USDT**
-   Display **24h percentage change**
-   Automatically send **chart image** of the requested coin
-   Clean structured response with formatting
-   Simple keyword-based usage (e.g., `BTC`, `ETH`)

------------------------------------------------------------------------

## 🗂 Project Structure

    ├── main.py
    ├── apis.py
    ├── chart_apis.py
    └── README.md

### `main.py`

Handles Telegram updates, receives messages, calls APIs, and sends the
chart image + price info.

### `apis.py`

Gets Nobitex-based crypto prices using:

    https://api.fast-creat.ir/nobitex/v2

### `chart_apis.py`

Fetches chart info (including image URL):

    https://api.fast-creat.ir/chart

------------------------------------------------------------------------

## 🔧 Requirements

-   Python 3.8+
-   Required packages:

```{=html}
<!-- -->
```
    pip install pyrogram requests python-dotenv

Optional (faster Pyrogram):

    pip install tgcrypto

------------------------------------------------------------------------

## ⚙️ Configuration (Environment Variables)

Before running, set:

    FAST_CREAT_API_KEY=your_api_key_here
    TELEGRAM_API_ID=123456
    TELEGRAM_API_HASH=your_api_hash_here
    TELEGRAM_BOT_TOKEN=your_bot_token_here
    CHART_ID=raven

Use a `.env` file for safety.\
⚠️ **Never commit your keys or tokens to GitHub.**

------------------------------------------------------------------------

## ▶️ Running the Bot

1.  Install requirements:

```{=html}
<!-- -->
```
    pip install -r requirements.txt

2.  Run the bot:

```{=html}
<!-- -->
```
    python main.py

3.  Bot should display:

```{=html}
<!-- -->
```
    Bot is running...

------------------------------------------------------------------------

## 💬 Usage

Simply send the bot a crypto symbol:

    BTC
    ETH
    XRP
    SOL

The bot replies with:

-   Price in **IRR**
-   Price in **USDT**
-   24h Change (%)
-   Chart Image

------------------------------------------------------------------------

## 🐞 Troubleshooting

-   **TgCrypto is missing** → Install:

        pip install tgcrypto

-   **Chart not sent** → Chart API may not return an image\

-   **None / KeyError** → API key invalid or API offline\

-   **Bot not responding** → Check `bot_token` or network

------------------------------------------------------------------------

## 🎯 Future Improvements (Optional)

-   Inline buttons for chart intervals (1h, 4h, 1d)
-   Multi-language support
-   Caching API results
-   Adding buy/sell signals

------------------------------------------------------------------------

## 📄 License

This project is currently license-free.\
Feel free to add `MIT` or any license you prefer.
