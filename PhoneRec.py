import json

phonebook = {  
    'John': ('209 Trafalgar Road', '905-666-7777'),  
    'Rosie': ('1439 Trafalgar Road', '487-423-7721')    
}

with open('PhoneBook.json','w') as file: 
    json.dump(phonebook,file)


with open('PhoneBook.json','rt') as file: 
    obj=json.load(file)
    with open('SpeedDial1.txt','w') as speeddialfile:

        for x in dict(obj).keys():
            i=1
            for y in ((dict(obj).get(x))):
                if i%2==0:
                    speeddialfile.writelines(y+"\n")
                i+=1

   
