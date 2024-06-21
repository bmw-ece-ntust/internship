## Reconnaisance
Passive information gathering, in general, there are four ways to do this
* Collecting Emails: Gather all valid emails from a company, for example, for the company Target.com, find emails with the domain @target.com.
* Collecting Subdomains: Gather both common and uncommon subdomains, such as finance.target.com and support.target.com.
* Dorking: Use Google to search for sensitive information about the target by using specific keywords (this can also be applied to GitHub).
* Collecting Breached Credentials: Search for data that has been breached previously.

## Red Team Tools for Reconnaisance

### Collecting Emails
* Hunter.io, Partially free, but it can provide the most common email patterns (i personally prefer this).
* Phonebook.cz, Completely free, allows users to enter a domain, URL, or email, but only displays information without additional analysis.

### Collecting Subdomains
* Censys.io, similiar to NMap, but can search up to Ports, Services, and IP. Users can also search for subdomains directly from here by viewing the domain names obtained.
* Mxtoolbox, users can input the ASN number of a company to locate its IP range.
* DNSDumpster, users can take the IP obtained from MXtoolbox and input one of its ranges here to retrieve subdomains/DNS records (make sure to input the range, not just a single IP -> .0/24).
* The Harvester, The Harvester is a powerful built-in Linux tool designed for gathering email addresses, IP addresses, and subdomains associated with a target domain.
It uses various public sources such as search engines (Google, Bing), PGP key servers, and SHODAN database to extract valuable reconnaissance information.
The tool's functionality aids cybersecurity professionals and ethical hackers in conducting passive information gathering to assess potential attack vectors and strengthen organizational security measures.

### Dorking
* Google Dorking, for more comprehensive searches, users can consult resources like the "Google Dorking Cheatsheet". When looking for subdomains, adding a wildcard before the site name can broaden the scope of results,
for example, vulnerability site:*Seagate.com. Additionally, users can utilize the "Google Hacking Database" available on the Exploit Database website for further exploration and reconnaissance.
* Github Dorking, the same as google dorking, only in Github, it can be accessed in “Github Dork Cheatsheet”

### Collecting Breached Credentials
* Intelx -> users can search for leaked email in databreach.

## Scanning and Enumeration
### Host Discovery
1. The ```-sn``` option in nmap is used to ping all IP addresses in the specified IP range. For example, the command nmap -sn 192.168.68.0/24 will
send ICMP echo requests to each IP address within the range to determine which hosts are alive.
2. ```sudo arp-scan -l``` scans all hosts on the local network and identifies the manufacturer based on the MAC addresses used.
3. ```sudo netdiscover -r``` provides similar results to ```arp-scan```,
displaying discovered hosts and their MAC addresses. For instance, ```sudo netdiscover -r 192.168.68.0/24``` scans
the specified IP range and lists active hosts along with their MAC addresses.

### NMap Basic
* Basic Command
1. By default, ```nmap 10.0.2.4```, only TCP ports are scanned, and only the first 1000 ports are checked.
2. To scan all ports, use ```nmap -p- 10.0.2.4```.
3. For specific ports, use ```nmap -p 80,443 10.0.2.4```.
4. To determine the version of services running on ports, use ```nmap -p 80,443 -sV 10.0.2.4```.
5. To increase scanning speed, use ```nmap 10.0.2.4 -T4```. Speed options range from 1 to 5, with higher values increasing the number of packets sent and potentially increasing the chance of missed results.

* Default Script Enumeration
1. To perform direct enumeration, use ```nmap -p 21,22,80,8180 -sV -sC 10.0.2.4```.
2. To conduct a comprehensive scan, use ```nmap -p 21,22,80,8180 -A 10.0.2.4``` to scan all ports and enable OS detection, version detection, script scanning, and traceroute.

### FTP Enumeration

If anonymous login is allowed on FTP discovered during an Nmap scan, you can directly access it by typing ftp 10.0.2.4 and logging in with the username anonymous. For the password, you can enter anything or simply press Enter.
1. Once logged in, change directory to /etc using ```cd /etc```.
2. Then, use ```more passwd``` to read the contents of the passwd file, similar to the ```cat``` command.
3. After that, use ```get passwd``` to download the passwd file.
* To upload a file
1. Use ```put``` to find a file in the working directory.
2. Change directory to /tmp using ```cd /tmp```.
3. Finally, upload a file to /tmp using ```put (file_name)```.
* For exploiting enumeration
1. After determining the FTP version, search for relevant exploits on Google.
2. Exploit-DB is often a reliable resource for finding suitable exploits.

