
# Network algorithms

The following algorithms are presented in this project:
* Algorithm Dijkstra;
* Algorithm Ford-Bellman;
* Algorithm Maximum flow;
* Reservation in communication networks.

# Install Python and Git
Before start this project you should install:
* install [Python3](https://www.python.org/downloads/);
* install [Git](https://git-scm.com/).

On Linux (Dedian) **terminal** you can do this with commands:
```
$ sudo apt-get update
$ sudo apt-get install -y python3
$ sudo apt-get install -y git
```
On Windows  **Powershell**   with administrator privileges :
```
> Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
> choco install -y python3
> choco install -y git
```

# Start project
For normal work project you should install python environment.

*On Linux (Dedian):*
```
$ cd /home/$(whoami)/Downloads
$ git clone https://github.com/Moon1705/network_USIOI.git
$ cd network_USIOI
$ pip3 install -r requirements.txt
```
*On Windows :*
```
> cd "C:\Users\$env:UserName\Downloads\"
> & 'C:\Program Files\Git\bin\git.exe' clone https://github.com/Moon1705/network_USIOI.git
> cd network_USIOI
> pip3 install -r requirements.txt

```

And start project!

*On Linux (Dedian):*
```
$ python3 main.py
```
*On Windows:*
```
> python main.py
```
# Delete project
  
If the project is no longer needed.
*On Linux (Dedian):*
```
$ cd ..
$ rm -rf network_USIOI
$ sudo apt-get uninstall -y python3
$ sudo apt-get uninstall -y git
```
*On Windows:*
```
> cd ..
> remove-item -force -recurse -path .\network_USIOI\
> choco uninstall python3
> choco uninstall git
> remove-item -force -recurse -path C:\ProgramData\chocolatey
```
