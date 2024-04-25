import pandas as pd
from wordcloud import WordCloud, STOPWORDS


def text_mining(input_path):
    stwords = set(STOPWORDS)
    data = pd.read_csv(input_path)
    stwords = set(STOPWORDS)
    stwords.add('조선비즈')
    stwords.add('호평')
    wordCloud = WordCloud(
        font_path='~./NanumSquareRegular.ttf',
        stopwords= stwords,
        width=400,
        height=400,
        max_font_size=100,
        background_color='white',
    )
    wordCloud.generate(str(data['title']))
    wordCloud.to_file('test.jpg')


def curation(input_path):
    df = pd.read_csv(input_path)
    print(df['title'])
    

curation('/Users/geonmin/Desktop/AiLab_python_project/news_2024-04-15.csv')