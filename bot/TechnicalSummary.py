import env
import invenv
from bot.bot_func import parse_tech


class TechnicalSummary:
    def __init__(self, investing_obj):
        self.inv = investing_obj
        self.technical_summary = None
        self.currency = None

    def set_currency(self, currency):
        self.currency = currency
        self.technical_summary = self.inv.get_currencies_techsum(currency)

    def get(self):
        if self.technical_summary:
            self.technical_summary.load_summary()
            return self.__parse()
        return None

    def __parse(self):
        tech_sum = self.technical_summary.get_all()
        ans = "Moving Average".center(30, '-') + "\n\n"
        ans += env.TECHSUM_TXT.format(
            m5=parse_tech(tech_sum[invenv.Env.MOVING_AVERAGE][0]),
            m15=parse_tech(tech_sum[invenv.Env.MOVING_AVERAGE][1]),
            h=parse_tech(tech_sum[invenv.Env.MOVING_AVERAGE][2]),
            d=parse_tech(tech_sum[invenv.Env.MOVING_AVERAGE][3]),
            M=parse_tech(tech_sum[invenv.Env.MOVING_AVERAGE][0])
        )

        ans += "\n\n" + "Technical Indicators".center(30, '-') + "\n\n"
        ans += env.TECHSUM_TXT.format(
            m5=parse_tech(tech_sum[invenv.Env.TECHNICAL_INDICATORS][0]),
            m15=parse_tech(tech_sum[invenv.Env.TECHNICAL_INDICATORS][1]),
            h=parse_tech(tech_sum[invenv.Env.TECHNICAL_INDICATORS][2]),
            d=parse_tech(tech_sum[invenv.Env.TECHNICAL_INDICATORS][3]),
            M=parse_tech(tech_sum[invenv.Env.TECHNICAL_INDICATORS][0])
        )

        ans += "\n\n" + "Summary".center(30, '-') + "\n\n"
        ans += env.TECHSUM_TXT.format(
            m5=parse_tech(tech_sum[invenv.Env.SUMMARY][0]),
            m15=parse_tech(tech_sum[invenv.Env.SUMMARY][1]),
            h=parse_tech(tech_sum[invenv.Env.SUMMARY][2]),
            d=parse_tech(tech_sum[invenv.Env.SUMMARY][3]),
            M=parse_tech(tech_sum[invenv.Env.SUMMARY][0])
        )
        return ans
