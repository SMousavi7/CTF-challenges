# Description of the question:
We have hidden something in the file and I'm sure you won't find it. Make sure to extract the archive using WinRar. Windows is your friend.
# Solution:
In this question they give us a file and we should find the flag in this file. When we extract the file it gives us flag.txt.txt which is 0KB but when we look at the rar file it isn't 0KB which means it has something hidden in it. In windows, we can use Get-Item to see what is in the file. 
First we use command _Get-Item Flag.txt.txt -Stream *_ to get all streams from this file. The result of this command will show you that there is a hidden stream in it called real_flag.txt. Now we can access it -which has flag in it- directly using *notepad Flag.txt.txt:real_flag.txt*. If you want to know more about this question, you can read about NTFS alternate data stream.

**flag: ctf{7ce5567830a2f9f8ce8a7e39856adfe5208242f6bce01ca9af1a230637d65a2d}**
