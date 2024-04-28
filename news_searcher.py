from GoogleNews import GoogleNews, ResultSet

def search_news(keyword):
    googlenews = GoogleNews(lang='uk', period='d', region='Ukraine')
    googlenews.search(keyword)
    result = googlenews.result()[0]
    print(result.get('link').lower())