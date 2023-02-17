from telebot import TeleBot, types
import env
import invenv
from investing import Investing


class Data:
    def __init__(self, bot_obj):
        self.bot = bot_obj
        self.inv = None
        self.msg_obj = None
        self.objects = {}
        return


# Keyboards
def start_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(env.BTN_TS, callback_data=env.BTN_TS),
        types.InlineKeyboardButton(env.BTN_EC, callback_data=env.BTN_EC),
        types.InlineKeyboardButton(env.BTN_CP, callback_data=env.BTN_CP)
    )
    return keyboard


def currencies_keyboard(tp):
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(env.BTN_EURUSD, callback_data=tp + ' ' + parse_currency(env.BTN_EURUSD)),
        types.InlineKeyboardButton(env.BTN_GBPUSD, callback_data=tp + ' ' + parse_currency(env.BTN_GBPUSD)),
        types.InlineKeyboardButton(env.BTN_EURCHF, callback_data=tp + ' ' + parse_currency(env.BTN_EURCHF))
    )
    return keyboard


# Basic
def get_calendar(inv):
    calendar = inv.get_economic_calendar()
    calendar.load_calendar()
    data = calendar.get_calendar()
    parsed = ''
    for date in data:
        for i in date:
            parsed += i + ' '
        parsed += "\n\n"
    return parsed


# Switchers
def start_switcher(bot):
    if bot.msg_obj.data == env.BTN_TS:
        bot.bot.send_message(bot.msg_obj.message.chat.id, env.CHOOSECUR_TEXT, reply_markup=currencies_keyboard('ts'))

    elif bot.msg_obj.data == env.BTN_CP:
        bot.bot.send_message(bot.msg_obj.message.chat.id, env.CHOOSECUR_TEXT, reply_markup=currencies_keyboard('cp'))

    elif bot.msg_obj.data == env.BTN_EC:
        bot.bot.send_message(bot.msg_obj.message.chat.id, get_calendar(bot.inv))

    elif bot.msg_obj.data == env.BTN_CNCL:
        bot.bot.send_message(bot.msg_obj.message.chat.id, reply_markup=start_keyboard())


def currency_switcher(bot):
    data = bot.msg_obj.data.split()
    if len(data) != 2:
        return
    s_type = data[0]
    currency = data[1]
    if s_type == env.TYPE_TS:
        ts = bot.objects['technical_summary']
        ts.set_currency(currency)
        bot.bot.send_message(bot.msg_obj.message.chat.id, ts.get())
    elif s_type == env.TYPE_CP:
        cp = bot.objects['candlestick_patterns']
        cp.set_currency(currency)
        bot.bot.send_message(bot.msg_obj.message.chat.id, cp.get())


# +
def parse_tech(txt):
    if txt == invenv.Env.NEUTRAL:
        return 'Neutral'
    elif txt == invenv.Env.SELL:
        return 'Sell'
    elif txt == invenv.Env.STRONG_SELL:
        return 'Strong Sell'
    elif txt == invenv.Env.BUY:
        return 'Buy'
    elif txt == invenv.Env.STRONG_BUY:
        return 'Strong Buy'


def parse_currency(currency):
    return currency.split('/')[0].lower() + '-' + currency.split('/')[1].lower()