### HTTP Enumeration

Start enumeration on insecure HTTP ports (other than 80, 8080, 443 for HTTPS). For example, if HTTP is running on port 8180:
1. Enter the IP address and port into the browser: 10.0.2.4:8180/
2. Content Discovery (Directory Bruteforcing):
* If using Kali Linux, users can use ```dirb```.
* Alternatively, users can download and use ```dirsearch```. This tool can also discover subdomains from a URL.
  * Usage example: ```python dirsearch.py -u http://10.0.2.4:8180```
  * You can specify additional file extensions with -e .bak,.backup,.txt -f.
  * Look for responses with status code 200, indicating the URL is accessible and can be further investigated or used.

### Scanning With Nessus
This tool is incredibly powerful for pinpointing vulnerabilities and their specifics. The only downside is that it's paid, but you can create  new accounts every week to bypass this. The activation is straightforward:
1. Type /bin/systemctl start nessusd.service.
2. Then, from a Linux browser, navigate to https://kali:8834/.


## Exploitation
### Reverse and Bind Shell
Shell is the access to a system, one of its example is Command Prompt. There are two kinds of shells:
1. Reverse Shell, The attacker is on "listening". The attacker opens a port, and the victim initiates the connection.

![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/b2acf1d5-3dc4-4678-a131-075ff027e060)

2. Bind Shell, The victim is on "listening". The victim opens a port, and the attacker initiates the connection.

![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/35358416-7624-4705-af77-e1486c6d93e4)

Reverse shell is more commonly used because bind shell connections are often blocked by firewalls (which typically monitor and restrict incoming connections, not outgoing ones).

![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/45769b27-609e-43bd-8c02-f5e460fc3ae8)

### Manual Exploitation FTP
1. Once you have determined the FTP version using Nmap (ensure version detection is included during the scan), search the internet for exploits. For example you found an exploit file, such as a backdoor named "49757.py"
2. Run the exploit using ```python 49757.py <target_host>```. Note that the execution method may vary for different exploits, but generally, you need to specify the language, e.g., ```python 49757.py <target_host>```.
3. If access is gained, immediately check your privileges with ```whoami```. If you have root access, proceed with the desired actions.

### Manual Exploitation Apache Tomcat
1. Log in to the website using the admin role credentials obtained through FTP enumeration.
2. Exploit a WAR file; search for the method online.
   
   a. Once found, create a malicious WAR file using msfvenom.
   
   b. The reverse shell will be used. After downloading the malicious WAR file (shell), start listening on port 4444 with nc -nlvp 4444.
   
   c. After setting up listening, upload the shell.
   
   d. Execute the uploaded shell to establish a connection back to Kali.

### Exploit Using Metasploit
Start with ```mfsconsole```
* FTP
1. To find an exploit, use ```search <version>```.
2. Once you find it, use ```use <exploit_number>```.
3. To understand how to use the exploit, type ```options```.
4. For vsftpd, use the command ```set <COMMAND> <required>``` before using the provided Metasploit commands. For example, ```set RHOSTS 10.0.2.4```.
5. After configuring the settings, execute the exploit with ```exploit``` or ```run```.
* Apache
1. It's similar, but this time search for ```apache tomcat manager```.

### Exploiting UNREALIRCD Using Metasploit
1. Start with Nmap.
2. For ports 6667 and 6697, where IRC is detected, run Nmap on these ports with the ```-A``` option to get detailed information, especially the version.
3. To find the exploit, use ```searchsploit unrealircd``` and locate the appropriate exploit.
4. Download the exploit with ```searchsploit -m <exploit_number>``` (Note: use the number after the last / in the path).
5. Launch Metasploit with ```msfconsole```.
6. Search for the exploit using ```search unrealircd```.
7. Use the identified exploit.
   a. If it cannot be executed due to missing payloads, list the available payloads with ```show payloads``` and set the payload with ```set payload <payload_number>```.

### Exploiting UNREALIRCD Manually
1. Search on Google for the appropriate exploit.
2. If you find it on GitHub, locate the code, open it in raw view, and copy the link.
3. Download it in Kali using ```wget <link_exploit>```.
4. Understand how it works. For example, if it's a Python exploit, run it with ```python <exploit_file_name>```.
5. Proceed to exploit.

   a. If it doesn't work, open the exploit file with nano <exploit_file_name> and check if there are any parameters that need to be changed.

