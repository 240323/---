import requests
from bs4 import BeautifulSoup

def get_links(url):
    """
    指定されたURLからリンクを取得する関数
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None and href.startswith('http'):
            links.append(href)
    return links

def crawl(url):
    """
    指定されたURLから全てのページをクローリングする関数
    """
    links_to_visit = [url]
    visited_links = set()
    while links_to_visit: #幅優先探索　
        current_url = links_to_visit.pop(0)
        if current_url in visited_links:
            continue
        visited_links.add(current_url)
        print(f'Crawling {current_url}')
        links = get_links(current_url)
        links_to_visit += links
    print('Crawling complete.')

if __name__ == '__main__':
    url = 'https://sites.google.com/view/shikidalab/home'
    crawl(url)
