# It's a simple script to brute force directories and file names on web servers

import urllib.request                                                        
import sys                                                              

def dirAttack():
    host = sys.argv[1]                                               
    wordlist_file = sys.argv[2]                                                  
    data = open(wordlist_file)                                                        
    words = data.readlines()      


    for line in words: 
        word = line.strip("\n")
        req_url = "{0}/{1}".format(host, word) 
        if "http" not in req_url:     
            req_url = "http://" + req_url 
        try: 
            req = urllib.request.urlopen(req_url) 
            if req.getcode() == 200: 
                print("[+] {0}/{1} is Found (200)".format(host, word)) 
        except: 
            pass 


if len(sys.argv) == 3:
    dirAttack()
else:
    print("You need to specify the IP address and a wordlist file")
    print("Example: python3 dirAttack.py IP wordlist.txt")
