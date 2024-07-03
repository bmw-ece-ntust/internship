# AIMLFW

## 1. Try to familiar with AIMLFW
### 1-1. Enter the InfluxDB to check data

```shell
1| kubectl exec -it my-release-influxdb-56c6fdcfcd-j52z5 -- bash

2| influx query  'from(bucket: "UEData") |> range(start: -1000d)' -o primary -t UcxRTvArR5mk_-J2k17SEf1uvD_-PT_gi1L-zkXdvW1KcyiyqREs7aD3kxkdtDngmhCW5qBKM69h0djn_CfEgw==
```
result:
![alt text](images/image.png)

### 1-2. Change the code and token in insert.py

```shell
1| git clone -b f-release https://gerrit.o-ran-sc.org/r/ric-app/qp
2| cd qp/qp
3| sudo nano insert.py
```

result:
![alt text](images/image-1.png)

### 1-3. Check your influx service name and port
```shell
1| kubectl get service -A
```
result:
![alt text](images/image-2.png)

Move to another terminal and execute this command
```shell
2| kubectl port-forward svc/my-release-influxdb 8086:8086 -n ricplt
```
Back to first terminal and execute this command to insert data
```shell
3| python3 insert.py
```
result:
![alt text](images/image-3.png)

