import mechanize, urllib2, time
from bs4 import BeautifulSoup
# import pandas as pd
from multiprocessing import Process, Queue, Pool, cpu_count

base_url = "https://myanimelist.net"
search_url = 'users.php?q=&loc=&agelow=8&agehigh=40&g=&show='
headers = ("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")



br = mechanize.Browser() #create a browser instance
br.set_handle_robots(False)

br.addheaders = [headers]

# print br.open(url).read()

def process():
    pages_links = [base_url+search_url+str(x) for x in xrange(0,480,24)]


def get_profiles(page=None):
    search_page = open('search.html', 'r').read()
    soup = BeautifulSoup(search_page, 'html.parser')
    search_results = soup.find_all('table')[1]
    profiles = []
    for item in search_results.find_all('div', {"class","picSurround"}):
        profiles.append(base_url+item.find('a')['href'])
    return profiles

def process_profile(page=None):
    profile_page = open('profile.html', 'r').read()
    soup = BeautifulSoup(profile_page, 'html.parser')
    profile_info = {}
    info = soup.find_all(class_='user-status')[0]
    for li in info.find_all('li'):
        key, value = li.find_all('span')
        profile_info[key.text.encode('ascii', 'ignore').lower()] = value.text.encode('ascii', 'ignore')
    return profile_info

def process_anime_list_page(page=None):
    anime_list = open('anime.html', 'r').read()
    soup = BeautifulSoup(anime_list, 'html.parser')
    columns = []
    for th in soup.find('tr', {'class', 'list-table-header'}):
        columns.append(th['class'][1])
    

print process_anime_list_page()
