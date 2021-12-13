file=open("2021_input1.txt","r")
input1=file.readlines()
file.close()
for i in range(len(input1)):
    input1[i]=int(input1[i].replace("\n",""))

prev=int(-1)
curr=int(-1)
greater=int()
prev_w=int(-1)
curr_w=int(-1)
greater_w=int()

for x in range(len(input1)):
    prev=curr
    curr=input1[x]
    if curr>prev and prev!=-1:
        greater+=1
    if x>=2:
        prev_w=curr_w
        curr_w=input1[x-2]+input1[x-1]+input1[x]
        if prev_w!=-1 and curr_w>prev_w:
            greater_w+=1

print("{} depth values were larger than the one before it.".format(greater))
print("{} three-value windows were greater than the previous one.".format(greater_w))
print("Got {} total values from file.".format(len(input1)))