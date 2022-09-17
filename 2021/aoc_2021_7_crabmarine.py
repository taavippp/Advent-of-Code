file=open("2021_input7.txt","r")
input7=file.readlines()
file.close()
input7=input7[0].split(",")
for i in range(len(input7)):
    input7[i]=int(input7[i])

lil_crab=min(input7)
big_crab=max(input7)
fuel={}

def all_before(num):
    nums=[]
    for i in range(0,num+1):
        nums.append(i)
    return sum(nums)

def fuel_usage(list,num):
    fuel_used=0
    for x in list:
        if x>num:
            fuel_used=fuel_used+(all_before(x-num))
        elif x<num:
            fuel_used=fuel_used+(all_before(num-x))
        else:
            continue
    return fuel_used

prev1=int()
prev2=int()
curr=int()
for i in range(lil_crab,big_crab):
    prev2=prev1
    prev1=curr
    curr=fuel_usage(input7,i)
    fuel.update({i:curr})
    if curr>prev1 and prev2>prev1:
        break
print(min(fuel.values()))
