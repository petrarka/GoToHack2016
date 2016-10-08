EVENTSF='blitz/co.csv'
stepsScore={}
evensts=open(EVENTSF,'r')
for i in evensts:
    eventData=i.split(',')
    if (eventData[2] in stepsScore)==False:
        stepsScore.update({eventData[2]:0})
    if eventData[1].find('discovered')==-1 and  eventData[1].find('viewed')!=-1:
        stepsScore[eventData[2]]+=1
print(stepsScore)
for x in range(10):
    print(max(stepsScore))
    print(stepsScore[max(stepsScore)])
    stepsScore.pop(max(stepsScore))
