## OSC O-DU I VERSION


# Downloading Ubuntu on Mac
1. To Install OSC o-du-l2 we can use either ubuntu or centOS. In this document we are gonna focus on installing using *ubuntu on mac*. First and foremost download files bye clicking this two link below.
```
hhttps://cdimage.ubuntu.com/jammy/daily-live/current/
UTM - https://mac.getutm.app/
```
2. Open the UTM file put in the application on mac. Then proceed to install. Put in the file ubuntu when the page is like the picture below 
<img width="541" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/c0913164-7e13-42eb-8d28-a2b4345d4fe1">
3. Continue to download the UTM. Then, open the file and install ubuntu application on the right side of the screen
![image](https://github.com/bmw-ece-ntust/internship/assets/123353805/514a17f2-67e8-43f0-a255-ae8ad86578f8)
4. After that log out -> restart -> log in again. Open your terminal in ubuntu and your screen should look like this
<img width="752" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/1f2c01f6-8b88-421c-818f-e097f6bd8d4a">
  
# Downloading the OSC 
1. GCC, LKSCTP, PCAP, nad libxml2 libraries are required to compile and execute O-DU High
> GCC
```
sudo apt-get install -y build-essential
```
> LKSCTP
```
sudo apt-get install -y libsctp-dev
```
> PCAP
```
sudo apt-get install -y libpcap-dev
```
> nad libxml2
```
sudo apt-get install -y libxml2-dev
```
The after process should look like this
<img width="868" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/2fcae383-35e8-4210-990a-e044afedb4d6">

3. Git Cloning
If your ubuntu cannot found 'git' command, install git first then use the code below to clone git (instruction from O-RAN SC DOCS is mistaken)
```
sudo apt install git
```
```
mkdir ~/O-DU_High_Directory\
```
```
git clone https://github.com/o-ran-sc/o-du-l2.git
```
<img width="868" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/945b3db7-5059-4024-9930-1d709c6dac6c">

4. Add netconf user
Note : use o-du-l2 instead of l2 from the reference, because it will result an error
```
gisela@giselaaurora:~$ pwd
/home/gisela
gisela@giselaaurora:~$ mv o-du-l2 O-DU_High_Directory
gisela@giselaaurora:~$ cd O-DU_High_Directory/l2/build/scripts
bash: cd: O-DU_High_Directory/l2/build/scripts: No such file or directory
gisela@giselaaurora:~$ pwd
/home/gisela
gisela@giselaaurora:~$ cd O-DU_High_Directory/o-du-l2/build/scripts
gisela@giselaaurora:~/O-DU_High_Directory/o-du-l2/build/scripts$ sudo ./add_netconf_user.sh
Adding system user `netconf' (UID 129) ...
Adding new user `netconf' (UID 129) with group `nogroup' ...
Creating home directory `/home/netconf' ...
BAD PASSWORD: The password contains the user name in some form
ssh-keygen: generating new host keys: RSA DSA ECDSA ED25519 
Generating public/private dsa key pair.
Your identification has been saved in /home/netconf/.ssh/id_dsa
Your public key has been saved in /home/netconf/.ssh/id_dsa.pub
The key fingerprint is:
SHA256:H0fYmBxSKmgxqO1j5x6t+QtptNAm398TKg0jYICnpTo root@giselaaurora
The key's randomart image is:
+---[DSA 1024]----+
|.  .o   ..o      |
|o +  +   + *     |
| O  o . . = o    |
|+ +o   .   .     |
|.oo.+   S . .    |
|E +*o=o  ..o     |
| o +B.o+ ...     |
|   ..=..o..      |
|   .+.oo. ..     |
+----[SHA256]-----+
```
5. Install package
>sudo apt-get install -y libssh
>sudo apt-get install -y libyang
>sudo apt-get install -y libnetconf2
>sudo apt-get install -y sysrepo
>sudo apt-get install -y netopeer2
>sudo apt install python2-dev python2 python-dev-is-python3

sudo ./install_lib_O1.sh -c

#Finish Install
