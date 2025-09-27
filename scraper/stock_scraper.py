"""
Stock Scraper for Yahoo Finance - Most Active Stocks

Author: Your Name
Description:
    - Scrapes Yahoo Finance "Most Active" stocks using Selenium
    - Cleans the scraped data with Pandas
    - Saves the result into a CSV file
"""

from time import sleep
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class StockScraper:
    def __init__(self, driver, timeout=10):
        """
        Initialize StockScraper
        :param driver: Selenium WebDriver instance
        :param timeout: wait timeout in seconds
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.data = []

    def wait_for_page_load(self):
        """Wait until the <body> is available (faster than waiting full page with ads)"""
        try:
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        except Exception as e:
            print(f"The page did not load within the given time: {e}")
        else:
            print("Page loaded successfully")

    def access_url(self, url):
        """Navigate to a URL and wait for the body to load"""
        self.driver.get(url)
        self.wait_for_page_load()

    def most_active_stocks(self):
        """Navigate through the menu → Trending Tickers → Most Active"""
        action = ActionChains(self.driver)

        # Hover over "Markets" menu
        market_menu = self.wait.until(
            EC.element_to_be_clickable((By.XPATH,
                "/html/body/div[2]/header/div/div/div/div[4]/div/div/ul/li[3]/a/span"))
        )
        action.move_to_element(market_menu).perform()

        # Click on "Trending Tickers"
        trending_tickers = self.wait.until(
            EC.element_to_be_clickable((By.XPATH,
                "/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/ul[1]/li[3]/div[1]/ul[1]/li[4]/a[1]/div[1]"))
        )
        trending_tickers.click()
        self.wait_for_page_load()

        # Click on "Most Active"
        most_active = self.wait.until(
            EC.element_to_be_clickable((By.XPATH,
                '//*[@id="main-content-wrapper"]/section[1]/div/nav/ul/li[1]/a/span'))
        )
        most_active.click()
        self.wait_for_page_load()

    def extract_stock_data(self):
        """Scrape stock data from the Most Active table across all pages"""
        while True:
            # Wait for table rows
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody tr")))
            rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

            # Extract data row by row
            for row in rows:
                value = row.find_elements(By.TAG_NAME, "td")
                stock_data = {
                    "Symbol": value[0].text,
                    "Name": value[1].text,
                    "Price(usd)": value[3].text,
                    "Change": value[4].text,
                    "Volume": value[6].text,
                    "Market Cap": value[8].text,
                    "PE Ratio": value[9].text,
                }
                self.data.append(stock_data)

            # Try clicking "Next Page"
            try:
                next_page = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH,
                        "/html[1]/body[1]/div[2]/main[1]/section[1]/section[1]/section[1]/section[1]/section[1]/div[1]/div[3]/div[3]/button[3]/div[1]/*[name()='svg'][1]"))
                )
                next_page.click()
                sleep(2)
            except:
                print("No more pages to navigate")
                break

    def clean_and_save_data(self, filename):
        """Clean scraped data and save to CSV"""
        df = pd.DataFrame(self.data)

        # Strip whitespace from string columns
        df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

        # Clean numeric columns
        df["Price_usd"] = pd.to_numeric(df["Price(usd)"].str.replace(",", ""), errors="coerce")
        df["Change"] = pd.to_numeric(df["Change"].str.replace("+", "").str.replace(",", ""), errors="coerce")
        df["Volume"] = pd.to_numeric(df["Volume"].str.replace("M", ""), errors="coerce")
        df["PE_Ratio"] = pd.to_numeric(
            df['PE Ratio'].replace(['--', 'N/A', ''], np.nan).astype(str).str.replace(",", ""),
            errors='coerce'
        )

        # Rename columns for clarity
        df = df.rename(columns={"Volume": "Volume_M"})

        # Save to CSV
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")


if __name__ == "__main__":
    # Set Chrome options for faster loading
    chrome_options = Options()
    chrome_options.page_load_strategy = "eager"  

    driver = webdriver.Chrome(options=chrome_options, service=Service())
    driver.maximize_window()
    scraper = StockScraper(driver, timeout=10)

    scraper.access_url("https://finance.yahoo.com/")
    scraper.most_active_stocks()
    scraper.extract_stock_data()
    scraper.clean_and_save_data(filename="most_active_stocks.csv")

    driver.quit()
