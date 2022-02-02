f = open("textfile.txt", "r")
data = []
for x in f:
    data.append(x)
    
del data[0]

clean_data = []
for i in data:   
    clean_data.append(i.replace('\n',''))
    
newlist = []
for i in clean_data:    
    newlist.append(i.split(' ',))
    

print(newlist)
#not finish yet