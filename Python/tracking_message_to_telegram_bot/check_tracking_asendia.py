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
#driver_path = '/mnt/c/Users/fabiu/.wdm/drivers/chromedriver/win32/114.0.5735.90/chromedriver'
driver_path = '/usr/bin/chromedriver'
# Inizializza il driver di Chromium
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
#
url = 'https://a1.asendiausa.com/tracking/?trackingnumber=EEUS001512506IT0'
driver.get(url)
time.sleep(2)
script = """
var results = [];

//codice JavaScript utilizzando jQuery
$("span.asendia-lead").each(function() {
    var text = $(this).text().trim();
    results.push(text);
});
return results;
"""
results = driver.execute_script(script)
# Chiudi il driver
driver.quit()
#
n = 17
filtered_results = results[n:]
#print(results[n:])
chat_id = '32230559'
custom_message = '<b>Tracking dal sito Asendia USA:</b>'
message = custom_message + '\n' + '\n'.join(filtered_results)

def send_message():
    async def send_telegram_message(bot_token, chat_id, message):
        bot = Bot(token=bot_token)
        await bot.send_message(chat_id=chat_id, text=message, parse_mode='HTML')
    async def main():
        bot_token_tg = bot_token
        chat_id_tg = chat_id
        message_tg = message
        await send_telegram_message(bot_token_tg, chat_id_tg, message_tg)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

asenda_txt = '/home/fabiuxtech/coding/learning_coding/Python/tracking_message_to_telegram_bot/asenda.txt'
list_to_str = ' '.join(filtered_results)
if os.path.exists(asenda_txt):
    file = open('asenda.txt', 'r')
    read_file_before = file.read()
    if read_file_before == list_to_str:
        print(f'I risultati sono identici quindi non procedo.')
        file.close()
    else:
        print(f'Le informazioni sono diverse quindi procedo con l\'update')
        file=open('asenda.txt', 'w')
        file.write(list_to_str)
        file.close()
        file=open('asenda.txt', 'r')
        read_file_after = file.read()
        print(read_file_after)
        file.close()
else:
    print('Non ho informazioni, quindi procedo con l\'update')
    send_message()
    file=open('asenda.txt', 'w')
    file.write(list_to_str)
    file.close()
    file=open('asenda.txt', 'r')
    read_file_after = file.read()
    print(read_file_after)
    file.close()