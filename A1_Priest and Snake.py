#!/usr/bin/env python
# coding: utf-8

# In[6]:


#N
N=int(input())
M=int(input())
snake_infos = []
for _ in range(M):
    snake_input = input("Enter snake information (start_block, end_block): ").split()
    start_block = tuple(map(int, snake_input[0].split(',')))
    end_block = tuple(map(int, snake_input[1].split(',')))
    snake_infos.append([start_block, end_block])

# Full Snakes's blocks
snake_info_list = snake_infos
#GOING DIR
snake_info_list_going_dir=[]
for snake_info_inner_list in snake_info_list:
    i1=snake_info_inner_list[0][0]
    i2=snake_info_inner_list[1][0]
    j1=snake_info_inner_list[0][1]
    j2=snake_info_inner_list[1][1]
    #print(i1,i2,j1,j2)
    if i1==i2:  
        if j1<j2:
            j1=j1+1
            snake_info_list_going_dir.append("W")
            while(j1<j2):
                snake_info_inner_list.append((i1,j1))
                j1=j1+1
        elif j1>j2:
            j1=j1-1
            snake_info_list_going_dir.append("E")
            while(j1>j2):
                snake_info_inner_list.append((i1,j1))
                j1=j1-1
    elif j1==j2:  
        if i1<i2:
            i1=i1+1
            snake_info_list_going_dir.append("N")
            while(i1<i2):
                snake_info_inner_list.append((i1,j1))
                i1=i1+1
        elif i1>i2:
            i1=i1-1
            snake_info_list_going_dir.append("S")
            while(i1>i2):
                snake_info_inner_list.append((i1,j1))
                i1=i1-1

#snake_info_list1
def movr_per_unit(snake_info_list,snake_info_list_going_dir):
    dir=0
    new_snake_info_list=[]
    for snake_info_inner_list in snake_info_list:
        new_snake_inner_info_list=[]
        d= snake_info_list_going_dir[dir]
        if d=="N":
            for (t1,t2) in snake_info_inner_list:
                if(t1==0):
                    t1=N
                t1=t1-1
                if(t1==0):
                    t1=N
                new_snake_inner_info_list.append((t1,t2))
        elif d=="S":
            for (t1,t2) in snake_info_inner_list:
                if(t1==N+1):
                    t1=1
                t1=t1+1
                if(t1==N+1):
                    t1=1
                new_snake_inner_info_list.append((t1,t2))
        elif d=="E":
            for (t1,t2) in snake_info_inner_list:
                if(t2==N+1):
                    t2=1
                t2=t2+1
                if(t2==N+1):
                    t2=1
                new_snake_inner_info_list.append((t1,t2))
        elif d=="W":
            for (t1,t2) in snake_info_inner_list:
                if(t2==0):
                    t2=N
                t2=t2-1
                if(t2==0):
                    t2=N
                new_snake_inner_info_list.append((t1,t2))
        new_snake_info_list.append(new_snake_inner_info_list)
       
        dir=dir+1
    return new_snake_info_list

all_Snake_lists_N=[]
all_Snake_lists_N.append(snake_info_list)
for i in range(1,N):
    snake_info_list=movr_per_unit(snake_info_list,snake_info_list_going_dir)
    all_Snake_lists_N.append(snake_info_list)

Priest=input()
i=Priest[0]
x=int(Priest[1])

POS=0
if i=="N":
    POS=(1,x)   
elif i=="S":
    POS=(N,x) 
elif i=="W":
    POS=(x,1)
else:
    POS=(x,N)

def mov_priest(p,d):
    if d=="S":
        new_p=(p[0]-1,p[1])
    elif d=="N":
        new_p=(p[0]+1,p[1])
    elif d=="E":
        new_p=(p[0],p[1]+1)
    elif d=="W":
        new_p=(p[0],p[1]-1)
    return new_p
def is_tuple_present(list_of_lists, input_tuple):
    for sublist in list_of_lists:
        if input_tuple in sublist:
            return True
    return False

for i in range(1, N+1):
 
    result = is_tuple_present(all_Snake_lists_N[i-1], POS)
    
    if result:
        print(POS)
        break 
    POS = mov_priest(POS, Priest[0])

if not result:
    print("NIRVANA")


# In[ ]:




