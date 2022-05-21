import csv
import json
import re

with open('Meme Studies Index .xlsx - Sheet1.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    with open('Meme Studies Index Cleaned.csv', 'w', newline='', encoding='utf-8') as authors:
        writer = csv.writer(authors)

        row_list = ['Author1 Last name','Author1 First name','Author2 Last name','Author2 First name','Author3 Last name','Author3 First name','Author4 Last name','Author4 First name','Author5 Last name','Author5 First name','Author6 Last name','Author6 First name','Author7 Last name','Author7 First name','Year*','Scholarly Article*','Platform','Place 1','Place 2','Resource Type*','Book','Book edited by','Publisher','ISBN','City (if book)','Volume','Number','Pages','Link (Where Applicable)','Topic1*','Topic2*','Topic3','Topic4']

        writer.writerow(row_list)

        
        #iterate through every line of csv file
        for row in reader:
            cleaned_isbn = re.sub('[^0-9]", ','',row['ISBN'])
            article_name = row['Scholarly Article*'].replace('“','"').replace('”','"').replace("’","'").replace("‘","'").replace('–','-').replace('…','...')

            cleaned_pages = row['Pages'].replace('–','-')
            link_str = row['Link (Where Applicable)']

            if link_str.endswith('.'):
                cleaned_link = link_str[:-1]
            else:
                cleaned_link = link_str
            row_list = [row['Author1 Last name']] + [row['Author1 First name']] + [row['Author2 Last name']] + [row['Author2 First name']] + [row['Author3 Last name']] + [row['Author3 First name']] + [row['Author4 Last name']] + [row['Author4 First name']] + [row['Author5 Last name']] + [row['Author5 First name']] + [row['Author6 Last name']] + [row['Author6 First name']] + [row['Author7 Last name']] + [row['Author7 First name']] + [row['Year*']] + [article_name] + [row['Platform']] + [row['Place 1']] + [row['Place 2']] + [row['Resource Type*']] + [row['Book']] + [row['Book edited by']] + [row['Publisher']] + [cleaned_isbn] + [row['City (if book)']] + [row['Volume']] + [row['Number']] + [cleaned_pages] + [cleaned_link] + [row['Topic1*']] + [row['Topic2*']] + [row['Topic3']] + [row['Topic4']]

            writer.writerow(row_list)



         
