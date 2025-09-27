# Yahoo Finance Most Active Stocks Scraper

A Python-based web scraper that extracts the **most active stocks** from Yahoo Finance, cleans the data, and saves it as a CSV file. Built using **Selenium** for web scraping and **Pandas** for data cleaning.

---

## Features

- Scrapes **most active stocks** from Yahoo Finance.
- Cleans and formats the data (numeric conversion, removing unwanted characters).
- Handles multiple pages of stock data.
- Saves results into a **CSV file** in the `data/` folder.
- Fully automated using **Selenium**.
- Includes a **video demo** of the scraper.

---

## Tech Stack

- **Python 3.10+**
- **Selenium**: Browser automation
- **Pandas**: Data cleaning & manipulation
- **NumPy**: Handling missing values
- **Chrome WebDriver**: To control the Chrome browser

---

## Project Structure

yahoo_finance_scraper/
│
├── scraper/
│ ├── init.py
│ └── stock_scraper.py # Main scraper class
│
├── data/ # Folder to store scraped CSV files
│ └── most_active_stocks.csv
│
├── demo/ # Video demonstration of the scraper
│ └── demo_run.mp4
│
├── requirements.txt # Python dependencies
├── README.md # Project documentation

yaml
Copy code

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/yahoo_finance_scraper.git
cd yahoo_finance_scraper```

2.**Create a virtual environment (optional but recommended)**

```bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate```

3.**Install dependencies**

```bash
Copy code
pip install -r requirements.txt```
4.**Download ChromeDriver**

Make sure the version matches your Chrome browser.

Add it to your system PATH or place it in the project directory.

Usage
Run the scraper:

```bash
Copy code
python scraper/stock_scraper.py```

The script will open Chrome, navigate to Yahoo Finance, scrape the most active stocks, clean the data, and save it to data/most_active_stocks.csv.

Check the video demo in the demo/ folder.

Output
The CSV file will contain the following columns:

Column	Description
Symbol	Stock symbol
Name	Company name
Price_usd	Current stock price in USD
Change	Price change
Volume_M	Trading volume (in millions)
Market Cap	Market capitalization
PE_Ratio	Price-to-Earnings ratio

Contributing
1.Fork the repository

2.Create a branch (git checkout -b feature/your-feature)

3.Commit your changes (git commit -m "Add feature")

4.Push to the branch (git push origin feature/your-feature)

5.Open a Pull Request

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Your Name

GitHub: yourusername

Email: your.email@example.com

Demo
You can view the scraper in action in the demo/demo_run.mp4 file.

pgsql
Copy code

✅ This is fully Markdown-ready, and it looks professional on GitHub.  

If you want, I can **also create a `.gitignore`** specifically for this setup so that the `__pycache__`, ChromeDriver, and possibly large video files are handled correctly.  

Do you want me to create that `.gitignore` too?
