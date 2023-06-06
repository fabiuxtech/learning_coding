from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from telegram import Bot
import asyncio
import warnings
import os
warnings.simplefilter('ignore', category=DeprecationWarning)
bot_token = 'miotoken'
# Imposta le opzioni del browser per eseguire Chromium in modalità headless
chrome_options = Options()
chrome_options.add_argument('--headless')  # Esegui in modalità headless senza interfaccia grafica
# Imposta il percorso del driver di Chromium
driver_path = '/usr/bin/chromedriver'
# Inizializza il driver di Chromium
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
#
url = 'https://tracking.dpd.de/status/en_US/parcel/29130000071255'
driver.get(url)
time.sleep(2)

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
chat_ids = ['32230559', '137293063']
#nicola id 137293063
custom_message = '<b>Tracking dal sito DPD Group (BRT):</b>'
message = custom_message + '\n' + '\n'.join(results)

def send_message():
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
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

dpd_txt = '/home/fabiuxtech/coding/learning_coding/Python/tracking_message_to_telegram_bot/dpd.txt'
list_to_str = ' '.join(results)
if os.path.exists(dpd_txt):
    file = open('dpd.txt', 'r')
    read_file_before = file.read()
    if read_file_before == list_to_str:
        print(f'I risultati sono identici quindi non procedo.')
        file.close()
    else:
        print(f'Le informazioni sono diverse quindi procedo con l\'update')
        file=open('dpd.txt', 'w')
        file.write(list_to_str)
        file.close()
        file=open('dpd.txt', 'r')
        read_file_after = file.read()
        print(read_file_after)
        file.close()
else:
    print('Non ho informazioni, quindi procedo con l\'update')
    send_message()
    file=open('dpd.txt', 'w')
    file.write(list_to_str)
    file.close()
    file=open('dpd.txt', 'r')
    read_file_after = file.read()
    print(read_file_after)
    file.close()