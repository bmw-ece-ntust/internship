|                               | Multi Scale CNN 1D based on Journal | My CNN 1D                      |
|-------------------------------|-------------------------------------|--------------------------------|
| **Time step (length) Input**   | 240 samples                         | 240 samples                    |
| **Input Features**             | PRB downlink, sine periodic, cosine periodic | PRB downlink, number of UEs in RRC, downlink throughput |
| **Total Convolution layer**    | 34                                  | 3                              |
| **Kernel size**                | 8                                   | first: (length input/8), second: (length input/4), third: (length input) |
| **Number of filters**          | 64                                  | 120                            |
| **Dilation rate**              | 1, 2, and 4                         | 1                              |
|**Dropout rate**                | 0.05 (5%)                           | 0.2 (20%)                      |
| **Batch Size**                 | 128                                 | length input/2                 |
| **Loss Function**              | Pinball Loss                        | MSE loss                       |
| **Optimizer**                  | AMSGrad                             | Adam                           |
| **Start Learning rate**        | 0.01                                | 0.001                          |
| **Learning Rate decay**        | 0.3                                 | 0.1                            |
| **Total epochs**               | 62 epochs                           | 40 epochs                      |
| **MAE**                        | 13.81                               | 1.21                           |
| **RMSE**                       | 17.52                               | 2.34                           |
