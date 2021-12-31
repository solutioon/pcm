# PCM
Python Connection Manager

When I started using MAC I missed putty connection manager. I decided I didn't want a complex tool, just needed a simple script to connect fastly to the list of machines I had in a file, and I also wanted to store the session automatically.

This is the beginning and the mission of Python Connection Manager.

I created an alias in bash_profile to load the script and logging the connection as: alias pcm='python3 /path/pcm.py | tee /path/sesionlog.txt'

I created a csv vm.txt file, with the ip of each machine in every line, a fliendy name and a user:

x.x.x.x,machinaname,user,
x.x.x.x,machinaname,user,
x.x.x.x,machinaname,user,
...

That's all.

