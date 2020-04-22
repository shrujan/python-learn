
#6_urllib2_demo.py
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
print(html)
   
"""
#In Python 2 - below code works-
import urllib2
#req = urllib2.Request('https://www.python.org/')

req = urllib2.Request('http://www.google.com')
response = urllib2.urlopen(req)
the_page = response.read()
print (the_page)
"""




"""
if any issue in network connectivity do this--->

>set HTTP_proxy=http://ptbc1.persistent.co.in:8080/
>set HTTPS_proxy=https://ptbc1.persistent.co.in:8080/



set HTTP_PROXY=http://sakshi_jamgaonkar:password@ptbc1.persistent.co.in:8080







"""
