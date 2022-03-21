# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

ArushiDB = []
# List with dictionary records placed in a list  
ArushiDB.append({  
               "FirstName": "Arushi",  
               "LastName": "Bharadwaj",  
               "DOB": "August 9",  
               "Residence": "San Diego",  
               "Email": "arushi9b@gmail.com",
               "Owns_Devices":     
["phone","TV","fitbit","laptop"
                                      ]  
              })    

x = ArushiDB[0]["Owns_Devices"][3] # Gives "laptop"
y = ArushiDB[0].get("Owns_Devices")[3]

print(x)
print(y)
print (ArushiDB)