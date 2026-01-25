import requests
from bs4 import BeautifulSoup
import os
from markdownify import markdownify as md
import re
from urllib.parse import urljoin, quote
import time

# List of Age Range URLs to crawl
AGE_RANGE_URLS = [
    "https://blog.lovevery.com/age-range/0-12-weeks/",
    "https://blog.lovevery.com/age-range/3-4-months/",
    "https://blog.lovevery.com/age-range/5-6-months/",
    "https://blog.lovevery.com/age-range/7-8-months/",
    "https://blog.lovevery.com/age-range/9-10-months/",
    "https://blog.lovevery.com/age-range/11-12-months/",
    "https://blog.lovevery.com/age-range/13-15-months/",
    "https://blog.lovevery.com/age-range/16-18-months/",
    "https://blog.lovevery.com/age-range/19-21-months/",
    "https://blog.lovevery.com/age-range/22-24-months/",
    "https://blog.lovevery.com/age-range/25-27-months/",
    "https://blog.lovevery.com/age-range/28-30-months/",
    "https://blog.lovevery.com/age-range/31-33-months/",
    "https://blog.lovevery.com/age-range/34-36-months/"
]

OUTPUT_DIR = r"c:\Users\ninni\Documents\projects\lovevery\Playtime Activities"

def clean_filename(title):
    return re.sub(r'[\\/*?:"<>|]', "", title).strip()

def crawl():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    all_articles = {} # Use dict to deduplicate by URL

    for base_url in AGE_RANGE_URLS:
        print(f"Crawling category: {base_url}")
        page = 1
        while True:
            if page == 1:
                url = base_url
            else:
                url = f"{base_url}page/{page}/"
            
            print(f"  Fetching list page: {url}")
            try:
                response = requests.get(url)
                
                # Check for 404 or redirect to homepage/other page which implies end of pagination
                if response.status_code == 404:
                    print("    404 Not Found. End of pagination.")
                    break
                # Some sites redirect to page 1 or homepage on invalid page
                if response.url != url and page > 1:
                     print(f"    Redirected to {response.url}. End of pagination.")
                     break
                
                response.raise_for_status()
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Find article links
                # Updated selector for Playtime Activities: a.post-grid-block__article-link
                # Also keeping the old one just in case: a.skill-grid-block__article-link
                article_links = soup.select('a.post-grid-block__article-link, a.skill-grid-block__article-link')
                
                if not article_links:
                    print("    No articles found on this page.")
                    if page > 1:
                        break
                    # If page 1 has no articles, maybe selector is wrong or empty category.
                
                new_articles_count = 0
                for link in article_links:
                    article_url = link.get('href')
                    if not article_url.startswith('http'):
                        article_url = urljoin(base_url, article_url)
                    
                    if article_url not in all_articles:
                        title_tag = link.find('h3')
                        title = title_tag.get_text(strip=True) if title_tag else "Untitled"
                        all_articles[article_url] = title
                        new_articles_count += 1
                
                print(f"    Found {len(article_links)} links, {new_articles_count} new.")
                
                if new_articles_count == 0 and page > 1:
                    print("    No new articles found (likely duplicate page). End of pagination.")
                    break

                # Check for "Next" button to be sure, or just rely on 404/redirect
                # If we rely on 404, we just increment.
                page += 1
                time.sleep(1) # Be polite
                
            except Exception as e:
                print(f"    Error fetching {url}: {e}")
                break

    print(f"Total unique articles found: {len(all_articles)}")

    processed_articles = []

    for article_url, title in all_articles.items():
        print(f"Processing article: {title} ({article_url})")
        try:
            article_resp = requests.get(article_url)
            article_resp.raise_for_status()
            article_soup = BeautifulSoup(article_resp.content, 'html.parser')
            
            # Extract content
            # Try to find the main content container. 
            # Common patterns: div.post-content, article, div.entry-content
            content_div = article_soup.select_one('div.post-content')
            if not content_div:
                content_div = article_soup.select_one('article')
            if not content_div:
                 print(f"  Warning: Could not find specific content div for {title}. Using body.")
                 content_div = article_soup.body

            # Remove unwanted elements from content (optional, but good for clean markdown)
            for tag in content_div.select('script, style, .related-posts, .share-buttons, header, footer'):
                tag.decompose()

            markdown_content = md(str(content_div), heading_style="ATX")
            
            # Save to file
            filename = clean_filename(title) + ".md"
            filepath = os.path.join(OUTPUT_DIR, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"Source: {article_url}\n\n")
                f.write(markdown_content)
            
            processed_articles.append({"title": title, "filename": filename})
            time.sleep(0.5)
            
        except Exception as e:
            print(f"  Error processing {title}: {e}")

    # Create Index
    create_index(processed_articles)

def create_index(articles):
    index_path = os.path.join(OUTPUT_DIR, "index.md")
    # Sort articles by title
    articles.sort(key=lambda x: x['title'])
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# Playtime Activities\n\n")
        f.write(f"Total Articles: {len(articles)}\n\n")
        for article in articles:
            encoded_filename = quote(article['filename'])
            f.write(f"- [{article['title']}](./{encoded_filename})\n")
    print(f"Created index at {index_path}")

if __name__ == "__main__":
    crawl()
