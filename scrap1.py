import bs4
import requests


res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
# print(type(res))
# print(res.text)


soup = bs4.BeautifulSoup(res.text,'lxml')

for i in soup.find_all('a',href=True):
    first2letters =i['href'][:2]
    first1letter = i['href'][0]

    if( '#' not in i['href']):
        if( first2letters != '//' or first1letter != '/'):
            print(i['href'])
    elif ("#" not in i['href']):
        if(first1letter == '/'):
            y = i['href'].replace('/','https://')
            print(y)
        elif( first2letters == '//'):
            x = i['href'].replace('//','https://')
            print(x)
