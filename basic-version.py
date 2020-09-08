import requests
from bs4 import BeautifulSoup

url = 'https://www.yell.com/ucs/UcsSearchAction.do?keywords=coffee&location=London&scrambleSeed=843665584&pageNum=1'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
article = soup.find_all('div', class_ = 'row businessCapsule--mainRow')

for item in article:
    name = item.find('span', class_ = 'businessCapsule--name').text
    link = item.find('a', class_ = 'businessCapsule--title')['href']
    address = item.find('span', {'itemprop': 'address'}).text.strip().replace('\n','')
    try:
        website = item.find('a', class_ = 'btn btn-yellow businessCapsule--ctaItem')['href']
    except:
        website = ''
    try:
        tel = item.find('span', {'class': 'business--telephoneNumber'}).text
    except:
        tel = ''
    try:
        rating = item.find('span', class_ = 'starRating--average').text
        reviews = item.find('span', class_ = 'starRating--total').text
    except:
        rating = ''
        reviews = ''
    business = {
        'name': name,
        'link': 'https://www.yell.com/' + link,
        'address': address,
        'website': website,
        'tel': tel,
        'rating': rating,
        'reviews': reviews,
    }
    print(business)
