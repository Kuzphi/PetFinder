import urllib
import urllib2
import re
prefix = "https://www.petfinder.com/"
url = "https://www.petfinder.com/pet-search?location=92617"
value  = {"Location":"92617"}
data = urllib.urlencode(value)
response = urllib2.urlopen(url)
html = response.read()
print html 

# pattern = re.complie(r'href="*"')
