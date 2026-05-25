from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import time
import re


def scrape_starlink():

    # CHROME OPTIONS
    chrome_options = Options()

    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )

    chrome_options.add_argument("--start-maximized")

    # START DRIVER
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    actions = ActionChains(driver)

    # OPEN STARLINK
    driver.get("https://www.starlink.com")

    print("LOGIN MANUALLY")

    # WAIT FOR LOGIN
    time.sleep(60)

    # OPEN USAGE PAGE
    driver.get(
        "https://starlink.com/account/service-line/AST-2293597-46342-54?selectedDevice=ut01000000-00000000-0060d786&page=0&limit=5"
    )

    # WAIT PAGE LOAD
    time.sleep(10)

    all_data = []

    # MONTH TABS
    month_tabs = [
        "Nov",
        "Dec",
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May - Jun"
    ]

    # FIND BUTTONS
    buttons = driver.find_elements(By.TAG_NAME, "button")

    # LOOP MONTH TABS
    for button in buttons:

        try:

            month_text = button.text.strip()

            if month_text in month_tabs:

                print(f"\nCLICKING MONTH: {month_text}")

                # CLICK TAB
                driver.execute_script(
                    "arguments[0].click();",
                    button
                )

                time.sleep(3)

                # REFRESH BARS
                bars = driver.find_elements(
                    By.CSS_SELECTOR,
                    "svg rect"
                )

                print("BARS FOUND:", len(bars))

                # LOOP THROUGH BARS
                for i in range(len(bars)):

                    try:

                        # REFRESH BARS EACH LOOP
                        bars = driver.find_elements(
                            By.CSS_SELECTOR,
                            "svg rect"
                        )

                        # PREVENT INDEX ERROR
                        if i >= len(bars):
                            break

                        bar = bars[i]

                        # SCROLL TO BAR
                        driver.execute_script(
                            "arguments[0].scrollIntoView();",
                            bar
                        )

                        # HOVER BAR
                        actions.move_to_element(
                            bar
                        ).pause(1).perform()

                        time.sleep(1)

                        # GET TOOLTIP DIVS
                        tooltips = driver.find_elements(
                            By.CSS_SELECTOR,
                            "div"
                        )

                        for tooltip in tooltips:

                            tooltip_text = tooltip.text.strip()

                            # MUST CONTAIN GB
                            if "GB" not in tooltip_text:
                                continue

                            lines = tooltip_text.split("\n")

                            # NEED DATE + VALUE
                            if len(lines) < 2:
                                continue

                            date = lines[0].strip()
                            usage_line = lines[-1].strip()

                            # VALID DATE
                            date_pattern = r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2}$"

                            if not re.match(
                                date_pattern,
                                date
                            ):
                                continue

                            # EXTRACT NUMBER
                            usage_match = re.search(
                                r"\d+(\.\d+)?",
                                usage_line
                            )

                            if not usage_match:
                                continue

                            usage = float(
                                usage_match.group()
                            )

                            # REMOVE 0 VALUES
                            if usage == 0:
                                continue

                            entry = {
                                "Date": date,
                                "Data Usage (GB)": usage
                            }

                            # REMOVE DUPLICATES
                            if entry not in all_data:

                                all_data.append(entry)

                                print(entry)

                    except Exception as e:
                        print("BAR ERROR:", e)

        except Exception as e:
            print("MONTH ERROR:", e)

    # CLOSE DRIVER
    driver.quit()

    # CREATE DATAFRAME
    df = pd.DataFrame(all_data)

    # REMOVE DUPLICATES
    df = df.drop_duplicates()

    # SORT DATA
    df = df.sort_values(by="Date")

    # SAVE CSV
    df.to_csv(
        "starlink_usage.csv",
        index=False
    )

    print("\nCSV SAVED SUCCESSFULLY")

    return df