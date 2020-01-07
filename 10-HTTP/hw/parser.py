import requests
from bs4 import BeautifulSoup
from collections import Counter

def grab_and_parse_pages(url):
    all_pages = []
    stories = []
    curr_page = 0
    while curr_page < 100:
        all_pages.append(session.get(f'https://pikabu.ru/new/subs?page={curr_page}', headers = headers).text)
        curr_page += 1
    for page in all_pages:
        soup = BeautifulSoup(page, 'html.parser')
        stories.extend(soup.find_all('article', limit=10))
    return stories

def find_popular_tags(stories):
    tags = []
    for story in stories:
        s = story.find_all("a", {"class": "tags__tag", "data-tag": True})
        for elem in s:
            tags.append(elem.get("data-tag"))
    popular_tags = Counter(tags).most_common(10)
    return popular_tags

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6",
    "Cache-Control": 'no-cache',
    "Connection": "keep-alive",
    "Cookie": input("     To continue you should input cookie from https://pikabu.ru/new/subs, \n \
    You can get it from subs (Request Headers) in Developer Console:"),
    "Host": "pikabu.ru",
    "Pragma": "no-cache",
    "Referer": "https://pikabu.ru/new/subs",
    "Upgrade-Insecure-Requests": "1",
    }

if __name__ == '__main__':
    session = requests.Session()
    stories = grab_and_parse_pages("https://pikabu.ru/new/subs")
    popular_tags = find_popular_tags(stories)
    with open('./pt.txt', 'w') as f:
        f.write('10 самых популярных тегов:\n')
        for tag in popular_tags:
            f.write(f"{tag[0]} - {tag[1]}\n")
