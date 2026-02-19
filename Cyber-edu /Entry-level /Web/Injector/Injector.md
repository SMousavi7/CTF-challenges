# Description of the question
Try harder!!
# Solution
This is a command injection. For running our commands first we put a ; to finisht the statement. Now we can inject any command we want. First we use ls to see what is in the server. The result of this command tells us that we have 2 files: 
1. flag.php
2. index.php
When we enter cat flag.php, no result appears but when enter cat index.php the server code appears. It tells us that it is sensitive to the command cat flag.php and we should bypass it somehow. There are so many options here to use but I used commad *rev* and when I get my result, I reversed it again to get the correct flag.

**flag: CTF{C0mm4nd_1nj3c5i0n_1s_E4sy}**
