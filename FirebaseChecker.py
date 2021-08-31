# Auther: Shawal Ahmad Mohmand
# Info: Simple Python Script that check Insecure Firebase Databases Permissions(readable/writeable). this type of insecure/vulnerable database mostly found in mobile application.
print ("""
╔═╗┬┬─┐┌─┐┌┐ ┌─┐┌─┐┌─┐              
╠╣ │├┬┘├┤ ├┴┐├─┤└─┐├┤               
╚  ┴┴└─└─┘└─┘┴ ┴└─┘└─┘              
╔╦╗┌─┐┬┌─┌─┐╔═╗┬  ┬┌─┐┬─┐           
 ║ ├─┤├┴┐├┤ ║ ║└┐┌┘├┤ ├┬┘           
 ╩ ┴ ┴┴ ┴└─┘╚═╝ └┘ └─┘┴└─           
╦  ╦┬ ┬┬  ┌┐┌┌─┐┬─┐┌─┐┌┐ ┬┬  ┬┌┬┐┬ ┬
╚╗╔╝│ ││  │││├┤ ├┬┘├─┤├┴┐││  │ │ └┬┘
 ╚╝ └─┘┴─┘┘└┘└─┘┴└─┴ ┴└─┘┴┴─┘┴ ┴  ┴ """)
print("""
╔═╗┬ ┬┌─┐┬ ┬┌─┐┬    ╔═╗┬ ┬┌┬┐┌─┐┌┬┐  ╔╦╗┌─┐┬ ┬┌┬┐┌─┐┌┐┌┌┬┐
╚═╗├─┤├─┤│││├─┤│    ╠═╣├─┤│││├─┤ ││  ║║║│ │├─┤│││├─┤│││ ││
╚═╝┴ ┴┴ ┴└┴┘┴ ┴┴─┘  ╩ ╩┴ ┴┴ ┴┴ ┴─┴┘  ╩ ╩└─┘┴ ┴┴ ┴┴ ┴┘└┘─┴┘
""")

print ("""
<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>
+                                                                       +
+   Auther: Shawal Ahmad Mohmand                                        +
+   Info  : Simple Python Script that check Insecure Firebase           +
+           Databases Permissions(readable/writeable). this type of     +   
+           insecure/vulnerable database mostly found in mobile         +
+           application.                                                +
+   Video:  https://www.youtube.com/watch?v=mnTLrNrk93Q                 +
+                                                                       +     
<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>
""")
import requests

site_name = input("[+] Enter firebase database name : ")
path = input("[+] Enter filename(create in firebase) : ")

payload = { "message": "Data writebale!!" }

res = requests.put("https://"+site_name+".firebaseio.com/"+path+".json", json=payload)

print("\n<+=================================================+>\n")
if res.status_code == 200:
    print("[>] Data is writable!")
    print("Visit: https://"+site_name+".firebaseio.com/"+path+".json")
else:
    print("[x] Not Vulnerable! (attacker not allowed to write data)")


get_res = requests.get("https://"+site_name+".firebaseio.com/"+path+".json")

print("\n<+=================================================+>\n")
if get_res.status_code == 200:
    print("[>] Data is readable! (allow attacker to read data) Status code:", get_res.status_code)
    print("[>] Response:", get_res.text)
elif get_res.status_code == 401:
    print("[>] Permission Denied! (attacker not allowed to read data) Status code:", get_res.status_code)
elif get_res.status_code == 404:
    print("[>] Please check your firebase url! Status code:", get_res.status_code)
else:
    print("[x] Unkown Error Status code:", get_res.status_code)