## Basic Privilege Escalation
### Linux Permissions
1. Regarding users, there are two important files:
   
a. /etc/passwd: This file contains user names, user IDs, home directories, and other details.

b. /etc/shadow: This file contains hashed passwords for each user.

2. Groups refer to collections of users:
   
a. /etc/group: This file contains information about user groups.

To view details of folders or files, you can use the command ls -la.

![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/8ea15f02-68b5-4320-9c01-154273d853e8)

### Kernel Exploit
The kernel is the core component of an operating system. Exploiting it can lead to obtaining a root shell, which involves four steps:

1. Identify the kernel version using ```uname -a```.
2. Search for exploits using tools like searchsploit or exploitsuggester2.
   
   a. To use exploitsuggester2, execute ```perl linux-exploit-suggester-2.pl -k <kernel_version>```.

4. Transfer the exploit to the target system.
5. Compile and execute the exploit.

### Exploiting SUID
Set User Id (SUID) is a feature in Linux that allows files to be executed with the privileges of the file owner. For example, if a file has its SUID bit set to root, anyone executing that file will run it with root privileges. The process involves:

1. Check for files with SUID set using ```find / -type f -perm -u=s 2> /dev/null```.
2. Use a helpful tool like ```lse.sh``` to specifically identify uncommon SUID settings:
   
   a. Make the script executable with ```chmod +x lse.sh```.
   
   b. Execute it with ./lse.sh | more.
   
3. Look for misconfigurations or vulnerabilities in the identified SUID binaries for potential privilege escalation using resources like GTFOBins. For example, explore potential vulnerabilities in utilities such as Nmap or xargs.

### Exploiting SUDO
Super User Do (Sudo) is a command that allows executing tasks with root privileges. Exploiting it is similar to SUID in nature but involves searching for executable files configured in the sudoers file. Here's how to proceed:

1. Check which commands can be run with sudo privileges using ```sudo -l```. Look for entries marked with NOPASSWD.
2. Once identified, search for potential exploits on GTFOBins that leverage these privileged commands.

### Weak File Permissions
* Examples of easily exploited file permissions:
1. Readable /etc/shadow
2. Writable /etc/shadow
3. Writable /etc/passwd
* Exploit Steps: Readable shadow
1. Check the permissions of shadow and passwd files using ```ls -la /etc/shadow``` and similar commands.
2. If shadow is readable, copy the root password hash and save it locally.
3. Once saved, use the 'john the ripper' tool to crack the password hash. Use the command ```john --format=sha512crypt --wordlist=/usr/share/wordlists/rockyou.txt <file_name>``` to retrieve the password.
* Exploit Steps: Writable shadow
1. Make sure to back up first, for example, using ```cp /etc/shadow /tmp/shadow.bak``` to create a backup in tmp.
2. Generate a new hash/password to replace the default hash, using ```mkpasswd -m sha-512 <new_password>```.
3. Edit the default file using ```vim /etc/shadow```.
4. Replace the default hash with the new hash.
5. Simply use sudo with the new password.
6. Don't forget to restore the backup to avoid detection, using ```cp /tmp/shadow.bak /etc/shadow```.
* Exploit Steps: Writable passwd
  
![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/308cc0d6-5c22-48d4-a830-7e549548057f)


Format: ```[username] : "x" = password stored in shadow : uid : guid.```

There are two exploits: you can replace "x" with a newly created hash for a new password, or simply delete "x" to gain root access without needing a password.

Steps to replace "x":

1. Don't forget to back up to avoid being caught stealing, use ```cp /etc/passwd /tmp/passwd.bak```.
2. Generate a new password hash using another method, such as openssl, like this: ```openssl passwd "<new_password>" ```.
3. Replace "x" with the new hash.
4. Use sudo with the new password.
5. Ensure to restore all files to their original state to avoid detection

### Upgrade Interactive Shells for Easier Operations
1. Check if Python is available using "which python". Proceed if Python is found, otherwise accept it.
2. Continue with "python -c 'import pty;pty.spawn("/bin/bash")'".
3. Press Ctrl + Z.
4. Proceed with "stty raw -echo; fg".
5. Press Enter twice.
