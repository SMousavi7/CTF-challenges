# Description of the question:
Find the vulnerability and get the flag. The flag is located in a temporary folder.

Flag format: CTF{sha256}
# Solution:
After entering the IP and port given in the question, we see this image:
![local](https://github.com/user-attachments/assets/3a1aaff7-c2b5-4b68-acc3-03e115b854a8)
First, I used developer tools to see the structure of the page. Then, I saw this in image tag of its HTML: `<img src="local?image_name=static/path.jpg" align="middle">`. So, I decided to test IP:PORT/local and it brought me another page with "TRY HARDER!" sentence on it. I tested some other things in URL and realized it has **Path traversal** or **Directory traversal** vulnerability. So, I tested local?image_name=static/....//....//....//....//tmp/flag in URL and a file was downloaded in my PC and it had flag in it.

**flag: CTF{0caec419d3ad1e1f052f06bae84d9106b77d166aae899c6dbe1355d10a4ba854}**
