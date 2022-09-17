file=open("2021_input5.txt")
input5=file.readlines()
file.close()
start=[]
end=[]
for i in range(len(input5)):
    input5[i]=input5[i].replace("\n","")
    temp=input5[i].split(" -> ")
    start.append(temp[0].split(","))
    end.append(temp[1].split(","))