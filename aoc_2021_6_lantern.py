file=open("2021_input6.txt","r")
input6=file.readlines()
file.close()
input6[0]=input6[0].replace("\n","")
input6=input6[0].split(",")
for i in range(len(input6)):
    input6[i]=int(input6[i])

fish=dict()

def count_num(list,num):
    counter=int()
    for i in range(len(list)):
        if list[i]==num:
            counter=counter+1
    return counter

def count_dict(dict):
    sum=0
    for x in dict:
        sum=sum+dict[x]
    return sum

def growth(dict):
    n_dict=dict.copy()
    value=int()
    for key in n_dict:
        value=n_dict[key]
        if key==0:
            n_dict[9]+=value
            n_dict[7]+=value
            n_dict[key]-=value
        else:
            n_dict[key-1]+=value
            n_dict[key]-=value
    return n_dict

for i in range(10):
    fish.update({i:count_num(input6,i)})

while True:
    fish_new=fish.copy()
    num=int(input("How many days would you like to let the lanternfish grow for? Starts at 300\n"))
    for i in range(num):
        fish_new=growth(fish_new)
    print(count_dict(fish_new))