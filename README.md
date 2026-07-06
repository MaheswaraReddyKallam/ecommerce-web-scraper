# E-Commerce Web Scraper 🕸️📚

### Overview
A Python-based data ingestion script designed to extract unstructured data from an e-commerce storefront. This project demonstrates the ability to bypass missing APIs by programmatically downloading raw HTML, parsing the Document Object Model (DOM), and structuring the extracted text into a clean format for downstream AI or data analysis.

### Technologies Used
* **Python**
* **Requests** (HTTP GET requests, Server status validation)
* **BeautifulSoup4** (HTML parsing, DOM navigation)
* **Pandas** (DataFrame structuring)

### Key Features
* **Automated Extraction:** Programmatically hunts specific `<h3>` and `<a>` HTML tags to extract embedded dictionary attributes (book titles).
* **Failsafes & Validation:** Implements `response.raise_for_status()` to ensure the script gracefully handles server rejections or 404 errors before attempting to parse data.
* **Data Structuring:** Automatically converts the raw scraped arrays into a 2D Pandas DataFrame, perfectly bridging the gap between data collection and data analysis.

### How to Run
Ensure the required libraries are installed:
`pip install requests beautifulsoup4 pandas`

Run the script in your terminal to see the live data extraction:
`python scraper.py`
