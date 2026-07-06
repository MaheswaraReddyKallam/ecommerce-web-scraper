import requests
import pandas as pd
from bs4 import BeautifulSoup

# ==========================================
# 1. HTTP REQUEST & VALIDATION
# ==========================================
url = "https://books.toscrape.com/"
response = requests.get(url)

# Ensure the website actually loaded successfully (Status 200 OK)
response.raise_for_status() 

# ==========================================
# 2. HTML PARSING & DATA EXTRACTION
# ==========================================
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("h3")

# Create an empty list to hold our extracted data
scraped_titles = []

for book in books:  
    link = book.find("a")
    
    # Failsafe: Ensure the link exists before extracting the title attribute
    if link: 
        scraped_titles.append(link["title"])

# ==========================================
# 3. DATA STRUCTURING
# ==========================================
# Convert extracted data to a DataFrame for downstream AI/Analytics use
df = pd.DataFrame({"Book Titles": scraped_titles})

print("--- Successfully Scraped Data ---")
print(df.head(10))  # Printing just the top 10 rows for a clean terminal output
