octopusKey="1254117228441687322483543815531372637614558653855372133334273571362825168112624387183121385254266347"
octopusList=list(octopusKey)
xList=[]
yList=[]
flashFrom=[]
flashTo=[]
flashable=((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

def coordinates(id):
    y=id//10
    x=id-y*10
    coordinates=[x,y]
    return coordinates

def normalStep(val,x,y):
    a=val+1
    if a==10:
        a=0
        flashFrom.append((x,y))
    return a

def flashCoordinates(x,y):
    updateX=[]
    updateY=[]
    a=0
    while a<8:
        flashableCoords=flashable[a]
        nx=x+flashableCoords[0]
        ny=y+flashableCoords[1]
        print(nx)
        print(ny)
        if nx>9 or nx<0 or ny>9 or ny<0:
            fBool=False
        else:
            fBool=True
        if fBool:
            updateX.append(nx)
            updateY.append(ny)
        a+=1
    updateCoords=[updateX,updateY]
    print(updateCoords)
    return updateCoords

for i in range(0,len(octopusList)):
    octopusList[i]=int(octopusList[i])
    temp=coordinates(i)
    xList.append(temp[0])
    yList.append(temp[1])

while True:
    for i in range(0,len(octopusList)):
        octopusList[i]=normalStep(octopusList[i],xList[i],yList[i])
    for a in flashFrom:
        flashTo.append(flashCoordinates(a[0],a[1]))
    flashFrom.clear()
    for a in flashTo[0]:
        id=flashTo[1][a]*10+flashTo[0][a]
        octopusList[id]=normalStep(octopusList[id],xList[id],yList[id])
    flashTo.clear()
    while 10 in octopusList:
        for a in flashFrom:
            flashTo.extend(flashCoordinates(a[0],a[1]))
        flashFrom.clear()
        for a in flashTo[0]:
            id=flashTo[1][a]*10+flashTo[0][a]
            octopusList[i]=normalStep(octopusList[id],xList[id],yList[id])
        flashTo.clear()
    print(octopusList)
    input("...")
    flashFrom.clear()
    flashTo.clear()