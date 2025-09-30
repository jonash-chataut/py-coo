import requests

# creating a dictionary proxies to enable proxies in the code
# the proxy server ary time to time so may not work if not then chnage the proxy server ip and port in the below proxies dictionary
proxies = {
    'http':  'http://103.160.205.86:8080',
    'https': 'http://103.160.205.86:8080'
}


response = requests.get("https://ipinfo.io/json", proxies=proxies)

if response.status_code == 200:
    data=response.json()
    print("Your IP Address:",data.get("ip"))
    print("Your city:",data.get("city"))
    print("Your Region:",data.get("region"))
    print("Your country:",data.get("country"))
else:
    print("Failed to get IP info")
