// Progess of installing OSC

# 1.Install Linux on device - success
# 2.Install OSC package part 1 (until github clone) - success
```
gcc --version
sudo apt-get install -y build-essential
sudo apt-get install -y libsctp-dev
sudo apt-get install -y libpcap-dev
pwd
mkdir ~/O-DU_High_Directory\
git clone https://github.com/o-ran-sc/o-du-l2.git
```
<img width="869" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/19341fda-e199-4874-a3ae-51238dbd2358">

# 3.Install OSC Package part 2 (until netopeer) - !problem!
```
pwd
mv o-du-l2 O-DU_High_Directory
cd O-DU_High_Directory/l2/build/scripts
pwd
cd O-DU_High_Directory/o-du-l2/build/scripts
sudo ./add_netconf_user.sh
sudo apt-get install -y libssh
sudo apt-get install -y libyang
sudo apt-get install -y libnetconf2
sudo apt-get install -y sysrepo
sudo apt-get install -y netopeer2
```
```
sudo ./install_lib_O1.sh -c
```
# 4.Install OSC Package part 3 (compilation) - !problem!
```
sudo ./netopeer-server.sh start
cd
cd O-DU_High_Directory/o-du-l2/build/scripts
make clean_odu MACHINE=BIT64 MODE=FDD
make odu MACHINE=BIT64/MODE=FDD
```
<img width="872" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/df3a9216-c630-4796-82b2-cc00e9720d33">
Still solving problem at the "make clean_odu" and "make odu"












