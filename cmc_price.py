import os, requests
from bs4 import BeautifulSoup
from requests import get
from discord_webhook import DiscordWebhook

# Webhook settings
url_wb = os.environ.get('DISCORD_WH')

# Data for the scrap
token = "bitgear"
level = 0.11
url = "https://coinmarketcap.com/es/currencies/" + token + "/"
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find(class_ = 'cmc-details-panel-price__price').text
price = float(price[1:])
msg = f":moneybag: **CMC Alert** | {token.upper()} at {price}"

# Message to Discord
if price > level:
	webhook = DiscordWebhook(url=url_wb, content=msg)
	response = webhook.execute()



