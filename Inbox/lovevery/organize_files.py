import requests
from bs4 import BeautifulSoup
import os
import shutil
import time
from urllib.parse import urljoin, quote
import re

BASE_DIR = r"c:\Users\ninni\Documents\projects\lovevery\Playtime Activities"

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

def get_article_categories():
    url_to_categories = {}
    print("Scanning categories to build map...")
    
    for category, base_url in AGE_RANGE_URLS.items():
        print(f"  Scanning {category}...")
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
                    
                    # Normalize URL (strip trailing slash for consistency)
                    href = href.rstrip('/')
                    
                    if href not in url_to_categories:
                        url_to_categories[href] = []
                    
                    if category not in url_to_categories[href]:
                        url_to_categories[href].append(category)
                        new_links += 1
                
                if new_links == 0 and page > 1:
                    break
                
                page += 1
                time.sleep(0.2)
            except Exception as e:
                print(f"    Error scanning {url}: {e}")
                break
    return url_to_categories

def organize():
    if not os.path.exists(BASE_DIR):
        print(f"Directory not found: {BASE_DIR}")
        return

    # 1. Build Map
    url_map = get_article_categories()
    print(f"Mapped {len(url_map)} articles to categories.")

    # 2. Scan Files
    files = [f for f in os.listdir(BASE_DIR) if f.endswith('.md') and f != 'index.md']
    print(f"Found {len(files)} markdown files to organize.")

    categorized_files = {cat: [] for cat in AGE_RANGE_URLS.keys()}
    uncategorized_files = []

    for filename in files:
        filepath = os.path.join(BASE_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract Source URL
        match = re.search(r'Source: (https?://\S+)', content)
        if match:
            source_url = match.group(1).strip().rstrip('/')
            
            # Find categories
            categories = url_map.get(source_url)
            
            if categories:
                for cat in categories:
                    # Create folder
                    cat_dir = os.path.join(BASE_DIR, cat)
                    if not os.path.exists(cat_dir):
                        os.makedirs(cat_dir)
                    
                    # Copy file
                    dest_path = os.path.join(cat_dir, filename)
                    shutil.copy2(filepath, dest_path)
                    categorized_files[cat].append(filename)
                
                # Delete original
                os.remove(filepath)
                print(f"Moved {filename} to {categories}")
            else:
                print(f"Warning: No category found for {filename} (URL: {source_url})")
                uncategorized_files.append(filename)
        else:
            print(f"Warning: No Source URL found in {filename}")
            uncategorized_files.append(filename)

    # 3. Create New Index
    create_master_index(categorized_files, uncategorized_files)

def create_master_index(categorized, uncategorized):
    index_path = os.path.join(BASE_DIR, "index.md")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# Playtime Activities Index\n\n")
        
        for cat, files in categorized.items():
            if not files:
                continue
            f.write(f"## {cat}\n\n")
            files.sort()
            for filename in files:
                # Link to the file in the subdirectory
                # Need to URL encode the path parts
                encoded_cat = quote(cat)
                encoded_filename = quote(filename)
                # Remove .md from title for display
                title = filename[:-3]
                f.write(f"- [{title}](./{encoded_cat}/{encoded_filename})\n")
            f.write("\n")
        
        if uncategorized:
            f.write("## Uncategorized\n\n")
            uncategorized.sort()
            for filename in uncategorized:
                encoded_filename = quote(filename)
                title = filename[:-3]
                f.write(f"- [{title}](./{encoded_filename})\n")
    
    print(f"Created master index at {index_path}")

if __name__ == "__main__":
    organize()
