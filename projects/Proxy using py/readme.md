A way to use proxy in your python programs.

simply add the dictionary like this
proxies = {
'http': 'http://proxy_ip:port',
'https': 'http://proxy_ip:port'
}

And connect it to your response

Note: the proxy server ary time to time so may not work if not then chnage the proxy server ip and port in the below proxies dictionary

You can also authenticate by adding the username and password
