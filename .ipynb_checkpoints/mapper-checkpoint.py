import csv
import sys
import time

def mapper():
    primeiraLinha = True
    for line in sys.stdin:
	if primeiraLinha:    #skip first line
        	primeiraLinha = False
        	continue
        data = line.strip().split(',')
        index, UNIT, DATEn, TIMEn, Hour, DESCn, ENTRIESn_hourly, EXITSn_hourly, maxpressurei, maxdewpti, mindewpti,minpressurei, meandewpti, meanpressurei, fog, rain,meanwindspdi, mintempi, meantempi, maxtempi, precipi,thunder = data
        print('{0}\t{1}'.format(UNIT, ENTRIESn_hourly))
	
		
mapper()
sys.stdin = open('turnstile_data_master_with_weather.csv')
sys.stdout = open('mapper_result.txt', 'w')
