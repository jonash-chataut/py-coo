A way to use proxy in your python programs.

simply add the dictionary like this
proxies = {
'http': 'http://103.160.205.86:8080',
'https': 'http://103.160.205.86:8080'
}

And connect it to your response

Note: the proxy server ary time to time so may not work if not then chnage the proxy server ip and port in the below proxies dictionary
