file=open("input1.txt","r")
input1=file.readlines()
file.close()
for i in range(len(input1)):
    input1[i]=int(input1[i].replace("\n",""))

prev=int(-1)
curr=int(-1)
greater=int()
for x in input1:
    prev=curr
    curr=x
    if curr>prev and prev!=-1:
        greater+=1
print("{} depth values were larger than the one before it.".format(greater))
print("Got {} total values from file.".format(len(input1)))