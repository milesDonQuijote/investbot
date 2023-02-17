class TimeFrameButtons:
    C_MIN5_XPATH = '//li[@data-tab="time_300"]'
    C_MIN15_XPATH = '//li[@data-tab="time_900"]'
    C_HOUR_XPATH = '//li[@data-tab="time_3600"]'
    C_DAILY_XPATH = '//li[@data-tab="time_86400"]'


class Summary:
    C_SUMMER_XPATH = '//tr[@data-test="instrument-tech-table-row"]'


class CandleStick:
    C_TABLE_XPATH = '//tbody[@id="patternTableBody"]'


class Calendar:
    C_TABLE_XPATH = '//section[contains(@id,"ec_wrapper")]'

# MOVING AVERAGE
class MovingAverage:
    C_MA5_XPATH = "/html/body/div[1]/div[2]/section[3]/table[2]/tbody/tr[1]/td[3]/div"
    C_MA10_XPATH = "/html/body/div[1]/div[2]/section[3]/table[2]/tbody/tr[2]/td[3]/div/text()[2]"
    C_MA20_XPATH = "/html/body/div[1]/div[2]/section[3]/table[2]/tbody/tr[3]/td[3]/div/text()[2]"
    C_MA50_XPATH = "/html/body/div[1]/div[2]/section[3]/table[2]/tbody/tr[4]/td[3]/div/text()[2]"
    C_MA100_XPATH = "/html/body/div[1]/div[2]/section[3]/table[2]/tbody/tr[5]/td[3]/div/text()[2]"
    C_MA200_XPATH = "/html/body/div[1]/div[2]/section[3]/table[2]/tbody/tr[6]/td[3]/div/text()[2]"
    C_MA_SUM_XPATH = "/html/body/div[1]/div[2]/section[3]/table[2]/tbody/tr[7]/td[3]/div"


# TECHNICAL INDICATORS
class TechnicalIndicators:
    C_RSI_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[1]/td[3]/div"
    C_RSIVAL_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[1]/td[2]"
    C_STOCH_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[2]/td[3]/div"
    C_STOCHVAL_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[2]/td[2]"
    C_STOCHRSI_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[3]/td[3]/div"
    C_STOCHRSIVAL_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[3]/td[2]"
    C_MACD_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[4]/td[3]/div"
    C_MACDVAL_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[4]/td[2]"
    C_ADX_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[6]/td[3]/div"
    C_ADXVAL_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[6]/td[2]"
    C_WILLIAMS_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[11]/td[3]/div"
    C_WILLIAMSVAL_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[11]/td[2]"
    C_CCI_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[7]/td[3]/div"
    C_CCIVAL_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[7]/td[2]"
    C_ATR_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[5]/td[3]/div"
    C_ATRVALL_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[5]/td[2]"

    # Highs/Lows
    C_HL_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[8]/td[3]/div"
    C_HLVAL_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[8]/td[2]"

    # Ultimate Oscilator
    C_ULTOSC_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[9]/td[3]/div"
    C_ULTOSCVAL_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[9]/td[2]"

    C_ROC_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[10]/td[3]/div"
    C_ROCVAL_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[10]/td[2]"

    # Bull/Pear Power
    C_BULLP_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[12]/td[3]/div"
    C_BULLPVAL_XPATH = "/html/body/div[1]/div[2]/section[3]/table[3]/tbody/tr[12]/td[2]"

    C_TECHSUM_XPATH = ""