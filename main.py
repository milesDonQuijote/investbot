from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from telebot import TeleBot
import env
from investing import Investing
from bot import bot_func
from bot.TechnicalSummary import TechnicalSummary
from bot.CandlestickPatterns import CandleStickPatterns
from bot.bot_func import Data


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 "
                     "(KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

inv = Investing(driver)
bot = TeleBot(env.TOKEN)
bot_data = Data(bot)
bot_data.inv = inv
bot_data.objects['technical_summary'] = TechnicalSummary(inv)
bot_data.objects['candlestick_patterns'] = CandleStickPatterns(inv)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, env.WELCOME_TEXT, reply_markup=bot_func.start_keyboard())


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot_data.msg_obj = call
    bot_func.start_switcher(bot_data)
    bot_func.currency_switcher(bot_data)


bot.polling(none_stop=True)
driver.close()
driver.quit()
