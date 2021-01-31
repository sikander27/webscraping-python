import re
import requests
import bs4

web = input("Enter the website url:")
if len(web)>1:
    print("-----------------------------------------------------")
    print("Website is being scraped. Please wait for a while. -SK")
    print("-----------------------------------------------------")
    try:
        res = requests.get(web)
    except:
        print("something went wrong")
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    scrape = soup.getText()
    emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[.]\w+", scrape))
    print(soup)
    print("---------------------------------------------------------")
    if len(emails) > 0:
        print("List of emails:")
        for email in emails:
            print(email)
            print("-----------------------")
    else:
        print("No email found.")
else:
    print("Invalid input")
    
# res = requests.get('https://www.randomlists.com/email-addresses')
# res1 = requests.get('https://sikander27.github.io/')
# #print(type(res))
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# regex = '^[A-Za-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' 
# scrape = soup.getText()
# emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[.]\w+", scrape))
# print(emails)
# hi = soup.select('title')
# print(hi[0].getText())
