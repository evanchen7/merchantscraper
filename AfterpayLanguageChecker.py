#!/usr/bin/env python3
from __future__ import print_function

import requests, regex, os, csv
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


class AfterpayLanguageChecker:

    def __init__(self, url, targetword):

        self.url = self.convert(url)
        self.targetWord = [targetword]

    def convert(self, url):
        if url.startswith('https://www.'):
            return 'https://' + url[len('http://www.'):]
        if url.startswith('www.'):
            return 'https://' + url[len('www.'):]
        if not url.startswith('https'):
            return 'http://' + url
        return url

    def regexGenerator(self):
        patterns = [(("(?i){}*".format(x))) for x in self.targetWord]
        return regex.compile('|'.join(patterns), regex.IGNORECASE)

    def requests_retry_session(self, retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504), session=None,):
        session = session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

    def patternMatcher(self):
        patterns = self.regexGenerator()
        try:
            page = self.requests_retry_session().get(self.url)
        except UnicodeError:
            return UnicodeError
        except Exception as x:
            print(x)
            print('It failed :(', x.__class__.__name__)
            return x.__class__.__name__
        else:
            if patterns.findall(page.text):
                print('True')
                return True
            else:
                print('False')
                return False


if __name__ == "__main__":
    try:
        # SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
        # store = file.Storage('credentials.json')
        # creds = store.get()
        # if not creds or creds.invalid:
        #     flow = client.flow_from_clientsecrets('client_secret_211130033141-ld8g50e9mipcf41k810mo2e5imtfag7b.apps.googleusercontent.com.json', SCOPES)
        #     creds = tools.run_flow(flow, store)
        # service = build('sheets', 'v4', http=creds.authorize(Http()))
        # SPREADSHEET_ID = '1lx_WaorGKZapzNNaG82B3-5O3JxGmWSc3Ex60TZWkbo'
        # RANGE_NAME = 'Output!A:C'
        # result = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
        #                                             range=RANGE_NAME ).execute()
        # values = result.get('values', [])
        # if not values:
        #     print('No data found.')
        # else:
        #     for row in values:
        #         targetUrl = row[1]
        #         if row[1] == '':
        #             row[1] = '-----'
        #         output = afterpayLanguageChecker(targetUrl, 'Shopify-Afterpay')
        #         with open('test.csv', 'a+') as outputFile:
        #             outputFile.write('{},{},{}\n'.format(row[0], row[1], output.patternMatcher()))

        with open('/Users/evanchen/Downloads/currentMerchants.csv') as inputFile:
            openCSV = list(csv.reader(inputFile))
            noHeaderCSV = openCSV[1:]
            with open('output.csv', 'a+') as outputFile:
                header = 'Company,Merchant ID, Url, CDN\n'
                outputFile.write(header)
                for row in noHeaderCSV:
                    targetUrl = row[2]
                    if row[1] == '':
                        row[1] = '-----'
                    output = afterpayLanguageChecker(targetUrl, 'Shopify-Afterpay')
                    outputFile.write('{},{},{},{}\n'.format(row[0], row[1], row[2], output.patternMatcher()))


    except Exception as identifier:
        print(identifier)
    else:
        print('Function Ended')