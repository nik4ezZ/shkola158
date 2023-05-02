import requests
from bs4 import BeautifulSoup
import json

c = 0
def get_news():
    global c
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0 (Edition Yx GX)"
    }
    url = "https://school158.best"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')
    all_news = soup.find_all("div", class_="elementor-post__card")

    news_dict = {}
    for news in all_news:
        news_title = news.find('span', class_='elementor-post__title').find('a').text.strip()
        news_url = news.find('a').get('href')
        c += 1
        # news_disc = f"https://www.cybersport.ru{news.find('a', class_='link_CocWY').get('href')}"
        news_discription = news.find('div', class_='elementor-post__excerpt').find('p').text
        news_date_time = news.find('span', class_='elementor-post-date').text
        #article_id = news_url.split('/')[3] + news_url.split('/')[4] + news_url.split('/')[5]
        article_id1 = news_url.replace('%','').replace('/','')
        article_id2 = article_id1.split('-')[2]
        news_dict[article_id2] = {
         "news_title": news_title,
        "news_desc": news_discription,
       "news_url": news_url,
            "news_date_time": news_date_time.replace('\t','').replace('\t',''),
             }
        #print(f'{c} | {news_title} | {news_discription} | {news_date_time} | {news_url}')


    with open('news_dict.json', 'w') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

def check_news_updates():
    with open('news_dict.json') as file:
        news_dict = json.load(file)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0 (Edition Yx GX)"
    }
    url = "https://school158.best"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')
    all_news = soup.find_all("div", class_="elementor-post__card")
    new_news = {}
    for news in all_news:
        news_url = news.find('a').get('href')
        article_id1 = news_url.replace('%', '').replace('/', '')
        article_id2 = article_id1.split('-')[2]

        if article_id2 in news_dict:
            continue
        else:
            news_title = news.find('span', class_='elementor-post__title').find('a').text.strip()
            # news_disc = f"https://www.cybersport.ru{news.find('a', class_='link_CocWY').get('href')}"
            news_discription = news.find('div', class_='elementor-post__excerpt').find('p').text
            news_date_time = news.find('span', class_='elementor-post-date').text
            # article_id = news_url.split('/')[3] + news_url.split('/')[4] + news_url.split('/')[5]
            article_id1 = news_url.replace('%', '').replace('/', '')
            article_id2 = article_id1.split('-')[2]
            news_dict[article_id2] = {
                "news_title": news_title,
                "news_desc": news_discription,
                "news_url": news_url,
                "news_date_time": news_date_time.replace('\t', '').replace('\t', ''),
            }
            new_news[article_id2] = {
                "news_title": news_title,
                "news_desc": news_discription,
                "news_url": news_url,
                "news_date_time": news_date_time.replace('\t', '').replace('\t', ''),
            }
            # print(f'{c} | {news_title} | {news_discription} | {news_date_time} | {news_url}')

    with open('news_dict.json', 'w') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

    return new_news



def main():
    get_news()
    check_news_updates()

if __name__ == '__main__':
    main()