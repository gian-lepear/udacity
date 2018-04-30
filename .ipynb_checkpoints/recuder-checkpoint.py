def reducer():
    ENTRIESn_hourlyTotal =0
    oldUNIT = None
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) != 2:
            continue
        thisUNIT, thisENTRIES = data
        
        if oldUNIT and oldUNIT != thisUNIT:
            print('{0}\t{1}'.format(oldUNIT, ENTRIESn_hourlyTotal))
        
            ENTRIESn_hourlyTotal = 0
        oldUNIT = thisUNIT
        ENTRIESn_hourlyTotal += float(thisENTRIES)
        
        if oldUNIT == None:
            print('{0}\t{1}'.format(oldUNIT, ENTRIESn_hourlyTotal))
			
reducer()