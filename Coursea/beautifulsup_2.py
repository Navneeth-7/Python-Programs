from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter link: ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
count = int(input("Enter count:"))
position=int(input("Enter position:"))
name=list()
for x in range(1,count+1):
    tags = soup("a")
    my_tags = tags[position - 1]
    a = tags[position - 1].contents[0]
    name.append(a)
    #print(tags[position-1].contents[0])
    needed_tag = my_tags.get('href', None)
    url = str(needed_tag)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    #print(my_tags.get('href', None))
print(name[-1])

    #  print 'TAG:',tag
    #    print('URL:',tag.get('class', None))
    #    print('Contents:',tag.contents[0])
#     #   print 'Attrs:',tag.attrs
#     count = int(tag.contents[0]) + count
# print(count)

# count = int(input("Enter count:"))
# position = int(input("Enter position:"))


#     # tags = soup("a")
#     # my_tags = tags[position - 1]
#     # print(my_tags)