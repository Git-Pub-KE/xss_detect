import http.client
import urllib.parse
import socket
texts=input()
furl = urllib.parse.urlparse(texts)
urldata = urllib.parse.parse_qsl(furl.query)
dcheck = '{uri.scheme}://{uri.netloc}/'.format(uri=furl)
d = dcheck.replace("https://","").replace("http://","").replace("www.","").replace("/","")
h1=http.client.HTTPConnection(d)
con=h1.connect()
if not con:
    print("YEs")
else:
    print("No")
