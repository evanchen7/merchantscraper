#!/usr/bin/env python3

import time, sys, os
from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse
from bs4 import BeautifulSoup


start = time.time()

class SeleniumPooling:
    def __init__(self, website):
        print(urlparse(website))
        self.driver = None
        self.website = website
        self.domain = ''
        self.urlToDo = { self.website }

    def setupSelenium(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument("--headless")
        # options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(chrome_options=options)

    def search(self):
        self.setupSelenium()

        self.driver.set_page_load_timeout(30)
        self.driver.get(self.website)

        # Parses HTML page into BeautifulSoup
        bs_obj = BeautifulSoup(self.driver.page_source, 'html.parser')

        # Finds all HREF references
        linkResults = bs_obj.find_all('a', href = True)



        #Grabs same domain name and checks for duplicates
        for link in linkResults:
            try:
                parsed_uri = urlparse(link.get('href'))

                if (len(self.domain) == 0):
                    parsedWebsite = urlparse(self.website)
                    self.domain = parsedWebsite.netloc

                newLink = 'https://' + self.domain + parsed_uri.path
                self.urlToDo.add(newLink)

                if len(self.urlToDo) >= self.linkCount:
                    break
            except:
                pass
        self.generate()

        print('Set of urls to check: ', self.urlToDo)

    def chunkArray(self, size):
        newList = list(self.urlToDo)
        for i in range(0, len(newList), size):
            yield newList[i:i+size]
        print(newList)
    def generate(self):

        if (len(self.urlToDo) > 30):
            self.chunkArray(3)
        else:
            self.chunkArray(2)

        def run_process(process):
            os.system('python {}'.format(process))


        # with Pool(10) as p:

        #     p.imap(run_process, [self.createWebdriver().get('https://www.google.com'),
        #                          self.createWebdriver().get('https://www.google.com'),
        #                          self.createWebdriver().get('https://www.google.com')])


    def createWebdriver(self):
        print('inside')
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        return webdriver.Chrome(chrome_options=options)
        # for x in range(count):
        #     webdrivers.append(webdriver.Chrome(chrome_options=options))
        # return webdrivers
try:
    # test = SeleniumPooling(website = 'https://www.princesspolly.com')
    # test.search()

    def chunkArray(newList, size):
        for i in range(0, len(newList), size):
            yield newList[i:i + size]

    print (list(chunkArray(range(10, 750), 10)))

except KeyboardInterrupt:
        test.driver.quit()
        sys.exit()
finally:
    print('{} completed in {}'.format(__name__, time.time()-start))