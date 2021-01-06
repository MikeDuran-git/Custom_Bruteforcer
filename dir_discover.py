import requests as req

target_url= input("[+] Enter the page URL: ") # input the webpage we want to input
file_name= input("[+] Enter file name containing directories: ") # input the webpage we want to input

def request(url):
    try:
        return requests.get("http://"+ url)
    except requests.exceptions.ConnectionError:
        pass
    pass

file = open(file_name,'r')
for line in file:
    directory= line.strip()
    full_url = target_url + '/' + directory
    response= request(full_url)
    if response:
        print("[*] Discovered directory at this Path: "+ full_url)