# Guide of AI/ML Management Dashboard - Satwika Bintang
## 1. Follow the Guide of AIMLFW
### Open Browser
```
http://localhost:32005/
```
## 2.Create training Function

![alt text](image-1.png)
### Click **Create Training Function**
![alt text](image-2.png)
## 3. Create New ipynb file
### copy the untitled.ipynb code to new ipynb file
![alt text](image-3.png)
### 4 Copy "In[7]" code and modify "pipeline_name" and "request.post_URI" to the "qoetest" before you running.
## 5. checklist zip file and download 
![alt text](image-4.png)
## 6.Go to localhost:32005 and fill the "Create training Job"
![alt text](image-5.png)

### if training function doesn't show up,  Go to http://192.168.8.44:32359/#/pipelines 
## 7. Check "Training Job Status"
![alt text](image.png)
### Data extraction  is still failed because the data is still empty. [Solution](https://hackmd.io/ai9WR29zTl2Rmle8K4-Yog#7-2-Rroblem-2%EF%BC%9AInfluxDB-datalake-cant-able-to-training-)

## 8. Create Feature Group
### Feature Group  Name: Hellopanda
![alt text](image-7.png)
## 9. Create Training Job
![alt text](image-8.png)
## 10. Training Job Status succeeded
### Trajining Job Name: Hellopanda22
![alt text](image-9.png)


### check debugging http://192.168.8.44/#/runs/details/42b37a30-cc00-4963-935c-1cf2a251396e 