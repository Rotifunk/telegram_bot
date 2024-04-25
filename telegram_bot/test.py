# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime
# import time

# def get_news():
#     news_title, news_link, news_time = [], [], []
#     url = "https://www.google.com/search?q=it%EB%89%B4%EC%8A%A4&sca_esv=2eb6d309d93fdcf1&sca_upv=1&rlz=1C5CHFA_enKR938KR938&biw=1680&bih=904&ie=UTF-8&tbs=qdr:d&tbm=nws&ei=JUkcZvi9I8zAvr0Pwti7gAo&start=0&sa=N"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     count = 2
#     while count :
#         time.sleep(3)
#         response = requests.get(url)
#         soup = BeautifulSoup(response.content, "html.parser")
#         articles = soup.find_all("div", class_='fP1Qef')
#         for article in articles:
#             news_title.append(article.find("div", class_="vvjwJb").text)
#             news_link.append(article.find("a")["href"][7:])
#             news_time.append(article.find("span", class_="rQMQod").text)
#         page_link = soup.find_all("a", class_="G5eFlf")
#         url = f'https://www.google.com{page_link[-1]["href"]}'
#         if len(page_link) > 1:
#             continue
#         else :
#             count -= 1
#     news_df = pd.DataFrame(
#         ({'title': news_title,
#         'link': news_link,
#         'time': news_time
#         }))
#     news_df.to_csv(f'news_{datetime.now().date()}.csv')

from wordcloud import WordCloud, STOPWORDS

print(STOPWORDS)