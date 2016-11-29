#!/usr/bin/python
# -*- coding: gbk -*-

import urllib2
import gzip, StringIO
from datetime import date
from datetime import timedelta
import time
# import csv

# Ask for input of starting YYYYMM and ending YYYYMM
Year = int(raw_input("Year:"))
StartMo = int(raw_input("Start Month:"))
EndingMo = int(raw_input("End Month:"))

oneDay = timedelta(days=1) #itervar
Start = date(Year, StartMo, 1)
End = date(Year, EndingMo+1, 1)-oneDay

# LOOP ON DATE
nowDate = Start
while (nowDate != End + oneDay):
	url = "http://beijingair.sinaapp.com/data/china/sites/"+nowDate.strftime("%Y%m%d")+"/csv"
# 	url = "http://beijingair.sinaapp.com/data/beijing/all/"+nowDate.strftime("%Y%m%d")+"/csv" #BACKUP URL for Beijing data
	response = urllib2.urlopen(url)
	html = response.read()
	html = gzip.GzipFile(fileobj=StringIO.StringIO(html), mode="r")
	
# 	DECODING
	data = html.read().decode('utf-8').encode('gbk') #According to http://beijingair.sinaapp.com/#messy
# 	CHN encoding ref: http://in355hz.iteye.com/blog/1860787; http://www.zhxl.me/1409.html
	
# 	OUTPUT AS CSV FILE
	print "now downloading..."+nowDate.strftime("%Y%m%d")
	fname = "DailyAirData"+nowDate.strftime("%Y%m%d")+".csv"
	outDailyAirData = open(fname, 'wb')
	for line in data:
		outDailyAirData.write(line)
	outDailyAirData.close

# 	BACKUP CODE FOR UNFINISHED CSV MODULE
# 	csvfile = file(fname, 'wb')
# 	writer = csv.writer(csvfile, dialect='excel')
# 	writer.writerow(data.split('\r', 1)[0])
# 	writer.writerows(data.split('\r', 1)[1:])
# 	csvfile.close()
	nowDate = nowDate + oneDay
	
	time.sleep(2)
	
	
# 	CODE FINISH HERE