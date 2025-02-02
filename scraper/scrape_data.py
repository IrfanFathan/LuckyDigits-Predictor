import requests
from bs4 import BeautifulSoup
import sqlite3

# 🔹 Define the URL (Update this with the actual lottery website)
URL = "https://example.com/lottery-results"

# 🔹 Fetch the webpage
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to retrieve data")
    exit()

# 🔹 Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# 🔹 Extract lottery results (Modify these selectors based on the website structure)
date = soup.find("div", class_="lottery-date").text.strip()
pm_1 = soup.find("span", id="result-1pm").text.strip()
pm_3 = soup.find("span", id="result-3pm").text.strip()
pm_6 = soup.find("span", id="result-6pm").text.strip()
pm_8 = soup.find("span", id="result-8pm").text.strip()

# 🔹 Connect to the SQLite database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# 🔹 Insert scraped data into the database
try:
    cursor.execute("""
        INSERT INTO lottery_results (date, pm_1, pm_3, pm_6, pm_8)
        VALUES (?, ?, ?, ?, ?)
    """, (date, pm_1, pm_3, pm_6, pm_8))
    conn.commit()
    print(f"Data inserted for {date}")
except sqlite3.IntegrityError:
    print(f"Data for {date} already exists. Skipping.")

# 🔹 Close the database connection
conn.close()
