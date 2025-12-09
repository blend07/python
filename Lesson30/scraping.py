import requests
from bs4 import BeautifulSoup
import pandas as pd  # Import pandas for handling CSV

# Define custom headers to simulate a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}


# Function to get the content from a single page
def get_page_content(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    return None


# Function to extract articles from the page content
def extract_articles(content):
    soup = BeautifulSoup(content, 'html.parser')
    articles = []

    # Find all the articles on the page
    for article in soup.find_all('div', class_='search-item'):
        # Find the 'search-txt' div within the article
        title_div = article.find('div', class_='search-txt')

        # Initialize variables for the extracted information
        title = "No title found"
        link = "No link found"
        date = "No date found"
        description = "No description found"

        # Ensure title_div is not None
        if title_div:
            # Extract title and link
            title_tag = title_div.find('a')
            if title_tag:
                title = title_tag.get_text(strip=True)
                link = title_tag['href']

            # Extract date from the first `li` tag in `ul` with class 'story-meta'
            meta_ul = title_div.find('ul', class_='story-meta')
            if meta_ul:
                date_li = meta_ul.find_all('li')[0]
                if date_li:
                    date = date_li.get_text(strip=True)

            # Extract description from the first `p` tag within the article
            description_tag = article.find('p')
            if description_tag:
                description = description_tag.get_text(strip=True)

        # Append the extracted information to the articles list
        articles.append({
            'Title': title,
            'Link': link,
            'Date': date,
            'Description': description
        })

    return articles


# Main function to scrape multiple pages
def scrape_multiple_pages(base_url, num_pages):
    all_articles = []

    for page in range(1, num_pages + 1):
        url = f"{base_url}/page/{page}"
        print(f"Scraping {url}...")
        page_content = get_page_content(url)
        if page_content:
            articles = extract_articles(page_content)
            all_articles.extend(articles)
        else:
            print(f"Failed to retrieve content from {url}")

    return all_articles


# Scrape the first 5 pages
base_url = 'https://www.technewsworld.com/section/technology'
num_pages = 5
all_articles = scrape_multiple_pages(base_url, num_pages)

# Convert the list of articles to a pandas DataFrame
df = pd.DataFrame(all_articles)

# Save the DataFrame to a CSV file
df.to_csv('technewsworld_articles.csv', index=False)

print("Articles have been saved to technewsworld_articles.csv")