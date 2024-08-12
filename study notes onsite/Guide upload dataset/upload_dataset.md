# Upload Data into InfluxDB
## 1. Check if your csv file avaliable or not. If not follow step 2.
```Javasrcipt
1. sudo -i
2. cd aimlfw-dep/demos/hrelease/scripts/
3. ls
```
![alt text](image.png)

## 2. Upload file into github/googledrive and access to public. Then, download using "wget"
```Javascript
wget https://raw.githubusercontent.com/bmw-ece-ntust/internship/2024-TEEP-17-Satwika/jupyternotebook/dataset/CellReports_resample.csv -O Cellreports_resample.csv
```
## 3.Check inside csv file
```
sudo nano Cellreports_resample.csv
```
![alt text](image-1.png)
### WARNING: if the csv have columns's name, the for loop in **step 4**  start from 1. If doesn't have, the for loop start from 0.
## 3. Go to Inside pushdata.py
### I.
```
sudo nano pushdata.py
```
### II.
```
change this parameter:
1. myorg
2. mybucket
3. mytoken
4. myurl
```
### III.
```
1. Adjust the range of the for loop to match the amount of samples data
2. Rename and adjust the fields for each column in the CSV
```
![alt text](image-2.png)

#### [link to get token  and org](https://github.com/bmw-ece-ntust/internship/blob/2024-TEEP-17-Satwika/vscode%20notes/notes%20AIMLF%20Server/Guide%20of%20AIMLFW%20Server.md#4-find-username-and-token)

### How to define bucket
Go to website: http://192.168.8.44:31843/
![alt text](image-3.png)

## 4. insertdata into influx db
```
pyhton3 pushdata.py
```
Go to website: http://192.168.8.44:31843/. The output if the data is successfully uploaded.
![alt text](image-4.png)

## 5. if InfluxDB datalake can't able to training
### I. Use this command to update "ip_address" and "datalake"
```
1. cd aimlfw-dep/
2. vim RECIPE_EXAMPLE/example_recipe_latest_stable.yaml
```
![alt text](image-6.png)

### II. Use this command to reinstall.
```
bin/uninstall.sh
bin/install.sh -f RECIPE_EXAMPLE/example_recipe_latest_stable.yaml
```
![alt text](image-5.png)