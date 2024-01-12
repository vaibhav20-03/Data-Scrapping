from bs4 import BeautifulSoup
import requests, openpyxl


excel=openpyxl.Workbook()
sheet =  excel.active
sheet.title='Movies'
print(excel.sheetnames)
sheet.append(['Rank','Name','Year','Ratings'])

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

try:
    source = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    movies=soup.find('ul',class_='ipc-metadata-list').findAll('li')
    
    for movie in movies:
        rank = movie.find('h3',class_='ipc-title__text').get_text(strip=True).split('.')[0]
        name = movie.find('h3',class_='ipc-title__text').get_text(strip=True).split('.')[1]
        year = movie.find('div',class_='sc-935ed930-7 bHIxWH cli-title-metadata').span.text
        rating = movie.find('span',class_='ipc-rating-star').get_text(strip=True).split('(')[0]
        print(rank,name,year,rating)
        sheet.append([rank,name,year,rating])
        
except Exception as e:
    print(e)
  

excel.save('Movies.xlsx')  