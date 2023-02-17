class CandleStickPatterns:
    def __init__(self, investing_obj):
        self.inv = investing_obj
        self.currency = None
        self.candlesticks = None

    def set_currency(self, currency):
        self.currency = currency
        self.candlesticks = self.inv.get_candlestick_patterns(self.currency)

    def get(self):
        if self.candlesticks:
            self.candlesticks.load_candlestick()
            return self.__parse()

    def __parse(self):
        patterns = self.candlesticks.get_candlesticks()
        ans = "Emerging Patterns\n\n"

        for pattern in patterns['Emerging Patterns']:
            ans += \
                pattern['name'] + ' ' + pattern['timeframe']+ ' ' + \
                pattern['candles_ago'] + ' ' + pattern['time'] + "\n"

        ans += "\nCompleted Patterns\n\n"
        for pattern in patterns['Completed Patterns']:
            ans += \
                pattern['name'] + ' ' + pattern['timeframe'] + ' ' + \
                pattern['candles_ago'] + ' ' + pattern['time'] + "\n"
        return ans
