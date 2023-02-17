import time
import re
import xpaths
import urls
import arbix
from invenv import TimeLimits, MaOPT, TiOPT, Env
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Investing:
    def __init__(self, driver, url="https://m.investing.com"):
        self.__url = url
        self.driver = driver
        self.__wait = WebDriverWait(driver, 20)
        self.__actions = ActionChains(self.driver)

    def get_currencies_techsum(self, curr):
        return InvestingCurrenciesTechnicalSummary(curr, self.driver, self.__wait, self.__actions, self.__url)

    def get_candlestick_patterns(self, curr):
        return InvestingCandlestickPatterns(curr, self.driver, self.__wait, self.__actions, self.__url)

    def get_economic_calendar(self):
        return InvestingEconomicCalendar(self.driver, self.__wait, self.__actions, self.__url)


class InvestingCurrenciesTechnicalSummary:

    def __init__(self, curr, driver, wait, actions, url):
        self.__driver = driver
        self.__wait = wait
        self.__actions = actions
        self.__status = ''
        self.__url = url
        self.summary_data = {}
        self.curr = curr

    def get_summary(self):
        return self.summary_data[Env.SUMMARY]

    def get_moving_average(self):
        return self.summary_data[Env.MOVING_AVERAGE]

    def get_technical_indicators(self):
        return self.summary_data[Env.TECHNICAL_INDICATORS]

    def get_all(self):
        return self.summary_data

    def load_summary(self):
        self.summary_data.clear()
        self.__driver.get(self.__url + urls.CURRENCIES_TECH_SUM.format(self.curr))
        summary_data = self.__wait.until(EC.presence_of_all_elements_located((By.XPATH, xpaths.Summary.C_SUMMER_XPATH)))
        for data in summary_data:
            key = data.text
            key = key.replace('Moving Averages', Env.MOVING_AVERAGE)
            key = key.replace('Technical Indicators', Env.TECHNICAL_INDICATORS)
            key = key.replace('Summary', Env.SUMMARY)
            key = key.replace('Neutral', Env.NEUTRAL)
            key = key.replace('Strong Sell', Env.STRONG_SELL)
            key = key.replace('Strong Buy', Env.STRONG_BUY)
            key = key.replace('Sell', Env.SELL)
            key = key.replace('Buy', Env.BUY)
            elements = key.split()
            self.summary_data[elements[0]] = elements[1:]


class InvestingCandlestickPatterns:
    def __init__(self, curr, driver, wait, actions, url):
        self.__driver = driver
        self.__wait = wait
        self.__actions = actions
        self.__status = ''
        self.__url = url
        self.__candlesticks = {}
        self.curr = curr

    def get_completed_patterns(self):
        return self.__candlesticks['Completed Patterns']

    def get_emerging_patterns(self):
        return self.__candlesticks['Emerging Patterns']

    def get_candlesticks(self):
        return self.__candlesticks

    def load_candlestick(self):
        self.__candlesticks.clear()
        self.__driver.get(self.__url + urls.CURRENCIES_CANDLESTICK.format(self.curr))
        lines = self.__wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, xpaths.CandleStick.C_TABLE_XPATH)
        ))[0].text.split('\n')
        type = 1
        self.__candlesticks['Completed Patterns'] = []
        self.__candlesticks['Emerging Patterns'] = []
        for line in lines:
            if "Completed Patterns" == line:
                type = 1
                continue
            elif "Emerging Patterns" == line:
                type = 2
                continue
            candle = {}
            name_l = re.search(r"\d", line)
            candle['name'] = line[:name_l.start()].strip()
            candle['timeframe'] = line[name_l.start():].split()[0]
            candle['candles_ago'] = line[name_l.start():].split()[1]
            candle['time'] = line[name_l.start() + len(candle['timeframe']) + len(candle['candles_ago']) + 2:].strip()
            if type == 1:
                self.__candlesticks['Completed Patterns'].append(candle)
            else:
                self.__candlesticks['Emerging Patterns'].append(candle)


class InvestingEconomicCalendar:
    def __init__(self, driver, wait, actions, url):
        self.__driver = driver
        self.__wait = wait
        self.__actions = actions
        self.__status = ''
        self.__url = url
        self.__calendar = []

    def get_calendar(self):
        return self.__calendar

    def load_calendar(self):
        self.__calendar.clear()
        self.__driver.get(self.__url + urls.ECONOMIC_CALENDAR)
        calendar = self.__wait.until(EC.presence_of_element_located(
            (By.ID, "ec_wrapper")
        )).text.split('\n')
        tmp = []
        i = j = 0
        while i < len(calendar):
            if not arbix.is_clock(calendar[i]):
                i += 1
                continue
            tmp.append(calendar[i])
            j = 0
            i += 1
            while i < len(calendar) and j < 3 and not arbix.is_clock(calendar[i]):
                tmp.append(calendar[i])
                i += 1
                j += 1
            self.__calendar.append(tmp.copy())
            tmp.clear()