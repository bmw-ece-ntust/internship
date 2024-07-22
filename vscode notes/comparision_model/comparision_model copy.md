

|                     | LSTM one-shot        | CNN 1D one-shot | N-Beats            | Xboost   | Auto ARIMA           | VAR             | Transfer learning LSTM  ?          |
|---------------------|----------------------|---------------------|--------------------|--------------------|-----------------|-----------------|-----------------|
| Library             | Tensorflow           | Tensorflow          | Darts & torch      | Darts & torch     | StatsModel      | statsmodels     | sfdasdfa       |
| Epochs              | 100                  | 30                  | 20                 | 10 estimators     | Data 12         | Data  | sdsafsdf               |
| Training Time per epoch  |6 sec and 38 ms  | 3 sec and 23 ms      | 51 sec             | Unknown                 | Data 10         | Data 11         | s               |
| Total Training Time | 10 min and 4 sec     | 91 seconds          | 17 min and 1 sec    | 137 sec            | Data 10         | Data 11         | s               |
| Testing Time for 60 data points| 24 ms     | 44 ms              | 592 ms             | 0.75 sec           | Data 10         | Data 11         | s               |
| Total Parameter     | 424440               | 2.7 Million            | 56.8 Million       | Unknown           | Data 14         | Data 15         | s               |
| Resource Usage      | GPU 4.8 GB VRAM      | GPU 5.3 GB VRAM           | GPU 3.3 GB VRAM  |  GPU 1.8 GB VRAM    | Data 14         | Data 15         | s               |
| RMSE                | 3.511 (train) <br> 3.355 (test) |  4.065 (train) <br> 2.961 (test) | 0.737 (train) <br> 2.694 (test) | Data 11            | Data 12         | Data 13         | s               |
| MSE                 | 12.325 (train) <br> 11.258 (test) | 16.525 (train) <br>  8.767 (test)   | 0.0691 (train) <br> 0.915 (test)| Data 11            | Data 12         | Data 13         | s               |
| MAE                 | 2.793 (train) <br> 2.6438 (test) | 3.201 (train) <br> 2.372 (test)      | 0.583 (train) <br> 2.147 (test) | Data 11            | Data 12         | Data 13         | s               |
| MAPE   (%)             | 6.6% (train) <br> 6.23% (test)   | 7.57% (train)<br> 5.6% (test)    | 1.37% (train) <br> 5.03% (test)  | tcn                | Data 12         | Data 13         | s               |
| Advantage           | Baris 2       | Data 3              | Data 4  | Data 5      | Data 6 | Data 7 | s|
| Disadvantage        | Baris 3       | Data 5              | Data 6  | Data 7      | Data 8 | Data 9 | s|
| additional info    | Baris 3       | Data 5              | Data 6  | Data 7      | Data 8 | Data 9 | s|