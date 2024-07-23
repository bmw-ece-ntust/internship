|                               | one-shot LSTM        | one-shot CNN 1D      | N-Beats              | Xboost                |
|-------------------------------|----------------------|----------------------|----------------------|-----------------------|
| Library                       | Tensorflow           | Tensorflow           | Darts                | Darts                 |
| Epochs                        | 100                  | 30                   | 20                   | 10 estimators         |
| Training Time per epoch       | 6 sec and 38 ms      | 3 sec and 23 ms      | 51 sec               | Unknown               |
| Total Training Time           | 10 min and 4 sec     | 91 seconds           | 17 min and 1 sec     | 137 sec               |
|Testing Time for 60 data points| 24 ms                | 44 ms                | 592 ms               | 0.75 sec              |
| Total Parameter               | 424440               | 2.7 Million          | 56.8 Million         | Unknown               |
| Resource Usage                | GPU 4.8 GB VRAM      | GPU 5.3 GB VRAM      | GPU 3.3 GB VRAM      | GPU 1.8 GB VRAM       |
| RMSE                          | 1.849 (train) <br>  3.26 (test) | 0.28 (train) <br> 2.6 (test) | 0.737 (train) <br> 2.694 (test) | 2.15 (train) <br>  2.7 (test)     |
| MSE                           |  3.42 (train) <br> 10.63(test) | 0.08 (train) <br> 6.74 (test) | 0.0691 (train) <br> 0.915 (test) | 4.62 (train) <br> 7.29 (test)          |
| MAE                           | 1.47 (train) <br> 2.61 (test) | 0.22 (train) <br> 2.07 (test)  | 0.583 (train) <br> 2.147 (test) | 1.709 (train) <br>    2.164  (test)         |
| MAPE (%)                      | 3.46% (train)<br> 6.16% (test)   | 0.52% (train)<br> 4.87% (test)   | 1.37% (train) <br> 5.03% (test) | 4.03% (train) <br> 5.09% (test)                  |
| Advantage                     | xxxxxxx              | xxxxxx            | xxxxxx              | xxxxxx               |
| Disadvantage                  | xxxxxx              | xxxxx               | xxxxx               | xxxxx                |
| additional info               | xxxxx             | xxxx               | xxxxx               | xxxxx                |
