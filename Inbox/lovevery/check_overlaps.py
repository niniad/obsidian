import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

AGE_RANGE_URLS = {
    "0 - 12 Weeks": "https://blog.lovevery.com/age-range/0-12-weeks/",
    "3 - 4 Months": "https://blog.lovevery.com/age-range/3-4-months/",
    "5 - 6 Months": "https://blog.lovevery.com/age-range/5-6-months/",
    "7 - 8 Months": "https://blog.lovevery.com/age-range/7-8-months/",
    "9 - 10 Months": "https://blog.lovevery.com/age-range/9-10-months/",
    "11 - 12 Months": "https://blog.lovevery.com/age-range/11-12-months/",
    "13 - 15 Months": "https://blog.lovevery.com/age-range/13-15-months/",
    "16 - 18 Months": "https://blog.lovevery.com/age-range/16-18-months/",
    "19 - 21 Months": "https://blog.lovevery.com/age-range/19-21-months/",
    "22 - 24 Months": "https://blog.lovevery.com/age-range/22-24-months/",
    "25 - 27 Months": "https://blog.lovevery.com/age-range/25-27-months/",
    "28 - 30 Months": "https://blog.lovevery.com/age-range/28-30-months/",
    "31 - 33 Months": "https://blog.lovevery.com/age-range/31-33-months/",
    "34 - 36 Months": "https://blog.lovevery.com/age-range/34-36-months/"
}

def check_overlaps():
    article_to_categories = {}

    for category, base_url in AGE_RANGE_URLS.items():
        print(f"Scanning {category}...")
        page = 1
        while True:
            url = base_url if page == 1 else f"{base_url}page/{page}/"
            try:
                resp = requests.get(url)
                if resp.status_code == 404 or (page > 1 and resp.url != url):
                    break
                
                soup = BeautifulSoup(resp.content, 'html.parser')
                links = soup.select('a.post-grid-block__article-link, a.skill-grid-block__article-link')
                
                if not links:
                    break

                new_links = 0
                for link in links:
                    href = link.get('href')
                    if not href.startswith('http'):
                        href = urljoin(base_url, href)
                    
                    if href not in article_to_categories:
                        article_to_categories[href] = []
                    
                    if category not in article_to_categories[href]:
                        article_to_categories[href].append(category)
                        new_links += 1
                
                if new_links == 0 and page > 1:
                    break
                
                page += 1
                time.sleep(0.5)
            except Exception as e:
                print(f"Error: {e}")
                break
    
    # Analyze overlaps
    multi_category_count = 0
    total_articles = len(article_to_categories)
    
    for url, cats in article_to_categories.items():
        if len(cats) > 1:
            multi_category_count += 1
            # print(f"Overlap: {url} -> {cats}")

    print(f"Total Articles: {total_articles}")
    print(f"Articles in multiple categories: {multi_category_count}")

if __name__ == "__main__":
    check_overlaps()
