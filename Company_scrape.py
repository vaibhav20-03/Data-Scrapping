from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0'}

try:
    source = requests.get("https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue",headers)
    source.raise_for_status()

    #for finding column heading 
    soup = BeautifulSoup(source.text,'html.parser')
    table = soup.find_all('table')[1]
    heading=table.find_all('th')
    headings=[head.text for head in heading]
    #print(headings) 

    df = pd.DataFrame(columns=headings)
    

    #for findings values
    column_data = table.find_all('tr')
    for row in column_data[1:]:
        row_data=row.find_all('td')
        single_row = [value.text.strip() for value in row_data]
        

        length = len(df)
        df.loc[length] = single_row
        #print(df)
    
    df.to_excel(r'C:/Users/Hp/Desktop/Companies.xlsx',index=False)

except Exception as e:
    print(e)    
