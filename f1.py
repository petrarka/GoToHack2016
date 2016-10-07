COSTSF='blitz/co2.csv'
EVENTSF='blitz/co.csv'
def readCosts(fname):
    costsFile=open(fname)
    costs={}
    for line in costsFile:
        line=line.split(',')
        costs.update({line[5]:int(line[8][0])})
    costsFile.close()
    return  costs
usersScore={}
usersTime={}
usersFinish={}
costs=readCosts(COSTSF)
evensts=open(EVENTSF,'r')
for i in evensts:
    eventData=i.split(',')
    if (eventData[0] in usersTime) == False:
        usersTime.update({eventData[0]:eventData[-1]})
        usersScore.update({eventData[0]:0})
    if eventData[1].find('passed')!=-1:
        usersScore[eventData[0]]+=costs[eventData[-2]]
        if usersScore[eventData[0]]>=24 and (eventData[0] in usersFinish)==False :
            usersFinish.update({eventData[0]:eventData[-1]})
print(str(len(usersTime))+' :user strarted, user fineshed: '+str(len(usersFinish)))
for user in usersFinish:
    usersFinish[user]=int(usersTime[user])-int(usersFinish[user])
print(usersFinish)
for x in range(10):
    print(str(x)+'    '+str(usersFinish[min(usersFinish)]))
    usersFinish.pop(min(usersFinish))
