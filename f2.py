import pandas as pa
EVENTSF='blitz/co.csv'
stepsScore={}
evensts=open(EVENTSF,'r')
for i in evensts:
    eventData=i.split(',')
    if (eventData[2] in stepsScore)==False:
        stepsScore.update({eventData[2]:0})
    if eventData[1].find('discovered')==-1 and  eventData[1].find('viewed')!=-1:
        stepsScore[eventData[2]]+=1
evensts.close()
df=pa.DataFrame(stepsScore,index=[0])
for x in range(10):
    print(df.idxmax(1)+'    '+str(df.max(1)))
    df[df.idxmax(1)]=0
