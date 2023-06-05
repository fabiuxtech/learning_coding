from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from telegram import Bot
import asyncio
bot_token = 'mytokenbot'
# Imposta le opzioni del browser per eseguire Chromium in modalità headless
chrome_options = Options()
chrome_options.add_argument('--headless')  # Esegui in modalità headless senza interfaccia grafica
# Imposta il percorso del driver di Chromium
driver_path = '/home/pi/.wdm/drivers/chromedriver/linux64/114.0.5735.90/chromedriver'
# Inizializza il driver di Chromium
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
#
url = 'https://tracking.dpd.de/status/en_US/parcel/29130000071255'
driver.get(url)
time.sleep(2)
#script = """
#var results = [];
#
#// Codice JavaScript utilizzando jQuery
#$("span.asendia-lead").each(function() {
#    var spanText = $(this).text().trim();
#    var divText = $(this).next('.card-body').text().trim();
#    var combinedText = spanText + ' ' + divText;
#    results.push(combinedText);
#});
#
#return results;
#"""
script = """
var results = [];

// Codice JavaScript utilizzando jQuery
$("tr.animate-show").each(function() {
    var text = $(this).text().trim().replace(/\s+/g, ' ');
    if (text !== '') {
        results.push(text);
    }
});
return results;
"""
results = driver.execute_script(script)
# Chiudi il driver
driver.quit()
#
#n = 17
#filtered_results = results[n:]
#print(results[n:])
chat_ids = ['mychatid', 'otherchatid']
custom_message = '<b>Tracking dal sito DPD Group (BRT):</b>'
message = custom_message + '\n' + '\n'.join(results)
async def send_telegram_message(bot_token, chat_id, message):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message, parse_mode='HTML')

async def main():
    bot_token_tg = bot_token
    tasks = []
    for chat_id in chat_ids:
        task = send_telegram_message(bot_token_tg, chat_id, message)
        tasks.append(task)
    await asyncio.gather(*tasks)
    #chat_id_tg = chat_id
    #message_tg = message
    #await send_telegram_message(bot_token_tg, chat_id_tg, message_tg)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())