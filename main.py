from datetime import datetime
from pyrogram import Client, filters
from pyrogram import enums
from apis import GetAllDataNobitex
from chart_apis import ChartCrypto, api_key, id

api_id = "" #api id here
api_hash = "" #api hash here
bot_token = "" #bot token here

app = Client("crypto_price_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
def start(client, message):
    welcome_text = (
        "👋 Welcome to the Crypto Price Bot!\n"
        "Send me a coin symbol (BTC, ETH, XRP, ADA, DOGE ...)\n"
        "📌 Data Source: Nobitex API\n"
        "👤 Created by @TheeeRaven"
    )
    message.reply_text(welcome_text)

@app.on_message(filters.text)
def get_price(client, message):
    coin = message.text.strip().upper()
    fetcher = GetAllDataNobitex()

    price_data = fetcher.get_price(coin)

    irr = f"{int(float(price_data['IRR'])):,}"
    usdt = f"{float(price_data['USDT']):,}"
    change = float(price_data["dayChange"])

    change_emoji = "🟢" if change >= 0 else "🔴"

    chart_fetcher = ChartCrypto(api_key, id)
    chart_data = chart_fetcher.get_chart(coin)
    img = chart_data["image"]
    response = (
        f"💰 **{price_data['name']} Price**\n"
        f"┏━━━━━━━━━━━━━━━━━━\n"
        f"┃ 🇮🇷 IRR: `{irr}` تومان\n"
        f"┃ 💵 USDT: `{usdt}` $\n"
        f"┃ 📊 24h Change: {change_emoji} `{change}%`\n"
        f"┗━━━━━━━━━━━━━━━━━━\n"
        f"⏱ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"👤 Bot by @TheeeRaven"
    )

    message.reply_photo(photo=img, caption=response, parse_mode=enums.ParseMode.MARKDOWN)

if __name__ == "__main__":
    print("Bot is running...")
    app.run()


