import csv
listi=[]
with open("rotten.csv",'r+')as file:
    read=csv.reader(file)
    for row in list(read)[0]:
        if(row=="1"):
            row ='t'
        elif(row=="0"):
            row ='f'
            #print("f done")
        listi.append(row)
            
with open("rotten.csv",'w')as file:
    writer=csv.writer(file)
    writer.writerows(listi)
    
