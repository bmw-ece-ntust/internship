|                               | one-shot LSTM        | one-shot CNN 1D      | N-Beats              | Xboost                |
|-------------------------------|----------------------|----------------------|----------------------|-----------------------|
| Library                       | Tensorflow           | Tensorflow           | Darts                | Darts                 |
| Epochs                        | 100                  | 30                   | 20                   | 10 estimators         |
| Training Time per epoch       | 6 sec and 38 ms      | 3 sec and 23 ms      | 51 sec               | Unknown               |
| Total Training Time           | 10 min and 4 sec     | 91 seconds           | 17 min and 1 sec     | 137 sec               |
|Testing Time for 60 data points| 24 ms                | 44 ms                | 592 ms               | 0.75 sec              |
| Total Parameter               | 424440               | 2.7 Million          | 56.8 Million         | Unknown               |
| Resource Usage                | GPU 4.8 GB VRAM      | GPU 5.3 GB VRAM      | GPU 3.3 GB VRAM      | GPU 1.8 GB VRAM       |
| RMSE                          | 3.511 (train) <br> 3.355 (test) | 4.065 (train) <br> 2.961 (test) | 0.737 (train) <br> 2.694 (test) | 2.15 (train) <br>  2.7 (test)     |
| MSE                           | 12.325 (train) <br> 11.258 (test) | 16.525 (train) <br> 8.767 (test) | 0.0691 (train) <br> 0.915 (test) | 4.62 (train) <br> 7.29 (test)          |
| MAE                           | 2.793 (train) <br> 2.6438 (test) | 3.20 (train) <br> 2.372 (test)  | 0.583 (train) <br> 2.147 (test) | 1.709 (train) <br>    2.164  (test)         |
| MAPE (%)                      | 6.6% (train) <br> 6.23% (test)   | 7.57% (train)<br> 5.6% (test)   | 1.37% (train) <br> 5.03% (test) | 4.03% (train) <br> 5.09% (test)                  |
| Advantage                     | xxxxxxx              | xxxxxx            | xxxxxx              | xxxxxx               |
| Disadvantage                  | xxxxxx              | xxxxx               | xxxxx               | xxxxx                |
| additional info               | xxxxx             | xxxx               | xxxxx               | xxxxx                |
