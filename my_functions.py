import time

from selenium.common.exceptions import (ElementNotInteractableException,
                                        NoSuchElementException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from termcolor import colored
from selenium.webdriver import ActionChains

from profit import profits
from TradeViewGUI import Main
import re

long_stopless_xpath = "//*[@class='input-uGWFLwEy with-end-slot-uGWFLwEy']"
settings_icon = "//*[@class='icon-1f5iHRsw']"


class Functions(Main):
    """You will find click, get, find, and show_me functions here."""

    # Find Functions
    def find_best_stoploss(self):
        best_in_dict = max(profits, key=profits.get)
        return best_in_dict

    def find_best_takeprofit(self):
        best_in_dict = max(profits, key=profits.get)
        return best_in_dict

    def find_best_key_both(self):
        best_in_dict = max(profits)
        return best_in_dict

    # Click Functions
    def click_settings_button(self, wait):
        """click settings button."""
        try:
            wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        settings_icon,
                    )
                )
            )
            settings_button = self.driver.find_element_by_xpath(
                settings_icon
            )
            settings_button.click()
        except AttributeError:
            pass

    def close_existing_alert(self, wait):
        try:
            # wait.until(
            #     EC.visibility_of_element_located(
            #         (
            #             By.XPATH,
            #             "//*[@class='button-OYqjX7Sg apply-common-tooltip']",
            #         )
            #     )
            # )
            strategy = self.driver.find_element_by_xpath(
                "//*[@class='title-OYqjX7Sg mainTitle-OYqjX7Sg apply-overflow-tooltip withDot-OYqjX7Sg']"
            )
            strategy.click()
            cancel_button = self.driver.find_elements_by_xpath(
                "//*[@class='button-OYqjX7Sg apply-common-tooltip']"
            )[3]
            cancel_button.click()
        except AttributeError:
            pass

    def click_indicators(self, wait):
        """click settings button."""
        try:
            wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//*[@class='button-khcLBZEz apply-common-tooltip newStyles-khcLBZEz']",
                    )
                )
            )
            settings_button = self.driver.find_element_by_xpath(
                "//*[@class='button-khcLBZEz apply-common-tooltip newStyles-khcLBZEz']"
            )
            settings_button.click()
        except AttributeError:
            pass

    def click_favorite_indicator(self, wait):
        """click settings button."""
        try:
            wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//*[@class='item-4TFSfyGO']",
                    )
                )
            )
            settings_button = self.driver.find_element_by_xpath(
                "//*[@class='item-4TFSfyGO']"
            )
            settings_button.click()
        except AttributeError:
            pass

    def click_time_button(self, time, wait):
        """click settings button."""
        try:
            if time == '1s':
                num = 0
            elif time == '5s':
                num = 1
            elif time == '15s':
                num = 2
            elif time == '30s':
                num = 3
            elif time == '1m':
                num = 4
            elif time == '3m':
                num = 5
            elif time == '5m':
                num = 6
            elif time == '15m':
                num = 7
            elif time == '30m':
                num = 8
            elif time == '45m':
                num = 9
            elif time == '1hr':
                num = 10
            elif time == '2hr':
                num = 11
            elif time == '3hr':
                num = 12
            elif time == '4hr':
                num = 13
            else:
                num = None

            if num:
                wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.XPATH,
                            "//*[@class='menu-cXbh8Gcw button-khcLBZEz apply-common-tooltip newStyles-khcLBZEz']",
                        )
                    )
                )
                time_button = self.driver.find_element_by_xpath(
                    "//*[@class='menu-cXbh8Gcw button-khcLBZEz apply-common-tooltip newStyles-khcLBZEz']"
                )

                # time_button = self.driver.find_element_by_class_name('group-T57LDNqT newStyles-T57LDNqT')
                time_button.click()

                time_choose = self.driver.find_elements_by_xpath(
                    "//*[@class='labelRow-4TFSfyGO']"
                )[num]

            # dd = Select(time_choose)
            # dd.select_by_index(4)
            # time_choose = self.driver.find_element_by_name("30S")
            # print(time_choose)

            time_choose.click()

            # settings_button.click()
        except AttributeError:
            pass

    def click_new_time(self, wait):
        """click settings button."""
        try:
            wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//*[@class='item-4TFSfyGO']",
                    )
                )
            )
            settings_button = self.driver.find_element_by_xpath(
                "//*[@class='item-4TFSfyGO']"
            )
            settings_button.click()
        except AttributeError:
            pass

    def click_strategy_tester(self, wait):
        """check if strategy tester tab is active if not click to open tab."""
        try:
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[@class='titleText-YKxsrK2Q']")
                )
            )
            strategy_tester_tab = self.driver.find_elements_by_xpath(
                "//*[@class='titleText-YKxsrK2Q']"
            )
            for index, web_element in enumerate(strategy_tester_tab):
                if web_element.text == "Strategy Tester":
                    active_tab = strategy_tester_tab[index].get_attribute(
                        "data-active")
                    if active_tab == "false":
                        strategy_tester_tab[index].click()
                    break
        except (IndexError, NoSuchElementException, ElementNotInteractableException):
            print(
                "Could Not Click Strategy Tester Tab. Please Check web element XPATH."
            )

    def click_overview(self):
        try:
            strategy_tester_tab = self.driver.find_elements_by_xpath(
                "//*[@class='titleText-YKxsrK2Q']"
            )
            for index, web_element in enumerate(strategy_tester_tab):
                if web_element.text == "Strategy Tester":
                    active_tab = strategy_tester_tab[index].get_attribute(
                        "data-active")
                    if active_tab == "false":
                        strategy_tester_tab[index].click()
                        # time.sleep(.3)
                        overview = self.driver.find_element_by_class_name(
                            "report-tabs"
                        ).find_elements_by_tag_name("li")[0]
                        overview.click()
                    else:
                        overview = self.driver.find_element_by_class_name(
                            "report-tabs"
                        ).find_elements_by_tag_name("li")[0]
                        overview.click()
                    break
        except (IndexError, NoSuchElementException, ElementNotInteractableException):
            print(
                "Could Not Click Strategy Tester Tab. Please Check web element XPATH."
            )

    def click_performance_summary(self):
        """click performance summary tab."""
        try:
            strategy_tester_tab = self.driver.find_elements_by_xpath(
                "//*[@class='titleText-YKxsrK2Q']"
            )
            for index, web_element in enumerate(strategy_tester_tab):
                if web_element.text == "Strategy Tester":
                    active_tab = strategy_tester_tab[index].get_attribute(
                        "data-active")
                    if active_tab == "false":
                        strategy_tester_tab[index].click()
                        # time.sleep(.3)
                        performance_tab = self.driver.find_elements_by_class_name(
                            "report-tabs").find_elements_by_tag_name("li")[1]
                        performance_tab.click()
                    else:
                        performance_tab = self.driver.find_element_by_class_name(
                            "report-tabs").find_elements_by_tag_name("li")[1]
                        performance_tab.click()
                    break
        except (IndexError, NoSuchElementException, ElementNotInteractableException):
            print(
                "Could Not Click Strategy Tester Tab. Please Check web element XPATH."
            )

    def click_list_of_trades(self):
        """click list of trades tab."""
        try:
            strategy_tester_tab = self.driver.find_elements_by_xpath(
                "//*[@class='titleText-YKxsrK2Q']"
            )
            for index, web_element in enumerate(strategy_tester_tab):
                if web_element.text == "Strategy Tester":
                    active_tab = strategy_tester_tab[index].get_attribute(
                        "data-active")
                    if active_tab == "false":
                        strategy_tester_tab[index].click()
                        # time.sleep(.3)
                        list_of_trades = self.driver.find_element_by_class_name(
                            "report-tabs").find_elements_by_tag_name("li")[2]
                        list_of_trades.click()
                    else:
                        list_of_trades = self.driver.find_element_by_class_name(
                            "report-tabs").find_elements_by_tag_name("li")[2]
                        list_of_trades.click()
                    break
        except (IndexError, NoSuchElementException, ElementNotInteractableException):
            print(
                "Could Not Click Strategy Tester Tab. Please Check web element XPATH."
            )

    def click_long_stoploss_input(self, count, wait):
        """click long stoploss input."""
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, long_stopless_xpath)))
        stoploss_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath)[0]
        stoploss_input_box.send_keys(
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE)
        stoploss_input_box.send_keys(str(count))
        stoploss_input_box.send_keys(Keys.ENTER)
        time.sleep(.5)
        ok_button = self.driver.find_element_by_name("submit")
        ok_button.click()

    def click_long_takeprofit_input(self, count, wait):
        """click long take profit input."""
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, long_stopless_xpath)))
        takeprofit_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath)[1]
        takeprofit_input_box.send_keys(
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE)
        takeprofit_input_box.send_keys(str(count))
        takeprofit_input_box.send_keys(Keys.ENTER)
        time.sleep(.5)
        ok_button = self.driver.find_element_by_name("submit")
        ok_button.click()

    def click_short_stoploss_input(self, count, wait):
        """click short stoploss input."""
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, long_stopless_xpath)))
        stoploss_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath)[2]
        stoploss_input_box.send_keys(
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE)
        stoploss_input_box.send_keys(str(count))
        stoploss_input_box.send_keys(Keys.ENTER)
        time.sleep(.5)
        ok_button = self.driver.find_element_by_name("submit")
        ok_button.click()

    def click_short_takeprofit_input(self, count, wait):
        """click short take profit input."""
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, long_stopless_xpath)))
        stoploss_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath)[3]
        stoploss_input_box.send_keys(
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE)
        stoploss_input_box.send_keys(str(count))
        stoploss_input_box.send_keys(Keys.ENTER)
        time.sleep(.5)
        ok_button = self.driver.find_element_by_name("submit")
        ok_button.click()

    def click_long_inputs(
            self,
            long_stoploss_value,
            long_takeprofit_value,
            wait):
        """click both long inputs."""
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, long_stopless_xpath)))
        stoploss_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath)[0]
        takeprofit_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath)[1]
        stoploss_input_box.send_keys(
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE)
        stoploss_input_box.send_keys(str(long_stoploss_value))
        takeprofit_input_box.send_keys(
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE)
        takeprofit_input_box.send_keys(str(long_takeprofit_value))
        takeprofit_input_box.send_keys(Keys.ENTER)
        time.sleep(.5)
        ok_button = self.driver.find_element_by_name("submit")
        ok_button.click()

    def click_short_inputs(
            self,
            short_stoploss_value,
            short_takeprofit_value,
            wait):
        """click both short inputs."""
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, long_stopless_xpath)))
        stoploss_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath)[2]
        takeprofit_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath)[3]
        stoploss_input_box.send_keys(
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE)
        stoploss_input_box.send_keys(str(short_stoploss_value))
        takeprofit_input_box.send_keys(
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE +
            Keys.BACK_SPACE)
        takeprofit_input_box.send_keys(str(short_takeprofit_value))
        takeprofit_input_box.send_keys(Keys.ENTER)
        time.sleep(.5)
        ok_button = self.driver.find_element_by_name("submit")
        ok_button.click()

    def click_all_inputs(
            self,
            long_stoploss_value,
            long_takeprofit_value,
            short_stoploss_value,
            short_takeprofit_value,
            buy_factor,
            sell_factor,
            adx_smoothing,
            di_length,
            wait,
    ):
        """click short stoploss input."""
        # wait.until(EC.visibility_of_element_located(
        #     (By.XPATH, long_stopless_xpath)))
        time.sleep(0.3)
        long_stoploss_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath
        )[3]
        long_takeprofit_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath
        )[4]
        short_stoploss_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath
        )[5]
        short_takeprofit_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath
        )[6]

        buy_factor_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath
        )[13]
        sell_factor_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath
        )[14]
        adx_smoothing_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath
        )[15]
        di_length_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath
        )[16]

        long_stoploss_input_box.send_keys(Keys.BACK_SPACE * 8)
        long_stoploss_input_box.send_keys(str(long_stoploss_value))
        long_takeprofit_input_box.send_keys(Keys.BACK_SPACE * 8)
        long_takeprofit_input_box.send_keys(str(long_takeprofit_value))
        short_stoploss_input_box.send_keys(Keys.BACK_SPACE * 8)
        short_stoploss_input_box.send_keys(str(short_stoploss_value))
        short_takeprofit_input_box.send_keys(Keys.BACK_SPACE * 8)
        short_takeprofit_input_box.send_keys(str(short_takeprofit_value))
        # short_takeprofit_input_box.send_keys(Keys.ENTER)
        buy_factor_input_box.send_keys(Keys.BACK_SPACE * 8)
        buy_factor_input_box.send_keys(str(buy_factor))
        sell_factor_input_box.send_keys(Keys.BACK_SPACE * 8)
        sell_factor_input_box.send_keys(str(sell_factor))
        adx_smoothing_input_box.send_keys(Keys.BACK_SPACE * 8)
        adx_smoothing_input_box.send_keys(str(adx_smoothing))
        di_length_input_box.send_keys(Keys.BACK_SPACE * 8)
        di_length_input_box.send_keys(str(di_length))
        di_length_input_box.send_keys(Keys.ENTER)

        time.sleep(0.5)
        ok_button = self.driver.find_element_by_name("submit")
        ok_button.click()

    def click_properties_tab(self):
        """making sure the input tab is clicked."""
        try:
            time.sleep(0.3)
            input_tab = self.driver.find_elements_by_xpath(
                "//*[@class='tab-VabV7Fn8 withHover-VabV7Fn8 tab-rKFlMYkc']"
            )[0]
            # time.sleep(0.3)
            # if input_tab.get_attribute("data-value") == "properties":
            input_tab.click()

            time.sleep(0.3)
            order_button = self.driver.find_elements_by_xpath(
                "//*[@class='button-children-h8C3IU2n']"
            )[1]

            # time_button = self.driver.find_element_by_class_name('group-T57LDNqT newStyles-T57LDNqT')
            order_button.click()

            time.sleep(0.3)
            order_choose = self.driver.find_elements_by_xpath(
                "//*[@class='label-4TFSfyGO']"
            )[1]
            order_choose.click()

        except IndexError:
            pass

    def click_input_tab(self):
        """making sure the input tab is clicked."""
        try:
            input_tab = self.driver.find_elements_by_xpath(
                "//*[@class='tab-VabV7Fn8 withHover-VabV7Fn8 tab-rKFlMYkc']"
            )[0]
            if input_tab.get_attribute("data-value") == "inputs":
                input_tab.click()
        except IndexError:
            pass

    def click_ok_button(self):
        time.sleep(0.5)
        ok_button = self.driver.find_element_by_name("submit")
        ok_button.click()

    def click_enable_both_checkboxes(self):
        long_checkbox = self.driver.find_elements_by_xpath(
            "//*[@class='input-5Xd5conM']")[0]
        short_checkbox = self.driver.find_elements_by_xpath(
            "//*[@class='input-5Xd5conM']")[1]
        if not long_checkbox.get_attribute("checked"):
            click_long_checkbox = self.driver.find_elements_by_xpath(
                "//*[@class='box-5Xd5conM check-5Xd5conM']"
            )[0]
            click_long_checkbox.click()
        if not short_checkbox.get_attribute("checked"):
            click_short_checkbox = self.driver.find_elements_by_xpath(
                "//*[@class='box-5Xd5conM check-5Xd5conM']"
            )[1]
            click_short_checkbox.click()

    def click_enable_long_strategy_checkbox(self):
        long_checkbox = self.driver.find_elements_by_xpath(
            "//*[@class='input-5Xd5conM']")[0]
        short_checkbox = self.driver.find_elements_by_xpath(
            "//*[@class='icon-5Xd5conM']")[1]
        if not long_checkbox.get_attribute("checked"):
            click_long_checkbox = self.driver.find_elements_by_xpath(
                "//*[@class='box-5Xd5conM check-5Xd5conM']"
            )[0]
            click_long_checkbox.click()
        if short_checkbox.get_attribute("checked"):
            click_short_checkbox = self.driver.find_elements_by_xpath(
                "//*[@class='box-5Xd5conM check-5Xd5conM']"
            )[1]
            click_short_checkbox.click()

    def click_enable_short_strategy_checkbox(self):
        long_checkbox = self.driver.find_elements_by_xpath(
            "//*[@class='input-5Xd5conM']")[0]
        short_checkbox = self.driver.find_elements_by_xpath(
            "//*[@class='input-5Xd5conM']")[1]
        if long_checkbox.get_attribute("checked"):
            click_long_checkbox = self.driver.find_elements_by_xpath(
                "//*[@class='box-5Xd5conM check-5Xd5conM']"
            )[0]
            click_long_checkbox.click()
        if not short_checkbox.get_attribute("checked"):
            click_short_checkbox = self.driver.find_elements_by_xpath(
                "//*[@class='box-5Xd5conM check-5Xd5conM']"
            )[1]
            click_short_checkbox.click()

    def click_rest_all_inputs(self):
        """click short stoploss input."""
        long_stoploss_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath
        )[3]
        long_takeprofit_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath
        )[4]
        short_stoploss_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath
        )[5]
        short_takeprofit_input_box = self.driver.find_elements_by_xpath(
            long_stopless_xpath
        )[6]
        long_stoploss_input_box.send_keys(Keys.BACK_SPACE * 8)
        long_stoploss_input_box.send_keys(str("50"))
        long_takeprofit_input_box.send_keys(Keys.BACK_SPACE * 8)
        long_takeprofit_input_box.send_keys(str("50"))
        short_stoploss_input_box.send_keys(Keys.BACK_SPACE * 8)
        short_stoploss_input_box.send_keys(str("50"))
        short_takeprofit_input_box.send_keys(Keys.BACK_SPACE * 8)
        short_takeprofit_input_box.send_keys(str("50"))
        short_takeprofit_input_box.send_keys(Keys.ENTER)

    def save_strategy(self):
        strategy_inline = self.driver.find_element_by_xpath(
            "//*[@class='title-OYqjX7Sg mainTitle-OYqjX7Sg apply-overflow-tooltip withDot-OYqjX7Sg']"
        )
        strategy_inline.click()

        time.sleep(0.3)
        source_code = self.driver.find_elements_by_xpath(
            "//*[@class='button-OYqjX7Sg apply-common-tooltip']"
        )[2]
        source_code.click()

        time.sleep(0.3)
        save = self.driver.find_elements_by_xpath(
            "//*[@class='button-TuYnJRjv rightControlsBlock__button-TuYnJRjv button-9pA37sIi isInteractive-9pA37sIi newStyles-9pA37sIi']"
        )[0]
        save.click()

        time.sleep(0.3)
        strategy = self.driver.find_element_by_xpath(
            "//*[@class='js-bottom-backtesting-tab container-YKxsrK2Q']"
        )
        strategy.click()

    def set_new_alert(self, alert_message, wait):

        # First remove existing Alert(if any)
        try:
            old_alert = self.driver.find_element_by_class_name('name-vv1LOxY7')
            if old_alert.text == alert_message:
                # print('ALERT FOUND!!')
                action = ActionChains(self.driver)
                action.move_to_element(self.driver.find_element_by_class_name("name-vv1LOxY7")).perform();
                action.context_click().perform()
                time.sleep(0.3)
                remove_tab = self.driver.find_elements_by_xpath(
                    "//*[@class='label-tPYeYcJa']"
                )[3]
                remove_tab.click()
                time.sleep(0.3)
                accept = self.driver.find_element_by_xpath(
                    "//*[@class='actionButton-EGu7SRYD button-YKkCvwjV size-small-YKkCvwjV color-green-YKkCvwjV variant-primary-YKkCvwjV']"
                )
                accept.click();
        except:
            pass

        alert_tab = self.driver.find_elements_by_xpath(
            "//*[@class='button-Kbdz4qEM button-Rsu8YfBx withText-Rsu8YfBx button-9pA37sIi apply-common-tooltip isInteractive-9pA37sIi newStyles-9pA37sIi']"
        )[1]
        alert_tab.click()
        time.sleep(0.3)
        condition = self.driver.find_elements_by_xpath(
            "//*[@class='tv-control-select__caret js-dropdown-toggle']"
        )[0]
        condition.click()

        time.sleep(0.3)
        condition_select = self.driver.find_elements_by_xpath(
            "//*[@class='tv-control-select__option-wrap']"
        )[1]
        condition_select.click()

        time.sleep(0.3)
        sub_condition = self.driver.find_elements_by_xpath(
            "//*[@class='tv-control-select__control tv-dropdown-behavior__button']"
        )[1]
        sub_condition.click()

        time.sleep(0.3)
        sub_condition_select = self.driver.find_elements_by_xpath(
            "//*[@class='tv-dropdown-behavior__item tv-control-select__option']"
        )[2]
        sub_condition_select.click()

        # Rename alert
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@class='tv-control-input tv-control-input--size_small']")))

        alert_name = self.driver.find_elements_by_xpath(
            "//*[@class='tv-control-input tv-control-input--size_small']"
        )[1]
        alert_name.send_keys(Keys.BACK_SPACE * 150)
        alert_name.send_keys(alert_message)

        time.sleep(0.3)
        create = self.driver.find_element_by_xpath(
            "//*[@class='js-dialog__action-click js-dialog__no-drag tv-button tv-button--primary js-submit-button tv-button--loader']"
        )
        create.click()

        # notification handling
        try:
            time.sleep(0.3)
            notification = self.driver.find_element_by_xpath(
                "//*[@class='actionButton-EGu7SRYD button-YKkCvwjV size-small-YKkCvwjV color-brand-YKkCvwjV variant-primary-YKkCvwjV']"
            )
            notification.click()
        except:
            pass

        time.sleep(0.5)

    # Get Functions
    def get_net_all(
            self,
            long_stoploss_value,
            long_takeprofit_value,
            short_stoploss_value,
            short_takeprofit_value,
            buy_factor,
            sell_factor,
            adx_smoothing,
            di_length,
            wait,
    ):
        wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "additional_percent_value")))
        try:
            check = self.driver.find_elements_by_class_name(
                "additional_percent_value")[0]
            check.find_element_by_xpath('./span[contains(@class, "neg")]')
            negative = True
        except NoSuchElementException:
            negative = False
        if negative:
            net_profit = self.driver.find_elements_by_class_name(
                "additional_percent_value"
            )[0].text.split(" %")
            # net_value = -float(net_profit[0])
            net_value = -float(re.sub(r'[^\x00-\x7F]+', '-', net_profit[0]))
            profits.update(
                {
                    -net_value: [
                        "Long Stoploss:",
                        long_stoploss_value,
                        "Long Take Profit:",
                        long_takeprofit_value,
                        "Short Stoploss:",
                        short_stoploss_value,
                        "Short Take Profit:",
                        short_takeprofit_value,
                    ]
                }
            )
            print(
                colored(
                    f"Net Profit: -{net_value}% --> Long Stoploss: {long_stoploss_value}, Long Take Profit: {long_takeprofit_value}, Short Stoploss: {short_stoploss_value}, Short Take Profit: {short_takeprofit_value}, Buy Factor:{buy_factor}, Sell Factor:{sell_factor}, ADX Smoothing:{adx_smoothing}, DI Length:{di_length}",
                    "red",
                )
            )
        else:
            net_profit = self.driver.find_elements_by_class_name(
                "additional_percent_value"
            )[0].text.split(" %")
            # net_value = float(net_profit[0])
            net_value = float(re.sub(r'[^\x00-\x7F]+', '-', net_profit[0]))
            profits.update(
                {
                    net_value: [
                        "Long Stoploss:",
                        long_stoploss_value,
                        "Long Take Profit:",
                        long_takeprofit_value,
                        "Short Stoploss:",
                        short_stoploss_value,
                        "Short Take Profit:",
                        short_takeprofit_value,
                    ]
                }
            )
            print(
                colored(
                    f"Net Profit: {net_value}% --> Long Stoploss: {long_stoploss_value}, Long Take Profit: {long_takeprofit_value}, Short Stoploss: {short_stoploss_value}, Short Take Profit: {short_takeprofit_value}, Buy Factor:{buy_factor}, Sell Factor:{sell_factor}, ADX Smoothing:{adx_smoothing}, DI Length:{di_length}",
                    "green",
                )
            )
        return net_profit

    def get_net_both(self, stoploss_value, takeprofit_value, wait):
        wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "additional_percent_value")))
        try:
            time.sleep(0.5)
            check = self.driver.find_elements_by_class_name(
                "additional_percent_value")[0]
            check.find_element_by_xpath('./span[contains(@class, "neg")]')
            negative = True
        except NoSuchElementException:
            negative = False

        if negative:
            net_profit = self.driver.find_elements_by_class_name(
                "additional_percent_value"
            )[0].text.split(" %")
            net_value = -float(re.sub(r'[^\x00-\x7F]+', '-', net_profit[0]))
            profits.update(
                {
                    -net_value: [
                        "Stoploss:",
                        stoploss_value,
                        "Take Profit:",
                        takeprofit_value,
                    ]
                }
            )
            print(
                colored(
                    f"Net Profit: -{net_value}% --> Stoploss: {stoploss_value}, Take Profit: {takeprofit_value}",
                    "red",
                ))
        else:
            net_profit = self.driver.find_elements_by_class_name(
                "additional_percent_value"
            )[0].text.split(" %")
            # net_value = float(net_profit[0])
            net_value = float(re.sub(r'[^\x00-\x7F]+', '-', net_profit[0]))
            profits.update(
                {net_value: ["Stoploss:", stoploss_value, "Take Profit:", takeprofit_value]}
            )
            print(
                colored(
                    f"Net Profit: {net_value}% --> Stoploss: {stoploss_value}, Take Profit: {takeprofit_value}",
                    "green",
                ))
        return net_profit

    def get_net_profit_stoploss(self, count, wait):
        wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "additional_percent_value")))
        try:
            time.sleep(0.5)
            check = self.driver.find_elements_by_class_name(
                "additional_percent_value")[0]
            check.find_element_by_xpath('./span[contains(@class, "neg")]')
            negative = True
        except NoSuchElementException:
            negative = False

        if negative:
            net_profit = self.driver.find_elements_by_class_name(
                "additional_percent_value"
            )[0].text.split(" %")
            # net_value = -float(net_profit[0])
            net_value = -float(re.sub(r'[^\x00-\x7F]+', '-', net_profit[0]))
            profits.update({count: -net_value})
            print(
                colored(
                    f"Stoploss: {count}%, Net Profit: {net_value}%",
                    "red"))
        else:
            net_profit = self.driver.find_elements_by_class_name(
                "additional_percent_value"
            )[0].text.split(" %")
            # net_value = float(net_profit[0])
            net_value = float(re.sub(r'[^\x00-\x7F]+', '-', net_profit[0]))
            profits.update({count: net_value})
            print(
                colored(
                    f"Stoploss: {count}%, Net Profit: {net_value}%",
                    "green"))
        return net_profit

    def get_net_profit_takeprofit(self, count, wait):
        try:
            wait.until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "additional_percent_value")
                )
            )
            time.sleep(0.5)
            check = self.driver.find_elements_by_class_name(
                "additional_percent_value")[0]
            check.find_element_by_xpath('./span[contains(@class, "neg")]')
            negative = True
        except (NoSuchElementException, IndexError):
            negative = False

        if negative:
            net_profit = self.driver.find_elements_by_class_name(
                "additional_percent_value"
            )[0].text.split(" %")
            # net_value = -float(net_profit[0])
            net_value = -float(re.sub(r'[^\x00-\x7F]+', '-', net_profit[0]))
            profits.update({count: -net_value})
            print(
                colored(
                    f"Take Profit: {count}%, Net Profit: {net_value}%",
                    "red"))
        else:
            net_profit = self.driver.find_elements_by_class_name(
                "additional_percent_value"
            )[0].text.split(" %")
            # net_value = float(net_profit[0])
            net_value = float(re.sub(r'[^\x00-\x7F]+', '-', net_profit[0]))
            profits.update({count: net_value})
            print(
                colored(
                    f"Take Profit: {count}%, Net Profit: {net_value}%",
                    "green"))
        return net_profit

    def get_win_rate(self, count, wait):
        wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "additional_percent_value")))
        try:
            win_rate = self.driver.find_elements_by_class_name(
                "additional_percent_value")[1]
            win_rate.find_element_by_xpath('./span[contains(@class, "neg")]')
            negative = True
        except NoSuchElementException:
            negative = False

        if negative:
            win_rate = self.driver.find_elements_by_class_name(
                "additional_percent_value")[1].text.split(" %")
            # net_value = float(win_rate[0])
            net_value = float(re.sub(r'[^\x00-\x7F]+', '-', win_rate[0]))
            profits.update({count: -net_value})
            negative_color = {count: net_value}
            print(colored(f"{negative_color}", "red"))
        else:
            win_rate = self.driver.find_elements_by_class_name(
                "additional_percent_value")[1].text.split(" %")
            # net_value = float(win_rate[0])
            net_value = float(re.sub(r'[^\x00-\x7F]+', '-', win_rate[0]))
            profits.update({count: net_value})
            positive_color = {count: net_value}
            print(colored(f"{positive_color}", "green"))
        return win_rate

    # Show Me Functions
    def print_best_stoploss(self):
        try:
            best_stoploss = max(profits, key=profits.get)
            max_percentage = profits[best_stoploss]
            if max_percentage > 0:
                profitable = colored(str(best_stoploss) + " %", 'green')
                print(f"Best Stoploss: " + str(profitable))
            else:
                profitable = colored(str(best_stoploss) + " %", 'red')
                print(f"Best Stoploss: " + str(profitable))
        except (UnboundLocalError, ValueError):
            print("error printing stoploss.")

    def print_best_takeprofit(self):
        try:
            best_takeprofit = max(profits, key=profits.get)
            max_percentage = profits[best_takeprofit]
            if max_percentage > 0:
                profitable = colored(str(best_takeprofit) + " %", 'green')
                print(f"Best Take Profit: " + str(profitable))
            else:
                profitable = colored(str(best_takeprofit) + " %", 'red')
                print(f"Best Take Profit: " + str(profitable))
        except (UnboundLocalError, ValueError):
            print("error printing take profit.")

    def print_best_both(self):
        try:
            best_key = self.find_best_key_both()
            best_stoploss = profits[best_key][1]
            best_takeprofit = profits[best_key][3]
            print(f"Best Stop Loss: {best_stoploss}")
            print(f"Best Take Profit: {best_takeprofit}\n")
        except (UnboundLocalError, ValueError):
            print("error printing stoploss.")

    def print_best_all(self):
        try:
            best_key = self.find_best_key_both()
            best_long_stoploss = profits[best_key][1]
            best_long_takeprofit = profits[best_key][3]
            best_short_stoploss = profits[best_key][5]
            best_short_takeprofit = profits[best_key][7]
            print(f"Best Long Stop Loss: {best_long_stoploss}")
            print(f"Best Long Take Profit: {best_long_takeprofit}")
            print(f"Best Short Stop Loss: {best_short_stoploss}")
            print(f"Best Short Take Profit: {best_short_takeprofit}\n")
        except (UnboundLocalError, ValueError):
            print("error printing stoploss.")

    def print_net_profit(self):
        net_profit = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[0]
                .find_element_by_class_name("additional_percent_value")
        )
        try:
            negative = net_profit.find_element_by_class_name("neg")
            if negative:
                display = colored(f"{net_profit.text}", "red")
                print(f"Net Profit: {display}")
        except NoSuchElementException:
            display = colored(f"{net_profit.text}", "green")
            print(f"Net Profit: {display}")

    def print_gross_profit(self):
        gross_profit = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[1]
                .find_element_by_class_name("additional_percent_value")
        )
        try:
            negative = gross_profit.find_element_by_class_name("neg")
            if negative:
                display = colored(f"{gross_profit.text}", "red")
                print(f"Gross Profit: {display}")
        except NoSuchElementException:
            display = colored(f"{gross_profit.text}", "green")
            print(f"Gross Profit: {display}")

    def print_gross_loss(self):
        gross_loss = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[2]
                .find_element_by_class_name("additional_percent_value")
        )
        try:
            negative = gross_loss.find_element_by_class_name("neg")
            if negative:
                display = colored(f"{gross_loss.text}", "red")
                print(f"Gross Loss: {display}")
        except NoSuchElementException:
            display = colored(f"{gross_loss.text}", "green")
            print(f"Gross Loss: {display}")

    def print_max_drawdown(self):
        max_drawdown = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[3]
                .find_element_by_class_name("additional_percent_value")
        )

        try:
            negative = max_drawdown.find_element_by_class_name("neg")
            if negative:
                display = colored(f'{max_drawdown.text}', 'red')
                print(f'Max Drawdown: {display}')
        except NoSuchElementException:
            display = colored(f'{max_drawdown.text}', 'green')
            print(f'Max Drawdown: {display}')

    def print_buy_and_hold_return(self):
        buy_and_hold_return = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[4]
                .find_element_by_class_name("additional_percent_value")
        )

        try:
            negative = buy_and_hold_return.find_element_by_class_name("neg")
            if negative:
                display = colored(f'{buy_and_hold_return.text}', 'red')
                print(f'Buy & Hold Return: {display}')
        except NoSuchElementException:
            display = colored(f'{buy_and_hold_return.text}', 'green')
            print(f'Buy & Hold Return: {display}')

    def print_sharpe_ratio(self):
        try:
            negative = (
                self.driver.find_element_by_class_name("report-data")
                    .find_element_by_tag_name("table")
                    .find_element_by_tag_name("tbody")
                    .find_elements_by_tag_name("tr")[5]
                    .find_elements_by_tag_name("td")[1]
                    .find_element_by_class_name("neg")
            )
            if negative:
                display = colored(f"{negative.text}", "red")
                print(f"Sharpe Ratio: {display}")
        except NoSuchElementException:
            sharpe_ratio = (
                self.driver.find_element_by_class_name("report-data")
                    .find_element_by_tag_name("table")
                    .find_element_by_tag_name("tbody")
                    .find_elements_by_tag_name("tr")[5]
                    .find_elements_by_tag_name("td")[1]
            )
            display = colored(f"{sharpe_ratio.text}", "green")
            print(f"Sharpe Ratio: {display}")

    def print_sortino_ratio(self):
        try:
            negative = (
                self.driver.find_element_by_class_name("report-data")
                    .find_element_by_tag_name("table")
                    .find_element_by_tag_name("tbody")
                    .find_elements_by_tag_name("tr")[6]
                    .find_elements_by_tag_name("td")[1]
                    .find_element_by_class_name("neg")
            )
            if negative:
                display = colored(f"{negative.text}", "red")
                print(f"Sortino Ratio: {display}")
        except NoSuchElementException:
            sortino_ratio = (
                self.driver.find_element_by_class_name("report-data")
                    .find_element_by_tag_name("table")
                    .find_element_by_tag_name("tbody")
                    .find_elements_by_tag_name("tr")[6]
                    .find_elements_by_tag_name("td")[1]
            )
            display = colored(f"{sortino_ratio.text}", "green")
            print(f"Sortino Ratio: {display}")

    def print_profit_factor(self):
        profit_factor = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[7]
                .find_elements_by_tag_name("td")[1]
        )
        try:
            negative = profit_factor.find_element_by_class_name("neg")
            if negative:
                display = colored(f"{profit_factor.text}", "red")
                print(f"Profit Factor: {display}")
        except NoSuchElementException:
            display = colored(f"{profit_factor.text}", "green")
            print(f"Profit Factor: {display}")

    def print_max_contracts_held(self):
        max_contracts_held = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[8]
                .find_elements_by_tag_name("td")[1]
        )
        try:
            negative = max_contracts_held.find_element_by_class_name("neg")
            if negative:
                display = colored(f"{max_contracts_held.text}", "red")
                print(f"Max Contracts Held: {display}")
        except NoSuchElementException:
            display = colored(f"{max_contracts_held.text}", "green")
            print(f"Max Contracts Held: {display}")

    def print_open_pl(self):
        open_pl = (
            self.driver.find_element_by_class_name("report-data")
            .find_element_by_tag_name("table")
            .find_element_by_tag_name("tbody")
            .find_elements_by_tag_name("tr")[9]
            .find_element_by_class_name("additional_percent_value")
        )
        try:
            negative = open_pl.find_element_by_class_name("neg")
            if negative:
                display = colored(f"{open_pl.text}", "red")
                print(f"Open PL: {display}")
        except NoSuchElementException:
            display = colored(f"{open_pl.text}", "green")
            print(f"Open PL: {display}")

    def print_commission_paid(self):
        commission_paid = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[10]
                .find_elements_by_tag_name("td")[1]
        )
        print(f"Commission Paid: {commission_paid.text}")

    def print_total_closed_trades(self):
        total_closed_trades = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[11]
                .find_elements_by_tag_name("td")[1]
        )
        print(f"Total Closed Trades: {total_closed_trades.text}")

    def print_total_open_trades(self):
        total_open_trades = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[12]
                .find_elements_by_tag_name("td")[1]
        )
        print(f"Total Open Trades: {total_open_trades.text}")

    def print_number_winning_trades(self):
        number_winning_trades = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[13]
                .find_elements_by_tag_name("td")[1]
        )
        print(f"Number Winning Trades: {number_winning_trades.text}")

    def print_number_losing_trades(self):
        number_losing_trades = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[14]
                .find_elements_by_tag_name("td")[1]
        )
        print(f"Number Losing Trades: {number_losing_trades.text}")

    def print_percent_profitable(self):
        percent_profitable = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[15]
                .find_elements_by_tag_name("td")[1]
        )
        print(f"Percent Profitable: {percent_profitable.text}")

    def print_avg_trade(self):
        avg_trade = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[16]
                .find_element_by_class_name("additional_percent_value")
        )
        try:
            negative = avg_trade.find_element_by_class_name("neg")
            if negative:
                display = colored(f"{avg_trade.text}", "red")
                print(f"Avg Trade: {display}")
        except NoSuchElementException:
            display = colored(f"{avg_trade.text}", "green")
            print(f"Avg Trade: {display}")

    def print_avg_win_trade(self):
        try:
            negative = (
                self.driver.find_element_by_class_name("report-data")
                    .find_element_by_tag_name("table")
                    .find_element_by_tag_name("tbody")
                    .find_elements_by_tag_name("tr")[17]
                    .find_element_by_class_name("additional_percent_value")
                    .find_element_by_class_name("neg")
            )
            if negative:
                display = colored(f"{negative.text}", "red")
                print(f"Avg Win Trade: {display}")
        except NoSuchElementException:
            avg_win_trade = (
                self.driver.find_element_by_class_name("report-data")
                    .find_element_by_tag_name("table")
                    .find_element_by_tag_name("tbody")
                    .find_elements_by_tag_name("tr")[17]
                    .find_element_by_class_name("additional_percent_value")
            )
            display = colored(f"{avg_win_trade.text}", "green")
            print(f"Avg Win Trade: {display}")

    def print_avg_loss_trade(self):
        avg_loss_trade = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[18]
                .find_element_by_class_name("additional_percent_value")
        )
        try:
            negative = avg_loss_trade.find_element_by_class_name("neg")
            if negative:
                display = colored(f"{avg_loss_trade.text}", "red")
                print(f"Avg Loss Trade: {display}")
        except NoSuchElementException:
            display = colored(f"{avg_loss_trade.text}", "green")
            print(f"Avg Loss Trade: {display}")

    def print_win_loss_ratio(self):
        win_loss_ratio = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[19]
                .find_elements_by_tag_name("td")[1]
        )
        print(f"Win/Loss Ratio: {win_loss_ratio.text}")

    def print_largest_winning_trade(self):
        largest_winning_trade = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[20]
                .find_element_by_class_name("additional_percent_value")
        )
        try:
            negative = largest_winning_trade.find_element_by_class_name("neg")
            if negative:
                display = colored(f"{largest_winning_trade.text}", "red")
                print(f"Largest Win Trade: {display}")
        except NoSuchElementException:
            display = colored(f"{largest_winning_trade.text}", "green")
            print(f"Largest Win Trade: {display}")

    def print_largest_losing_trade(self):
        largest_losing_trade = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[21]
                .find_element_by_class_name("additional_percent_value")
        )
        try:
            negative = largest_losing_trade.find_element_by_class_name("neg")
            if negative:
                display = colored(f"{largest_losing_trade.text}", "red")
                print(f"Largest Loss Trade: {display}")
        except NoSuchElementException:
            display = colored(f"{largest_losing_trade.text}", "green")
            print(f"Largest Loss Trade: {display}")

    def print_avg_bars_in_trades(self):
        avg_bars_in_trades = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[22]
                .find_elements_by_tag_name("td")[1]
        )
        print(f"Avg Bars In Trades: {avg_bars_in_trades.text}")

    def print_avg_bars_in_winning_trades(self):
        avg_bars_in_winning_trades = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[23]
                .find_elements_by_tag_name("td")[1]
        )
        print(f"Avg Bars In Winning Trades: {avg_bars_in_winning_trades.text}")

    def print_avg_bars_in_losing_trades(self):
        avg_bars_in_losing_trades = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[24]
                .find_elements_by_tag_name("td")[1]
        )
        print(f"Avg Bars In Losing Trades: {avg_bars_in_losing_trades.text}")

    def print_margin_calls(self):
        margin_calls = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[25]
                .find_elements_by_tag_name("td")[1]
        )
        print(f"Avg Bars In Losing Trades: {margin_calls.text}")

    def print_win_rate(self):
        win_rate = (
            self.driver.find_element_by_class_name("report-data")
                .find_element_by_tag_name("table")
                .find_element_by_tag_name("tbody")
                .find_elements_by_tag_name("tr")[15]
                .find_elements_by_tag_name("td")[1]
        )
        print(f"Win Rate: {win_rate.text}")
