#!/usr/bin/env python3
import time, regex, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from multiprocessing import Pool

start = time.time()

class MerchantCompetitionChecker:

    def __init__(self, website, keywords, linkCount = int(15), headlessMode = False):
        if type(website) != str or type(keywords) != list or type(linkCount) != int:
            raise TypeError('(website, keywords, linkCount, headlessMode) need to be (str, list, int, boolean)')
        self.driver = None
        self.website = website
        self.keywords = keywords
        self.linkCount = linkCount
        self.headlessMode = headlessMode
        self.urlToDo = {self.website}
        self.domain = ''
        self.count = 0

    # Initialize Selenium driver
    def setupSelenium(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        if self.headlessMode == True:
            options.add_argument("--headless")
            options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(chrome_options=options)

    def search(self):
        self.setupSelenium()

        self.driver.set_page_load_timeout(30)
        self.driver.get(self.website)

        # Parses HTML page into BeautifulSoup
        bs_obj = BeautifulSoup(self.driver.page_source, 'html.parser')

        # Finds all HREF references
        linkResults = bs_obj.find_all('a', href = True)

        # Grabs same domain name and checks for duplicates
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

        print('Set of urls to check: ', self.urlToDo)
        self.openTab()

    # Opens Chrome in headless mode and opens tabs
    def openTab(self):
        self.driver.set_page_load_timeout(30)

        for sites in self.urlToDo:
            try:
                self.driver.execute_script('window.open("{}","_blank");'.format(sites))
            except:
                pass

        for tabs in self.driver.window_handles:
            try:
                self.driver.switch_to.window(tabs)
                bs_obj = BeautifulSoup(self.driver.page_source, 'html.parser')
                self.checkForKeywords(bs_obj)
            except:
                pass

    # Checks for keywords in the parsed html file
    def checkForKeywords(self, bs4):
        pat = self.regexGenerator()
        with open('{}.txt'.format(self.domain), 'a+') as outfile:
            for line in bs4.find_all():
                if pat.search(str(line)) and self.count < 10:
                    match = pat.search(str(line))
                    outfile.write('\n----------------------------------------------\n')
                    outfile.write(str(match))
                    self.count += 1
                    if self.count > 10:
                        print('More than 10 instances of {} found'.format(self.keywords))
                        self.driver.quit()

    # Generates regular expression for keywords
    def regexGenerator(self):
        patterns = [(("(?i){}*".format(x))) for x in self.keywords]
        return regex.compile('|'.join(patterns), regex.MULTILINE|regex.VERBOSE|regex.IGNORECASE)


if __name__ == "__main__":
    try:
        website = 'https://www.spirithoods.com'
        newSelenium = MerchantCompetitionChecker(website, ['afterpay', 'affirm'], 30)
        newSelenium.search()
        newSelenium.driver.quit()
    except KeyboardInterrupt:
        newSelenium.driver.quit()
        sys.exit()
    finally:
        print('{} completed in {}'.format(__name__, time.time()-start))
