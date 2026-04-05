import requests
from bs4 import BeautifulSoup
from typing import List, Optional

# Constants for scraping behavior
DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}
CONTENT_LIMIT = 5000000
NOISE_TAGS = ["script", "style", "img", "input", "noscript", "iframe"]

def scrape_text_content(url: str) -> str:
    """
    Downloads a webpage, strips non-textual elements, and returns a 
    truncated summary of the title and body text.
    """
    try:
        response = requests.get(url, headers=DEFAULT_HEADERS, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Error fetching {url}: {e}"

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract page title
    title = soup.title.string.strip() if soup.title else "Untitled Page"
    
    # Process body content if it exists
    if soup.body:
        # Remove elements that don't contribute to textual meaning
        for tag in soup.body(NOISE_TAGS):
            tag.decompose()
        
        # Extract and clean text content
        main_text = soup.body.get_text(separator="\n", strip=True)
    else:
        main_text = "No content found in the page body."

    # Combine title and text, then truncate to stay within token limits
    combined_output = f"TITLE: {title}\n\n{main_text}"
    return combined_output[:CONTENT_LIMIT]

def scrape_hyperlinks(url: str) -> List[str]:
    """
    Extracts all valid 'href' links from a given webpage.
    """
    try:
        response = requests.get(url, headers=DEFAULT_HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Gather all non-empty links
    links = [a.get("href") for a in soup.find_all("a") if a.get("href")]
    
    return links