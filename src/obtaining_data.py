import pandas as pd
import urllib.request
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError, URLError

allQuoteData = []

baseUrl = "http://quotes.toscrape.com/"
curPage = baseUrl

while True:
    try:
        print("Retrieving page: " + curPage)
        curPageContent = urllib.request.urlopen(curPage).read()
    except:
        break

    soup = bs(curPageContent, "html.parser")

    quoteBlocks = soup.find_all(class_="quote")

    for quoteBlock in quoteBlocks:
        quoteDict = {}

        # Add quote
        quote = quoteBlock.find(class_="text").text
        quoteDict['Quote'] = quote

        # URL for the each author
        authorUrl = baseUrl + 'author/' + quoteBlock.find("a").get("href").split('/')[2]

        # Read author page
        try:
            authorInfo = urllib.request.urlopen(authorUrl).read()
        except HTTPError as e:
            print(curPage, " ", authorUrl, " ", e)
        except URLError as e:
            print(curPage, " ", authorUrl, " ", e)

        authorSoup = bs(authorInfo, "html.parser")

        # Author name
        author = authorSoup.find(class_='author-title').text
        quoteDict['Author name'] = author

        # Author born date
        authorDob = authorSoup.find(class_='author-born-date').text
        quoteDict['Author DOB'] = authorDob

        # Author place
        authorPlace = authorSoup.find(class_='author-born-location').text
        quoteDict['Author born location'] = authorPlace.replace('in ', '')

        # Author bio
        authorDesc = authorSoup.find(class_='author-description').text
        quoteDict['Author description'] = authorDesc.strip()

        allQuoteData.append(quoteDict)

    if soup.find(class_="next") is None:
        break

    pageLink = soup.find(class_='next').find('a').get('href')[1:]
    nextPage = pageLink
    curPage = baseUrl + nextPage

headers = allQuoteData[0].keys()
quoteDf = pd.DataFrame(allQuoteData, columns=headers)

quoteDf.to_csv("../data/raw/Quotes.csv", encoding='utf-8-sig')
quoteDf.to_excel("../data/raw/Quotes.xlsx")

print('Successfully converted data to CSV, xlsx')