from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import chromedriver_autoinstaller
import pandas as pd
import time
import re


def scrape_starlink():

    chromedriver_autoinstaller.install()

    chrome_options = Options()

    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )

    chrome_options.add_argument(
        "--start-maximized"
    )

    # Suppress Chrome internal logs (harmless but noisy)
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--silent")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(
        options=chrome_options
    )

    actions = ActionChains(driver)

    try:

        # OPEN STARLINK
        driver.get(
            "https://www.starlink.com"
        )

        print("=" * 60)
        print("STARLINK LOGIN")
        print("=" * 60)

        input(
            "\n1. Login to Starlink\n"
            "2. Open the Usage Dashboard\n"
            "3. Make sure you can see the usage graph\n"
            "4. Press ENTER here to start scraping\n\n"
        )

        time.sleep(3)

        print("\nCURRENT PAGE:")
        print(driver.current_url)
        print(driver.title)

        all_data = []

        # Adjust if Starlink changes labels
        month_tabs = [
            "Nov",
            "Dec",
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ]

        buttons = driver.find_elements(
            By.TAG_NAME,
            "button"
        )

        print("\nFOUND BUTTONS:")

        for btn in buttons:

            try:
                print(btn.text)
            except:
                pass

        for button in buttons:

            try:

                month_text = button.text.strip()

                if month_text not in month_tabs:
                    continue

                print(
                    f"\nSCRAPING MONTH: {month_text}"
                )

                driver.execute_script(
                    "arguments[0].click();",
                    button
                )

                time.sleep(3)

                bars = driver.find_elements(
                    By.CSS_SELECTOR,
                    "svg rect"
                )

                print(
                    f"BARS FOUND: {len(bars)}"
                )

                for i in range(len(bars)):

                    try:

                        bars = driver.find_elements(
                            By.CSS_SELECTOR,
                            "svg rect"
                        )

                        if i >= len(bars):
                            break

                        bar = bars[i]

                        driver.execute_script(
                            "arguments[0].scrollIntoView();",
                            bar
                        )

                        actions.move_to_element(
                            bar
                        ).perform()

                        time.sleep(1)

                        tooltips = driver.find_elements(
                            By.CSS_SELECTOR,
                            "div"
                        )

                        for tooltip in tooltips:

                            text = tooltip.text.strip()

                            if "GB" not in text:
                                continue

                            lines = text.split("\n")

                            if len(lines) < 2:
                                continue

                            date = lines[0].strip()

                            usage_line = lines[-1].strip()

                            date_pattern = (
                                r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2}$"
                            )

                            if not re.match(
                                date_pattern,
                                date
                            ):
                                continue

                            usage_match = re.search(
                                r"\d+(\.\d+)?",
                                usage_line
                            )

                            if not usage_match:
                                continue

                            usage = float(
                                usage_match.group()
                            )

                            if usage <= 0:
                                continue

                            entry = {
                                "Date": date,
                                "Data Usage (GB)": usage
                            }

                            if entry not in all_data:

                                all_data.append(
                                    entry
                                )

                                print(entry)

                    except Exception as e:

                        print(
                            "BAR ERROR:",
                            str(e)
                        )

            except Exception as e:

                print(
                    "MONTH ERROR:",
                    str(e)
                )

        driver.quit()

        df = pd.DataFrame(
            all_data
        )

        if len(df) > 0:

            df = df.drop_duplicates()

            df.to_csv(
                "starlink_usage.csv",
                index=False
            )

            print(
                "\nCSV SAVED SUCCESSFULLY"
            )

        else:

            print(
                "\nNO DATA FOUND"
            )

        return df

    except Exception as e:

        print(
            "\nSCRAPER ERROR:",
            str(e)
        )

        driver.quit()

        return pd.DataFrame()


if __name__ == "__main__":

    df = scrape_starlink()

    print(df.head())