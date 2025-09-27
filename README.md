# 📈 Yahoo Finance Most Active Stocks Scraper

A Python scraper to extract **Most Active Stocks** data from Yahoo Finance using **Selenium** and **Pandas**.  
Cleans the scraped data and saves it into a CSV file for further analysis.

---

## 🗂️ Project Structure
```
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
```
## 🚀 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/yahoo_finance_scraper.git
cd yahoo_finance_scraper
```
### 2️⃣Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣Download ChromeDriver

Make sure the version matches your Chrome browser.

Add it to your system PATH or place it in the project directory.

## 🖥️ Usage
Run the scraper:
```bash
python scraper/stock_scraper.py
```
## 📊 Output
| Column     | Description                  |
| ---------- | ---------------------------- |
| Symbol     | Stock symbol                 |
| Name       | Company name                 |
| Price_usd  | Current stock price in USD   |
| Change     | Price change                 |
| Volume_M   | Trading volume (in millions) |
| Market Cap | Market capitalization        |
| PE_Ratio   | Price-to-Earnings ratio      |

## 🤝 Contributing

- Fork the repository

- Create a branch: git checkout -b feature/your-feature

- Commit changes: git commit -m "Add feature"

- Push branch: git push origin feature/your-feature

- Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🧑‍💻 Author
### Sikder Sabit Al Fahad ###
- Github: https://github.com/sabitalfahad
- Email: sabitalfahad.info@gmail.com