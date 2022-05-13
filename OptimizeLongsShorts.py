import random
import re
from selenium.common.exceptions import (NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException)
from selenium.webdriver.support.ui import WebDriverWait

import time
import pandas as pd
from my_functions import Functions
from profit import profits
from TradeViewGUI import Main

# Global variables --> **to be updated by user**
# here time represents in seconds. example 5minutes - 300
TIME_BETWEEN_ALERT_UPDATE = 10

# Next to crypto BTCUSDT
INITIAL_TIME = '1m'

# For optimal solution - please change as per needed.
buy_factor_range = [0.0001, 10.0]
sell_factor_range = [0.0001, 10.0]
adx_smoothing_range = [2, 30]
di_length_range = [2, 60]


class LongShortScript(Functions):
    """find the best stop loss and take profit values for your strategy."""

    def __init__(self):
        Main.__init__(self)
        self.driver = self.create_driver()
        self.run_script()

    def run_script(self):
        # Loading website with web driver.
        wait = WebDriverWait(self.driver, 15)
        best_settings = {'profit': 0, 'long_stoploss': 0, 'long_takeprofit': 0, 'short_stoploss': 0,
                         'short_takeprofit': 0, 'buy_factor': 0, 'sell_factor': 0,
                         'adx_smoothing': 0, 'di_length': 0}
        try:
            self.driver.get("https://www.tradingview.com/chart/")
        except Exception:
            print(
                "WebDriver Error: Please Check Your FireFox Profile Path Is Correct.\n"
            )
            print(
                "Find Your Firefox Path Instructions. https://imgur.com/gallery/rdCqeT5 "
            )
            return

        # Making sure strategy tester tab is clicked so automation runs properly.
        try:
            self.click_strategy_tester(wait)
            self.click_overview()
        except NoSuchElementException:
            self.click_overview()
        print("Generating Max Profit For Stop Loss.")
        print("Loading script...\n")

        # picking the favorite strategy
        self.close_existing_alert(wait)
        self.click_indicators(wait)
        self.click_favorite_indicator(wait)
        # Picking time
        self.click_time_button(INITIAL_TIME, wait)

        # Making sure we are on inputs tab and resetting values to default settings.
        self.click_settings_button(wait)
        self.click_properties_tab()
        self.click_input_tab()
        self.click_enable_both_checkboxes()
        self.click_rest_all_inputs()
        self.click_ok_button()

        # Loop through max attempts while randomizing values each attempt.
        count = 0
        lastsave = 0
        change = False
        best_settings = pd.DataFrame(data={'profit':[0]})
        try:
            # starting range
            while count < int(self.maxAttemptsValue.text()):
                try:
                    count = 1

                    # if loop < 30:
                    #     loop += 1
                        # Creating random values every loop.
                    long_stoploss_value = round(
                        random.uniform(float(self.minLongStoplossValue.text()),
                                       float(self.maxLongStoplossValue.text()),
                                       ),
                        int(self.decimalPlaceValue.text()),
                    )
                    long_takeprofit_value = round(
                        random.uniform(
                            float(self.minLongTakeprofitValue.text()),
                            float(self.maxLongTakeprofitValue.text()),
                        ),
                        int(self.decimalPlaceValue.text()),
                    )
                    short_stoploss_value = round(
                        random.uniform(
                            float(self.minShortStoplossValue.text()),
                            float(self.maxShortStoplossValue.text()),
                        ),
                        int(self.decimalPlaceValue.text()),
                    )
                    short_takeprofit_value = round(
                        random.uniform(
                            float(self.minShortTakeprofitValue.text()),
                            float(self.maxShortTakeprofitValue.text()),
                        ),
                        int(self.decimalPlaceValue.text()),
                    )

                    buy_factor = round(
                        random.uniform(
                            buy_factor_range[0],
                            buy_factor_range[1],
                        ),
                        4,
                    )

                    sell_factor = round(
                        random.uniform(
                            sell_factor_range[0],
                            sell_factor_range[1],
                        ),
                        4,
                    )

                    adx_smoothing = round(
                        random.uniform(
                            adx_smoothing_range[0],
                            adx_smoothing_range[1],
                        ),
                        0,
                    )

                    di_length = round(
                        random.uniform(
                            di_length_range[0],
                            di_length_range[1],
                        ),
                        0,
                    )

                    # Click settings button
                    self.click_settings_button(wait)

                    # Click all input boxes and add new values.
                    self.click_all_inputs(
                        long_stoploss_value,
                        long_takeprofit_value,
                        short_stoploss_value,
                        short_takeprofit_value,
                        buy_factor,
                        sell_factor,
                        adx_smoothing,
                        di_length,
                        wait,
                    )

                    # Saving the profitability of the new values into a dictionary.
                    net_profit = self.get_net_all(
                        long_stoploss_value,
                        long_takeprofit_value,
                        short_stoploss_value,
                        short_takeprofit_value,
                        buy_factor,
                        sell_factor,
                        adx_smoothing,
                        di_length,
                        wait,
                    )

                        # print('net profit', float(re.sub(r'[^\x00-\x7F]+', '-', net_profit[0])), best_settings['profit'])
                    #
                    if float(re.sub(r'[^\x00-\x7F]+', '-', net_profit[0])) > best_settings['profit'].iloc[0]:
                        change = True
                        best_settings = pd.DataFrame({'profit': [float(re.sub(r'[^\x00-\x7F]+', '-', net_profit[0]))],
                                         'long_stoploss': [long_stoploss_value],
                                         'long_takeprofit': [long_takeprofit_value],
                                         'short_stoploss': [short_stoploss_value],
                                         'short_takeprofit': [short_takeprofit_value],
                                         'buy_factor': [buy_factor],
                                         'sell_factor': [sell_factor],
                                         'adx_smoothing': [adx_smoothing],
                                         'di_length': [di_length]})

                    if time.time() - lastsave > TIME_BETWEEN_ALERT_UPDATE and change:
                        change = False
                        lastsave = time.time()
                        best_settings.to_csv('best_case_in_past_5_minutes.csv', index=False)
                        self.save_strategy()
                        self.set_new_alert(alert_message='Alert by BOT', wait=wait)
                        # self.click_settings_button(wait)
                        # self.click_rest_all_inputs()
                        # self.click_ok_button()

                    # else:
                    #     print("**========NEW CYCLE========**")
                    #     print('Best Settings: %s'% best_settings)
                    #     loop = 0
                    #     long_stoploss_value = best_settings['long_stoploss']
                    #     long_takeprofit_value = best_settings['long_takeprofit']
                    #     short_stoploss_value = best_settings['short_stoploss']
                    #     short_takeprofit_value = best_settings['short_takeprofit']
                    #     buy_factor = best_settings['buy_factor']
                    #     sell_factor = best_settings['sell_factor']
                    #     adx_smoothing = best_settings['adx_smoothing']
                    #     di_length = best_settings['di_length']
                    #
                    #     long_stoploss_range = [long_stoploss_value - long_stoploss_value * percentage,
                    #                            long_stoploss_value + long_stoploss_value * percentage]
                    #     long_takeprofit_range = [long_takeprofit_value - long_takeprofit_value * percentage,
                    #                              long_takeprofit_value + long_takeprofit_value * percentage]
                    #     short_stoploss_range = [short_stoploss_value - short_stoploss_value * percentage,
                    #                             short_stoploss_value + short_stoploss_value * percentage]
                    #     short_takeprofit_range = [short_takeprofit_value - short_takeprofit_value * percentage,
                    #                               short_takeprofit_value + short_takeprofit_value * percentage]
                    #     buy_factor_range = [buy_factor - buy_factor * percentage,
                    #                         buy_factor + buy_factor * percentage]
                    #     sell_factor_range = [sell_factor - sell_factor * percentage,
                    #                          sell_factor + sell_factor * percentage]
                    #     adx_smoothing_range = [adx_smoothing - adx_smoothing * percentage,
                    #                            adx_smoothing + adx_smoothing * percentage]
                    #     di_length_range = [di_length - di_length * percentage,
                    #                        di_length + di_length * percentage]

                except (
                        StaleElementReferenceException,
                        TimeoutException,
                        NoSuchElementException,
                ) as error:
                    if error:
                        count -= 1
                        continue
        except ValueError:
            print(
                "\nValue Error: Make sure all available text input boxes are filled with a number for script to run properly.\n"
            )
            return

        # Adding the best parameters into your strategy.
        self.click_settings_button(wait)
        best_key = self.find_best_key_both()
        self.click_all_inputs(
            profits[best_key][1],
            profits[best_key][3],
            profits[best_key][5],
            profits[best_key][7],
            wait,
        )
        self.driver.implicitly_wait(1)

        print("\n----------Results----------\n")
        self.click_overview()
        self.print_best_all()
        self.click_performance_summary()
        self.print_total_closed_trades()
        self.print_net_profit()
        self.print_win_rate()
        self.print_max_drawdown()
        self.print_sharpe_ratio()
        self.print_sortino_ratio()
        self.print_win_loss_ratio()
        self.print_avg_win_trade()
        self.print_avg_loss_trade()
        self.print_avg_bars_in_winning_trades()
        # print("\n----------More Results----------\n")
        # self.print_gross_profit()
        # self.print_gross_loss()
        # self.print_buy_and_hold_return()
        # self.print_max_contracts_held()
        # self.print_open_pl()
        # self.print_commission_paid()
        # self.print_total_open_trades()
        # self.print_number_winning_trades()
        # self.print_number_losing_trades()
        # self.print_percent_profitable()
        # self.print_avg_trade()
        # self.print_avg_win_trade()
        # self.print_avg_loss_trade()
        # self.print_largest_winning_trade()
        # self.print_largest_losing_trade()
        # self.print_avg_bars_in_trades()
        # self.print_avg_bars_in_winning_trades()
        # self.print_avg_bars_in_losing_trades()
        # self.print_margin_calls()
