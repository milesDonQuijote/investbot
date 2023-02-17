
# timelimits
class TimeLimits:
    MIN5 = "min5"
    MIN15 = "min15"
    HOUR = "hour"
    DAILY = "daily"


# Currencies
class Currencies:
    EURUSD = "eur-usd"
    EURGBP = "eur-gbp"


# Moving Average Options
class MaOPT:
    MA5 = "min5"
    MA10 = "min10"
    MA20 = "min20"
    MA50 = "min50"
    MA100 = "min100"
    MA200 = "min200"
    SUM = "sum"


# Technical Indicators Options
class TiOPT:
    RSI = "rsi14"
    STOCH = "stoch9_6"
    STOCHRSI = "stochrsi"
    MACD = "macd"
    ADX = "adx"
    WILLIAMS = "williams"
    CCI = "cci"
    ATR = "atr"
    HIGHS_LOWS = "high_lows"
    ULTIMATE_OSCILATOR = "ultimate_oscilator"
    ROC = "roc"
    BULL_BEAR_POWER = "bp"
    SUM = "sum"

class Env:
    MOVING_AVERAGE = "M"
    TECHNICAL_INDICATORS = "T"
    SUMMARY = "S"
    NEUTRAL = "0"
    STRONG_SELL = "1"
    SELL = "2"
    BUY = "3"
    STRONG_BUY = "4"
