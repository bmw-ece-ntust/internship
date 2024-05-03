## UERANSIM
> Make sure you have enough space in your VM by making a bigger storage. In this example I am using 8GB (~~I tried 4GB~~ --> it did not work)
## A bit about 5G, OAI, and USRP
![image](https://github.com/bmw-ece-ntust/internship/assets/123353805/6f3d3d54-e43e-46ff-a9d0-33ad421d6626)

## Installing UERANSIM

1. Update and Upgrade UERANSIM VM
```
sudo apt update
sudo apt upgrade
```
<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/65e360b3-15dd-45e8-b6b3-01f9386d38d5">
<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/afa2ea07-2f63-4dc4-9171-12644edf2ae4">
```
P.S. YEP! it might take a while just be patient :>
```
<img width="715" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/4ae9c0a8-838c-45eb-b901-45a2e4338aa2">

2. Installing Tools
```
sudo apt install make
sudo apt install g++
sudo apt install libsctp-dev lksctp-tools
sudo apt install iproute2
sudo snap install cmake --classic
```
<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/ac4043f5-c47b-4681-aa78-e2747079083f">

<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/93b0ed6e-f8cd-4c6e-98ce-fdcb3f0ac5f4">

<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/e5db0f23-87d3-404f-9eb0-0bcff71193b4">
<img width="496" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/f33b621d-dc2f-4961-bbf1-2d7364b1215f">

3. Downloading UERANSIM
```
sudo apt install git
git clone https://github.com/aligungr/UERANSIM
cd UERANSIM
git checkout v3.1.0
```
<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/691c8da5-9b4b-44aa-bfd5-46d099fef170">

<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/b9dda15b-77d9-4b9e-b85a-800e53f51f77">
<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/55b4dc1f-8a0e-4bbf-a2c2-5cb18f09c5d5">

4. Building UERANSIM
```
make
```
<img width="912" alt="image" src="https://github.com/bmw-ece-ntust/internship/assets/123353805/f73a7d19-ec3c-4f0a-9415-48b03210f1aa">

6. 
7. D
