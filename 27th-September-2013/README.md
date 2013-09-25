HTML & CSS
========

How does the web work?

![DNS Service](http://static.ddmcdn.com/gif/dns-rev-1.gif "DNS Server")

1. You put the name of the domain you want to go to - ie: "http://nyusw.com"
2. The DNS (Domain Name Server) server is a kind of a "router". You ask it where the website you want to find is, and it points you to it. It gives you an IP address.
3. There are multiple DNS servers, and if one doesn't know the IP address then it asks another one.
4. Your computer now knows the specific IP address (or the magical number) of the website or the server where it's located. The servers hold the web files, and when you request that IP address you make a request to the server for the rendered HTML files, and the server will send you back a response.
5. A server can send back HTML, CSS, or Javascript. These are then rendered by your browser, and displayed to you.

Lets try put in the IP address of the domain "http://nyusw.com": "192.237.249.194". Is the output the same? It should be!

How can I get started?!

1. Make a folder for your website, and name it the project name. 
2. The main page on your basic HTML website will always be "index.html" (Do NOT change this). By default - the server will send back a file called "index.html", and if it isn't found it'll return "404 not found".
3. Create sub folders for "css", "images", "javascript", etc. <- according to what you need.