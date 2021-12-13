file=open("2021_input2.txt","r")
input2=file.readlines()
file.close()

x=0
y=0
aim=0

for val in input2:
    val=val.replace("\n","")
    val_data=val.split()
    num=int(val_data[1])
    if val_data[0]=="forward":
        x+=num
        y=y+(aim*num)
    elif val_data[0]=="down":
        aim+=num
    elif val_data[0]=="up":
        aim-=num
print("Final aim was {}".format(aim))
print("Horizontal pos. {}\nVertical pos. {}\nMultiplication: {}".format(x,y,x*y))