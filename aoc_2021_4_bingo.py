file=open("2021_input4.txt","r")
input4=file.readlines()
file.close()
for i in range(len(input4)):
    input4[i]=input4[i].replace("\n","")

for val in input4:
    if val=="":
        input4.remove(val)
    
won_at_step=list()
draw=input4[0].split(",")
input4.pop(0)

def check_column(lines,index,drawn):
    line=list()
    drawn_on_line=int()
    for x in lines:
        line.append(x[index])
    for x in drawn:
        if x in line:
            drawn_on_line=drawn_on_line+1
    if drawn_on_line==5:
        return True
    else:
        return False

def check_row(lines,line_num,drawn):
    line=list()
    drawn_on_line=int()
    line.extend(lines[line_num])
    for x in drawn:
        if x in line:
            drawn_on_line=drawn_on_line+1
    if drawn_on_line==5:
        return True
    else:
        return False

def new_board(inputlist,num):
    board=[]
    for i in range(num*5,(num*5)+5):
            board.append(inputlist[i].split())
    return board

class Bingo_board:
    lines=list()
    drawn_nums=list()
    steps=int()

curr=Bingo_board
for i in range(len(input4)//5):
    curr.lines.clear()
    won=False
    curr.drawn_nums.clear()
    curr.steps=int()
    curr.lines=new_board(input4,i)
    for x in draw:
        curr.drawn_nums.append(x)
        curr.steps=curr.steps+1
        for num in range(5):
            if check_column(curr.lines,num,curr.drawn_nums) or check_row(curr.lines,num,curr.drawn_nums):
                won_at_step.append(curr.steps)
                won=True
                break
        if won:
            won=False
            break
del curr
print("Slowest board win at step {}, on board num {}/99".format(max(won_at_step),won_at_step.index(max(won_at_step))))

def n_lists_to_1(lines):
    line=list()
    for i in range(len(lines)):
        line.extend(lines[i])
    return(line)

winner_board=n_lists_to_1(new_board(input4,won_at_step.index(min(won_at_step))))
winning_num=draw[min(won_at_step)-1]
last_board=n_lists_to_1(new_board(input4,won_at_step.index(max(won_at_step))))
last_num=draw[max(won_at_step)-1]

step=int()
deletable=str()
while deletable!=last_num:
    step=step+1
    deletable=draw[step]
    if deletable in last_board:
        last_board.remove(deletable)
for i in range(len(last_board)):
    last_board[i]=int(last_board[i])
l_sum=sum(last_board)
print(int(last_num)*l_sum)