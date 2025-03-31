

phonebook = {  
    'John': ('209 Trafalgar Road', '905-666-7777'),  
    'Rosie': ('1439 Trafalgar Road', '487-423-7721')    
}

with open('SpeedDial1.txt','w') as speeddialfile:

    for x in phonebook.keys():
        i=1
        for y in ((phonebook.get(x))):
            if i%2==0:
                speeddialfile.writelines(y+"\n")
            i+=1

   
