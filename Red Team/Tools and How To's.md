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


