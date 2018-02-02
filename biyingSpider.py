import requests
import re
import time
local = time.strftime("%Y.%m.%d")
url = 'http://cn.bing.com/'
con = requests.get(url)
content = con.text
# reg = r"(http://s.cn.bing.com/az/hprichbg/rb/.*?.jpg)"
reg = r"(/az/hprichbg/rb/.*?.jpg)"
a = re.findall(reg, content, re.S)[0]
print("https://cn.bing.com"+a)
read = requests.get("https://cn.bing.com"+a)
f = open('%s.jpg' % local, 'wb')
f.write(read.content)
f.close()
