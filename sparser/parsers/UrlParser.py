from joblib import Parallel, delayed
from sparser.workers.worker import processGoogleURL

global URLS

def scrapeURL(url): 
    a = Parallel(n_jobs=3)(delayed(processGoogleURL)(url) for i in range(1))
    return a

def scrapeURLs(url_list):
    a = Parallel(n_jobs=3)(delayed(processGoogleURL)(i) for i in url_list)

if __name__ == "__main__":
    lst = scrapeURL('http://news.google.com')
    lst = scrapeURLs(lst[0])
    for i in lst: 
        print(len(i))