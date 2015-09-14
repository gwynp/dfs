# Gwyn
# Script that scrapes dfsgold site for results of Draftkings MLB Contests
# Grabs a date range based on the date1 and date2 variables
# 
from bs4 import BeautifulSoup
from urllib import urlopen
import time
import datetime

date1 = datetime.date(2015, 4, 6)
#date1 = datetime.date(2015, 9, 12)
date2 = datetime.date(2015, 9, 13)
resultsFile = 'results.csv'

def daterange(d1, d2):
    return (d1 + datetime.timedelta(days=i) for i in range((d2 - d1).days + 1))

def processTheDay(theday):
	print theday
	optionsUrl = 'http://www.dfsgold.com/mlb/daily-fantasy-recap-draftkings-' + theday
	print optionsUrl
	optionsPage = urlopen(optionsUrl)
	soup = BeautifulSoup(optionsPage)
	table = soup.find("table", { "id" : "MainContent_GridView3" })
	for row in table.findAll("tr"):
		cells = row.findAll("td")
		if len(cells) == 10:
			contestName = cells[0].find(text=True)
			contestTime = cells[1].find(text=True)
			contestBuyIn = cells[2].find(text=True)
			contestEntries = cells[3].find(text=True)
			contestPool = cells[4].find(text=True)
			contestTopPrize = cells[5].find(text=True)
			contestCash = cells[6].find(text=True)
			contestWin = cells[7].find(text=True) 
			contestWinner = cells[8].find(text=True) 
			contestTotalEntries = cells[9].find(text=True)
			print >> fo, theday + ';' + contestName + ';' + contestTime + ';' + contestBuyIn + ';' + contestEntries + ';' + contestPool + ';' + contestTopPrize + ';' + contestCash + ';' + contestWin + ';' + contestWinner + ';' + contestTotalEntries	
	return



# open results file and print csv header
fo = open(resultsFile, "w")
print >> fo, "Date;Name;Time;Buy-In;Entries;Prize Pool;Top Prize;Pts Cash;Pts Win;Winner Name;Winner Num Of Entries"

#this is the main part.  Cycle through the two dates al call the scraper function
for d in daterange(date1, date2):
	theday = d.strftime('%b-%d-%Y').decode('utf-8').lower()
	print theday
	processTheDay(theday)
	
fo.close()