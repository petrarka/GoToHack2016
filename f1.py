COSTSF='blitz/co2.csv'
EVENTSF='blitz/co.csv'
def readCosts(fname):
    costsFile=open(fname)
    costs={}
    for line in costsFile:
        line=line.split(',')
        costs.update({line[5]:line[8][0]})
    return  costs
b=0
for v in readCosts(COSTSF).values():
    b+=int(v, 10)
print(b)
