# Firebase Database Permissions Check:
Simple Python Script that check Insecure Firebase Databases Permissions(read/write). this type of insecure/vulnerable database mostly found in mobile application.

# Insecure/Vulnerable Firebase Databases:
Insecure/Vulnerable Firebase Databases are those databases in which firebase rules are allow for all users.
```json
    {
        "rules": {
            ".read": true,
            ".write": true,
        }
    }
```

# How to Find Insecure/Vulnerable Firebase Databases in Mobile Applications:
[![Concept Video](https://img.youtube.com/vi/mnTLrNrk93Q/0.jpg)](https://www.youtube.com/watch?v=mnTLrNrk93Q)

# How to Secure Insecure/Vulnerable Firebase Databases:
To secure in Insecure/Vulnerable Firebase Database Goto ```https://console.firebase.google.com/```. Select your project >> Goto Realtime Database(from left side bar) >> Click on Rules. Update your Rules from 
```json
    {
        "rules": {
            ".read": true,
            ".write": true,
        }
    }
```
to
```json
    {
        "rules": {
            ".read": false,
            ".write": false,
        }
    }
```

# Script Usage: 

Open Terminal and Run ```pip3 install -r requirements.txt``` to install requirements.

Now ```python3 FirebaseChecker.py``` to run your script.
Enter your target firebase database uri e.g ```your_project``` from ```https://your_project.firebaseio.com/```.
Then Enter your path your you want to write data to check permissions.

# Usage Attachment:
![alt Usage Attachment](https://github.com/criticalmiind/CheckInsecureFirebaseDatabases/blob/main/images/ss01.png)
```
[+] Enter firebase database name : your_project
[+] Enter filename(create in firebase) : test
```

# Thanks You All

Subscribe my youtube: https://www.youtube.com/c/shawalahmadmohmandofficail
