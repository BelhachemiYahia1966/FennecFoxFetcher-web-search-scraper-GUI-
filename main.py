from playwright.sync_api import sync_playwright
import logging
import os
import tkinter as tk
from tkinter import scrolledtext, filedialog

# Set up logging
logging.basicConfig(level=logging.INFO)

# Function to perform the search and display results
def osint_ex(query, result_text, chromium_path):
    try:
        with sync_playwright() as pr:
            # Launch the browser with the custom Chromium path
            try:
                browser = pr.chromium.launch(
                    executable_path=chromium_path,  # Use the custom Chromium executable
                    headless=True  # Set headless=False for debugging
                )
            except Exception as e:
                logging.error(f"Failed to launch browser: {e}")
                logging.error("Reinstalling browsers...")
                os.system("playwright install")  # Reinstall browsers
                browser = pr.chromium.launch(
                    executable_path=chromium_path,  # Use the custom Chromium executable
                    headless=False  # Set headless=False for debugging
                )

            page = browser.new_page()

            # Construct the search URL
            search_link = f"https://www.bing.com/search?q={query}"
            page.goto(search_link)

            num_pages = 6  # Number of pages to scrape
            all_results = []  # Store all results

            for page_num in range(1, num_pages + 1):
                logging.info(f"Extracting URLs from Page: {page_num}")
                result_text.insert(tk.END, f"Extracting URLs from Page: {page_num}\n")

                # Wait for the search results to load
                page.wait_for_selector('li.b_algo')

                # Extract all search results
                results = page.query_selector_all('li.b_algo')
                for result in results:
                    try:
                        # Extract title and link
                        title_element = result.query_selector('a')
                        if title_element:
                            title = title_element.inner_text()
                            link = title_element.get_attribute('href')
                            all_results.append({"title": title, "link": link})
                            result_text.insert(tk.END, f'Title: {title}\nLink: {link}\n\n')
                            logging.info(f'Title: {title}\nLink: {link}\n')
                        else:
                            result_text.insert(tk.END, "Skipping result: Could not find title element.\n")
                            logging.warning("Skipping result: Could not find title element.")
                    except Exception as e:
                        result_text.insert(tk.END, f"Error extracting result: {e}\n")
                        logging.error(f"Error extracting result: {e}")

                # Check for and click the "Next" button
                next_page_button = page.query_selector('a.sb_pagN')
                if next_page_button:
                    next_page_button.click()
                    page.wait_for_timeout(3000)  # Wait for the next page to load
                else:
                    result_text.insert(tk.END, "No more pages to scrape.\n")
                    logging.info("No more pages to scrape.")
                    break  # Exit if there's no "Next" button

            # Close the browser
            browser.close()

        # Print all results
        result_text.insert(tk.END, 'All results:\n')
        logging.info('All results:')
        for result in all_results:
            result_text.insert(tk.END, f"Title: {result['title']}\nLink: {result['link']}\n\n")
            logging.info(f"Title: {result['title']}\nLink: {result['link']}\n")

    except Exception as e:
        result_text.insert(tk.END, f"An error occurred: {e}\n")
        logging.error(f"An error occurred: {e}")

# Function to handle the search button click
def on_search():
    query = entry.get()  # Get the search query from the entry widget
    chromium_path = chromium_entry.get()  # Get the Chromium path from the entry widget
    result_text.delete(1.0, tk.END)  # Clear previous results
    osint_ex(query, result_text, chromium_path)  # Perform the search and display results

# Function to browse for the Chromium executable
def browse_chromium():
    file_path = filedialog.askopenfilename(
        title="Select Chromium Executable",
        filetypes=[("Executable Files", "*.exe")]
    )
    if file_path:
        chromium_entry.delete(0, tk.END)
        chromium_entry.insert(0, file_path)

# Create the GUI
root = tk.Tk()
root.title("FennecFoxFetcher (FFF)")

# Create and place the input field for the search query
label = tk.Label(root, text="Enter search query:")
label.pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create and place the input field for the Chromium path
chromium_label = tk.Label(root, text="Path to Chromium executable:")
chromium_label.pack(pady=10)
chromium_entry = tk.Entry(root, width=50)
chromium_entry.pack(pady=10)

# Create and place the browse button for the Chromium executable
browse_button = tk.Button(root, text="Browse", command=browse_chromium)
browse_button.pack(pady=10)

# Create and place the search button
search_button = tk.Button(root, text="Search", command=on_search)
search_button.pack(pady=10)

# Create and place the results text box
result_text = scrolledtext.ScrolledText(root, width=80, height=20)
result_text.pack(pady=10)

# Run the GUI
root.mainloop()
