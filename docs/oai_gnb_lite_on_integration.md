# OAI gNB + LiteON RU Integration Note


> **References:**
> - [OAI gNB(BBU version/branch: develop/commit 168b172f9) + LiteOn RU integration](https://hackmd.io/@Summer063/H1l9KtAcp)

## 1. LiteON RU
#### 1.1 Connect to the RU :
SSH to the RU
```bash
ssh user@192.168.*.**
```
Password
```bash
******
```
Enable password
```bash
*******
```
#### 1.2 Set the eAxC ID in RU (Need to do this after every reboot) :
Set this settings in configuration mode (enable)
```bash
enable
set_devmem 0x80001014 32 0x00050004
set_devmem 0x80001018 32 0x00070006
set_devmem 0x8000201C 32 0x00000001
```
#### 1.3 Check RU Status :
To check the RU status you need to be in configuration mode
```bash
enable
show oru-status
```
![status_not_ready](/assets/oai_gnb_lite_on/status_not_ready.png)

## 2. OAI gNB Server (192.168.8.29)
#### 2.1 Connect to the server :
SSH to the server
```bash
ssh oai72@192.168.*.**
```
Password
```bash
******
```
#### 2.2 After every server reboot you need to do this step :
To setup maximum performance, vf, and environment
```bash
source /home/oai72/Script/oaiLOvf.sh
```
#### 2.3 Bring up the Core Network (open5gs) :
Go to home directory and start open5gs
```bash
sudo ./createtun.sh # not persistent after rebooting
./start_open5gs.sh
```
To check if everything is running fine, you can check the amf log by attaching it's screen session.
```bash
screen -r amf
```
#### 2.4 Run gNB :
Go to this directory and run the gNB (change the log filename for every restart)
```bash
cd /home/oai72/FH_7.2_dev/openairinterface5g/cmake_targets/ran_build/build
sudo ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.273prb.fhi72.4x4-liteon.conf --sa --reorder-thread-disable 1 --thread-pool 1,3,5,7,9,11,13,15 > /home/oai72/OAI_gNB_LOG/01_change_name.log 2>&1
```
#### 2.5 Check DU connection at RU side
To check the RU status you need to be in configuration mode
```bash
enable
show oru-status
```
![status_ready](/assets/oai_gnb_lite_on/status_ready.png)

## 3. UE Test
#### 3.1 Open nemo handy app
![nemo_handy_app](/assets/oai_gnb_lite_on/nemo_handy_app.png)
#### 3.2 Lock the band of SSB center frequency and SCS
![carrier_lock](/assets/oai_gnb_lite_on/carrier_lock.png)
#### 3.3 We use ARFCN 630048(3450.72 MHz) for OAI gNB
![arfcn](/assets/oai_gnb_lite_on/arfcn.png)
#### 3.4 Check the signaling log
![signalling](/assets/oai_gnb_lite_on/signalling.png)

## Result
![nemo result](/assets/oai_gnb_lite_on/nemo%20result.png)