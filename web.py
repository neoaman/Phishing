import numpy as np 
import pandas as pd
from urllib.parse import urlparse
from tld import get_tld
import pickle
import re
def website(site):
    from urllib.parse import urlparse
    from tld import get_tld
    import os.path
    import re
    url_length = len(str(site))
    hostname_length = len(urlparse(site).netloc)
    path_length = len(urlparse(site).path)
    def fd_length(url):
        urlpath= urlparse(url).path
        try:
            return len(urlpath.split('/')[1])
        except:
            return 0
    fd_length = fd_length(site)
    tld = get_tld(site,fail_silently=True)
    def tld_length(tld):
        try:
            return len(tld)
        except:
            return -1

    tld_length = tld_length(get_tld(site,fail_silently=True))
    def digit_count(url):
        digits = 0
        for i in url:
            if i.isnumeric():
                digits = digits + 1
        return digits
    count_digits= digit_count(site)
    def letter_count(url):
        letters = 0
        for i in url:
            if i.isalpha():
                letters = letters + 1
        return letters
    count_letters = letter_count(site)
    def no_of_dir(url):
        urldir = urlparse(url).path
        return urldir.count('/')
    count_dir=no_of_dir(site)
    count_ = site.count('-')
    count_ad = site.count('@')
    count_qu = site.count('?')
    count_pr = site.count('%')
    count_dot = site.count('.')
    count_eql = site.count('=')
    count_http = site.count('http')
    count_https = site.count('https')
    count_www = site.count('www')
    def having_ip_address(site):
        match = re.search(
            '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
            '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
            '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
            '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', site)  # Ipv6
        if match:
            # print match.group()
            return -1
        else:
            # print 'No matching pattern found'
            return 1
    use_of_ip = having_ip_address(site)
    def shortening_service(url):
        match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                          'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                          'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                          'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                          'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                          'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                          'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                          'tr\.im|link\.zip\.net',
                          url)
        if match:
            return -1
        else:
            return 1
    short_url = shortening_service(site)
    site_dict = [hostname_length,
       path_length, fd_length, tld_length, count_, count_ad, count_qu,
       count_pr, count_dot, count_eql, count_http,count_https, count_www, count_digits,
       count_letters, count_dir, use_of_ip]
    return site_dict
    #site = input("Input Site Here: ")

# pickle.dump(dt_model, open('model.pkl', 'wb'))
dt_model = pickle.load(open('/var/www/Phishing/model.pkl','rb'))
def classifier(site):
    phishing_predict = dt_model.predict([website(site)])
    if phishing_predict == 0:
        #print('You are Using Safe Website')
        return 'You Are Using Safe Website'
    else:
        #print('Beware From Phishing Website')
        return 'This Website Is Not Safe'
if __name__ == "__main__":
    print(classifier("https://google.com"))
    