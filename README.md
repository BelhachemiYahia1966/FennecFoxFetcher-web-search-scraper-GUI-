# FennecFoxFetcher-web-search-scraper-GUI-
FennecFoxFetcher (FFF) is a Tool(Search scraper with a GUI) that let you get links from a lot of pages for a web search. it will give you a lot of URL's with small description 

FennecFoxFetcher Search Scraper with GUI
This Python script uses Playwright to automate a browser and scrape search results from Bing. It includes a GUI interface built with tkinter that allows you to:

Enter a search query.

Specify the path to a custom Chromium executable.

View the scraped results in a scrollable text box.

Features
Web Scraping:

Automates Bing search and extracts the titles and links of search results.

Supports pagination (scrapes multiple pages of results).

GUI Interface:

Input field for the search query.

Input field for the Chromium executable path.

"Browse" button to select the Chromium executable using a file dialog.

"Search" button to start the scraping process.

Scrollable text box to display the results.

Custom Chromium Path:

Allows you to specify the path to a custom Chromium executable, which is useful if the default Playwright Chromium installation is not compatible with your system (e.g., on Windows 8.1).

Requirements
To run this script, you need the following:

Python:

Python 3.7 or later must be installed on your system.

Download Python from python.org.

Playwright:

Playwright is a browser automation library used to control the browser.

Install Playwright using pip:

bash
Copy
pip install playwright
Install the browser binaries:

bash
Copy
playwright install
Chromium Executable (Optional):

If the default Playwright Chromium installation does not work on your system (e.g., on Windows 8.1), you can download a compatible version of Chromium from Chromium.woolyss.com.

Extract the Chromium executable and specify its path in the GUI.

Tkinter:

Tkinter is a standard Python library for creating GUIs. It is included with most Python installations.

How to Use
Clone or Download the Script:

Save the script (FFF_scraper_gui.py) to your local machine.

Install Dependencies:

Install Playwright and its browser binaries:

bash
Copy
pip install playwright
playwright install
Run the Script:

Open a terminal or command prompt and navigate to the directory where the script is saved.

Run the script:

bash
Copy
python bing_scraper_gui.py
Using the GUI:

Enter your search query in the "Enter search query" field.

Specify the path to your Chromium executable in the "Path to Chromium executable" field, or click the "Browse" button to select the executable.

Click the "Search" button to start the scraping process.

The results will be displayed in the scrollable text box.

