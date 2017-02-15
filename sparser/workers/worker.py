from bs4 import BeautifulSoup
from urllib.request import urlopen

def processGoogleURL(baseurl):
   
    # list to store and return unique URLs scraped from the site
    urllst = []
   
    # Read URL and load data into beautifulsoup
    r = urlopen(baseurl).read()
    soup = BeautifulSoup(r, 'lxml')
   
    # find all links in the text loaded from the site
    for link in soup.find_all('a', href=True):
       
        # get the link and strip wite space around it (if any)
        link = link['href'].strip()
       
        # get all the links tarting with 'http' and add them to the urllst
        if link.startswith('http'):
            urllst.append(link)
       
        # ignore all links starting with '//'
        elif link.startswith('//'):
            pass
            #link = link[2:]
            #print(link)
       
        # prefix www with http:// for the lines starting with www
        elif link.startswith('www'):
            urllst.append(baseurl + link)
       
        # substitute '/' at the beginning of the link with the baseurl
        elif link.startswith('/'):
            urllst.append(baseurl + link)
   
    # get unique urls by using set() command
    urllst = set(urllst)
   
    # get a list of unique urls back by using list() command and return the list
    return list(urllst)

               
if __name__ == "__main__":
    urllst = processGoogleURL("http://news.google.com")
    print(urllst)