import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://news.ycombinator.com/"

try:
    # Send HTTP request
    response = requests.get(url)
    response.raise_for_status()

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract headlines
    headlines = soup.find_all("span", class_="titleline")

    print("\n===== Latest News Headlines =====\n")

    for i, headline in enumerate(headlines, start=1):
        title = headline.get_text(strip=True)
        print(f"{i}. {title}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching website: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")