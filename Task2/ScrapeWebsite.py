import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# URL of the Wikipedia Main Page
url = 'https://en.wikipedia.org/wiki/Main_Page'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the "In the news" section by ID
    news_section = soup.find('div', id='mp-itn')

    # Check if the news section exists
    if news_section:
        # Open a CSV file to write the data
        with open('news_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Headline', 'News'])  # Write headers

            # Find all list items within the news section
            news_items = news_section.find_all('li')
            if news_items:
                # Get the current date
                current_date = datetime.now().strftime('%Y-%m-%d')

                # Loop through each news item
                for item in news_items:
                    # Extract the headline (first <a> tag's text)
                    headline = item.find('a').text.strip()

                    # Extract the rest of the news text (remaining text after the first <a> tag)
                    news_text = item.get_text(separator=' ').replace(headline, '').strip()

                    # Write the date, headline, and news text into the CSV file
                    writer.writerow([current_date, headline, news_text])

                print("Data saved to news_data.csv in tabular form!")
            else:
                print("No news items found in the news section.")
    else:
        print("News section not found on the page.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")






