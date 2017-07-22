
import csv
listi=[]
num=[]
name=[]
state=[]
prices=[]
header=['id','name','condition','price']
with open('number.csv','r')as file:
    read=csv.reader(file)
    for row in read:
        for x in row:
            if(x!=''):
                num.append(int(x))
            else:
                num.append(x)
print("hello")
#print(num)
with open('fruits.csv','r')as file:
    read=csv.reader(file)
    for row in read:
        for x in row:
            name.append((x))

#print(name)

with open('rotten.csv','r')as file:
    read=csv.reader(file)
    for row in read:
        for x in row:
            if(x=='t'or x=='f'):
                state.append(x)
            elif(x=='0'):
                state.append('f')
            elif(x=='1'):
                state.append('t')
            
#print(state)

with open('price.csv','r')as file:
    read=csv.reader(file)
    for row in read:
        for x in row:
            if(x!=''):
                prices.append(float(x))
            elif(x==''):
                prices.append(0.0)

#print(prices)
for x in range(0,100):
    if(num[x]):
        listi.append({'id':num[x],'name':name[x],'condition':state[x],'price':prices[x]})
    elif(num[x]==''):
        if(x%2!=0):
            listi.append({'id':x,'name':name[x],'condition':state[x],'price':prices[x]})


list_len = len(listi)
print(listi)
for elem in range(0,list_len):
    if(listi[elem]['name']!=''):
        listi[elem]['name']=listi[elem]['name']
    elif(listi[elem]['name']==''):
        #while(listi[elem]['name']!=''):
        listi[elem]['name']=listi[elem-10]['name']

for elem in range(0,list_len):
    if(listi[elem]['condition']=='t'):
        listi[elem]['price']=listi[elem]['price'];
    elif(listi[elem]['condition']=='f'):
        listi[elem]['price']=0.0
        

#print(listi)
with open('data.csv','w')as file:
    writer=csv.DictWriter(file,fieldnames=header)
    writer.writeheader()
    for x in range(0,list_len):
        writer.writerow({'id':listi[x]['id'],'name':listi[x]['name'],'condition':listi[x]['condition'],'price':listi[x]['price']})
print("done..")
    
