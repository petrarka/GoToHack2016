from collections import OrderedDict
usersFinish={'d':2,'f':3,'dd':32,'ff':33,'ff2':333,'ff3':3333,'ff4':333333}
for x in range(10):
    print(str(x)+'    '+str(usersFinish[min(usersFinish)]))
    usersFinish.pop(min(usersFinish))
