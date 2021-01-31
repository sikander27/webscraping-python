#!/usr/bin/env python3

'''
Webpage scraper by Cameron Cobb                
Scrapes for phone and emails and places in     
spreadsheet.                                   
Python 3 required                              
'''

import re
from urllib.request import urlopen, Request
import os
from datetime import datetime

from bs4 import BeautifulSoup


def start_scrape(page):

    print("\n\nWebpage is currently being scrapped... please wait...")
       
    scrape = BeautifulSoup(page, 'html.parser')
    scrape = scrape.get_text()
    
    emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", scrape))

    nodupemail = len(list(emails))

    dupemail = len(list(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", scrape)))

    number_of_dup_email = int(dupemail) - int(nodupemail)

    email_list = list(emails)

    print("-----------------------------\n")

    if len(emails) == 0:
        print("No email address(es) found.")
        print("-----------------------------\n")
    else:
        count = 1
        for item in emails:
            print('Email address #' + str(count) + ': ' + item)
            count += 1


       
    print("\nDuplicates have been removed from list.")
    print("Total email addresses: ", nodupemail)
    print("There were " + str(number_of_dup_email) + " duplicate email addresses.")

  
def main():

    webpage = input("Paste the webpage you would like to scrape (include http/https): ")

    try:
        page = urlopen(webpage) 
        start_scrape(page)
    except:
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(webpage, headers=hdr)
        page = urlopen(req)
        start_scrape(page)

if __name__ == "__main__":
    main()