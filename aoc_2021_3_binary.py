file=open("2021_input3.txt")
input3=file.readlines()
file.close()

gamma=""
epsilon=""

for i in range(0,len(input3)):
    input3[i]=input3[i].replace("\n","")

def binary_bit_count(list,index):
    z=0
    o=0
    for x in list:
        if x[index]=="0":
            z+=1
        else:
            o+=1
    if z>o:
        return "0"
    else:
        return "1"

def yabba_dabba(bit):   #i have given up on making this slightly readable at all
    if bit=="0":
        return "1"
    else:
        return "0"

for i in range(12):
    gamma=gamma+binary_bit_count(input3,i)
    if gamma[len(gamma)-1]=="0":
        epsilon=epsilon+"1"
    else:
        epsilon=epsilon+"0"
print(int(gamma,2))
print(int(epsilon,2))
print(int(gamma,2)*int(epsilon,2))

temp_l=input3.copy()
temp_g=input3.copy()
for i in range(12):
    if len(temp_g)<2:
        break
    bit=binary_bit_count(temp_g,i)
    temp_g=[x for x in temp_g if bit in x[i]]

for i in range(12):
    if len(temp_l)<2:
        break
    bit=yabba_dabba(binary_bit_count(temp_l,i))
    temp_l=[x for x in temp_l if bit in x[i]]
oxy=int(temp_g[0],2)
co2=int(temp_l[0],2)
print(oxy*co2)
