
import requests

# resp = requests.get("http://httpbin.org/get")

# print(resp.text)

# print("===============================\n")

# print("Status Code: {}".format(resp.status_code))

# print("Content-Length: {}".format(resp.headers['Content-Length']))

# print("Server: {}".format(resp.headers['Server']))

# if resp.status_code != 200:
#     print("Page Not Found!")

# else:
#     print("This Page exists")


# resp2 = requests.get('http://httpbin.org/get',params={"id":"1"})   #sending a get parameter


# print(resp2.url)

# resp3 = requests.get('http://httpbin.org/get', params={"id":"2"}, headers={"My-Header":"yay","test-header":"Test"})  #sending a get parameter with headers

# print(resp3.text)

# headers = {"X-POST":"YAY"}

# data = {"username":"Admin"}

# resp4 = requests.post('http://httpbin.org/post', headers = headers, data = data)

# print(resp4.text)  # POST request response with headers and post data or post params

# # Sending a file using multipart form data

# headers = {"X-Image": "Uploaded"}
# files = {"file": open('google.png', 'rb')}

# resp5 = requests.post("http://httpbin.org/post", headers = headers, files = files)

# print(resp5.text)


# #Authorization Basic \/\/\/Tuple

# auth = ('admin','password')       # as tuple

# resp6 = requests.get('http://httpbin.org/get', auth = auth)


# print(resp6.text)

# print("-------------")

# auth = ('admin', 'password')       # auth is send as a tuple.
# headers = {'X-Basic-Auth': 'Done', 'User-Agent':'Firefox 60.1'}

# resp = requests.get('http://httpbin.org/get', auth = auth, headers = headers)

# print(resp.text)


# # resp2 = requests.get('http://expired.badssl.com', verify = False) #dont verify ssl certificate
# print("-----------------")

# resp3 = requests.get('http://github.com', allow_redirects = False) #dont allow redirects.

# print(resp3.headers)

# resp4 = requests.get('http://httpbin.org/get', timeout = 0.1)

# print(resp4.content)

# cookies and Sessions..


resp = requests.get('http://httpbin.org/cookies', cookies = {'phpsessid': 'svags16162vb'})

print(resp.content)

# For a cookie sent in a request for another request we have to send the cookies everytime, hence sessions helps us.


resp_sess = requests.Session()

resp_sess.cookies.update({'token': 'eyjanbbahstagsavs.xbxhsaa.snjaop'})


print(resp_sess.get('http://httpbin.org/cookies').text)

print(resp_sess.get('http://httpbin.org/cookies').text)

print(resp_sess.get('http://httpbin.org/cookies').text) #session is attached to the request


x = requests.get('https://api.github.com/events')

print(x.json())

y = requests.get('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')

with open('image2.png', 'wb') as f:
	f.write(y.content)


print("-------------------")

print("Go through requests documentation..")