import json

phonebook = {  
    'John': ('209 Trafalgar Road', '905-666-7777'),  
    'Rosie': ('1439 Trafalgar Road', '487-423-7721')    
}

with open('Speeddial2.json','w') as file: 
    json.dump(phonebook,file,indent=4)


with open('Speeddial2.json','rt') as file: 
    obj=json.load(file)  
    print(json.dumps(obj, indent=4))

   
