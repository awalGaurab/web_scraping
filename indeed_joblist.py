# import neccessary libraries
import os,csv
import requests
from bs4 import BeautifulSoup

# Read the data from the url,where each webpage contains 10 job list.
for i in range(0,351,10):
    url ="https://jp.indeed.com/jobs?q=%E3%83%87%E3%83%BC%E3%82%BF%E3%82%B5%E3%82%A4%E3%82%A8%E3%83%B3%E3%83%86%E3%82%A3%E3%82%B9%E3%83%88&l=%E6%9D%B1%E4%BA%AC%E9%83%BD&start={}".format(i)
 
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    results = soup.find_all('td',class_="resultContent")
    
    for res in results:      
        job_title = res.find('h2',class_='jobTitle').text
        company_name = res.find('span',class_ = 'companyName').text
        location = res.find('div',class_ = 'companyLocation').text
        datalist = [job_title,company_name,location]
        header = ['Job title','Company name','Office location']

        path = os.getcwd()
        filename = 'datascientist_job.csv'
        file_specified = os.path.join(path,filename)
        file_exists = os.path.exists(file_specified)

        with open(file_specified,mode='a',newline='',encoding='utf-8') as csvfile:
            file_writer = csv.writer(csvfile,delimiter=',')
            if not file_exists:
                file_writer.writerow(header)
            file_writer.writerow(datalist)


