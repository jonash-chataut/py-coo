<h2>
A way to use proxy in your python programs.
</h2>
<h3>
simply add the dictionary like this
</h3>
<p>
proxies = {<br>
'http': 'http://proxy_ip:port',<br>
'https': 'http://proxy_ip:port'<br>
}
</p>
<h3>
And connect it to your response
</h3>
<i>
Note: the proxy server ary time to time so may not work if not then chnage the proxy server ip and port in the below proxies dictionary
</i>

<h3>
Website I used to get proxy ip and port: https://www.proxynova.com/proxy-server-list/
</h3>
<h3>
You can also authenticate by adding the username and password:
</h3>
<p>
proxies = {<br>
    'http': 'http://username:password@proxy_ip:port',<br>
    'https': 'http://username:password@proxy_ip:port',<br>
}
</p>
