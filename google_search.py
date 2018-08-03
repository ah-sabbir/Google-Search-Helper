from bs4 import BeautifulSoup
import urllib.request
import requests
import re
import random
import threading as thread
import pandas as pd
import time

# List with google queries I want to make read from text file
with open("input.txt","r+") as data_file:
    data_list=data_file.readlines()

desired_google_queries =[x.strip() for x in data_list]

def str_rand(st,lenth_of_domain):
    random_list=[]
    for i in range(0,len(st)):
        match=''
        for j in range(0,len(lenth_of_domain)):
            match=match+random.choice(st)
        random_list.append(match)
    return random_list
            

def sub_str(name):
    name=(((((name.replace(" ",'')).replace(".",'')).replace(",",'')).replace(")",'')).replace("(",''))
    sub_name_list=[]
    for i in range(0,len(name)):
        for j in range(0,len(name)):
            if name[i:j]=='':
                pass
            else:
                sub_name_list.append(name[i:j])
    return sub_name_list

def str_matched(company_name,domain):
    if (domain.lower()).startswith("www."):
        domain=(((domain.replace("www.",'')).replace("-",'')).replace("&",''))
##    data= sub_str(company_name.lower())
##    l=sub_str(domain.lower())
    company_name=(((comapany_name.replace(" ",'')).lower()).replace("-",'')).replace("&",'')
    if((company_name[:2]).lower()==(domain[:2]).lower()) or ((company_name[:3]).lower()==(domain[:3]).lower()):
        return True
    
    '''for d in range(0,len(data)):
        for i in range(0,len(l)):
            if data[d] is l[i]:
                return True'''
        
     


def domain_getter():
    con=True
    start_time=time.time()
    uk_company=[]
    uk_domain=[]
    company_name=[]
    domain=[]
    print("you have to wait while running this proccess ")
    for query in desired_google_queries:
        data=query
        query=query.replace(" ","+")
        # Constracting http query
        bing_url = 'https://www.bing.com/search?q=' + query
        google_url = 'http://google.com/search?q=' + query
        runningTime=round((time.time() - start_time),3)
        print("--- %s seconds passed --- " % runningTime)        
        # For avoid 403-error using User-Agent
        try:
            if con == True:
                print("running google searching ...")
                url=google_url
            else:
                print("running bing searching ...")
                url=bing_url
            global req,response
            req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
            response = urllib.request.urlopen( req )
            html = response.read()
            # Parsing response
            soup = BeautifulSoup(html, 'lxml')
            # Extracting number of results
            #resultStats = soup.find(id="resultStats").string
            all_links=soup.find_all('div')
            for link in all_links:
                if "http" or "https" in link.a:
                    #print(link.text)
                    if data in link.text:
                        lnk=str(link).split("/")
                        for l in lnk:
                            if l.startswith('www') :
                                if str_matched(data,l)==True:
                                    if l in domain:
                                        break
                                    company_name.append(data)
                                    domain.append(l)
    # if there is connection error to google or bing then it change it's own link and running 
        except:
            if con == True:
                con=False
            else:
                con=True
                                

    #start DataFrame
    d_list={'company name':company_name,'domain':domain}
    writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
    dataframe= pd.DataFrame(d_list)
##    print(dataframe)
    dataframe.to_excel(writer)
    writer.save()
##result = str_matched('SUQIAN GREEN WOODEN PRODUCTS CO.,LTD' ,"www.klm.com")
domain_getter()



