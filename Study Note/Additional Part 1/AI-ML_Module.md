# Part 4: AI/ML Module
- Goal : 
    - [x] Learning Isoforest & Random Forest
    - [x] Learning VAR Module
    - [x] Learning LSTM
    - [x] Learning RNN
- Useful Links:
    - [AI/ML in Near-RT RIC](https://www.analysysmason.com/contentassets/62ee68d6f8fd4c91b7318e97036382c9/analysys-mason_near_rt_ric_jun2021_rma07.pdf)
    - [Isolation Forest Algorithm](https://towardsdatascience.com/how-to-perform-anomaly-detection-with-the-isolation-forest-algorithm-e8c8372520bc)
    - [Hands On Tutorial on VAR Module](https://analyticsindiamag.com/hands-on-tutorial-on-vector-autoregressionvar-for-time-series-modeling/)
    - [Introduction to LSTM](https://machinelearningmastery.com/gentle-introduction-long-short-term-memory-networks-experts/)
    - [Introduction to RNN](https://www.datacamp.com/tutorial/tutorial-for-recurrent-neural-network)

- Outcome (Study Note) : 
    - Learn about Isoforest & Random Forest
    - Learn about VAR Module
    - Learn about LSTM
    - Learn about RNN

***

## I. Isoforest & Random Forest
The Isolation Forest (iForest) and Random Forest are both machine learning algorithms with distinct applications and characteristics.

The **Isolation Forest** algorithm is primarily **used for anomaly detection**. It is an unsupervised learning method that excels at isolating anomalies (or outliers) in a dataset. The algorithm leverages the fact that anomalies are typically few in number and have attribute values that differ significantly from normal instances. By constructing isolation trees and **measuring the number of splits required to isolate an instance**, the algorithm can effectively identify anomalies. It is a fast algorithm and is available as a module in Scikit-learn, making it accessible for practical use in anomaly detection applications.
![image](https://hackmd.io/_uploads/SJs-L2Pt6.png)

On the other hand, the **Random Forest** algorithm is a versatile ensemble learning method that can be used for both **classification** and **regression** tasks. It operates by constructing a multitude of decision trees during training and **outputting the mode of the classes** (in the case of classification) or **the average prediction** (in the case of regression) of the individual trees. Random Forest is known for its robustness and ability to handle large amounts of data with high dimensionality. It is commonly used in various domains, including finance, healthcare, and ecology, for tasks such as fraud detection, disease prediction, and species classification.
![image](https://hackmd.io/_uploads/BkVaB3Dt6.png)


In **Near-RT RIC**, AI/ML technologies, including algorithms like Isolation Forest and Random Forest, are being integrated **to automate and optimize RAN operations**. The Near-RT RIC incorporates AI/ML into its decision-making functionalities, enabling real-time control and network optimization actions. AI/ML is recognized as a critical enabler to automate near-RT use cases, with applications in QoS-based radio optimization, real-time video optimization, and massive MIMO optimization. The integration of AI/ML technologies is expected to significantly enhance the efficacy of RAN use cases by exploiting the massive amount of data generated in the RAN.

## II. VAR Module
One of the AI/ML modules used in the Near-RT RIC is the **VAR (Vector Autoregression) module**. The VAR module is a statistical model that can be used to **analyze the relationship between multiple time series variables**. It is commonly used in finance, economics, and other fields to forecast future values of a variable based on its past values and the past values of other related variables. In the **Near-RT RIC**, the VAR module can be used to **predict network traffic patterns** and **optimize network resource allocation**. By analyzing historical data on network traffic and resource usage, the VAR module can identify patterns and trends that can be used to predict future traffic and resource needs. This information can then be used to optimize network resource allocation, ensuring that resources are allocated where they are needed most. The VAR module is just one example of the many AI/ML modules that can be used in the Near-RT RIC to automate and optimize RAN operations. 

## III. LSTM
**Long Short-Term Memory** (LSTM) is a type of recurrent neural network (RNN) designed to handle the vanishing gradient problem present in traditional RNNs. LSTMs are particularly useful for learning **long-term dependencies in sequence prediction tasks**, such as time series prediction, speech recognition, and music composition. Key characteristics of LSTM networks include:
1. **Chain-like structure**: LSTMs have a chain-like structure, with repeating modules consisting of four interacting layers.
2. **Gating mechanisms**: LSTMs introduce three gating mechanisms (input gate, forget gate, and output gate) that control the flow of information through the network, allowing it to selectively remember or forget information from the input.
3. **Memory blocks**: LSTM networks have memory blocks connected through layers, with each block containing components that make it smarter than a classical neuron and a memory for recent inputs.
4. **Stacking**: LSTM networks can be stacked into deep network architectures, allowing them to address complex sequence problems in machine learning.


In the Near-RT RIC, LSTM networks can be used for various AI/ML applications, such as:
- **Time series prediction**: LSTMs can be used to predict network traffic patterns and optimize network resource allocation based on historical data.
- **Speech recognition**: LSTMs can be employed in speech recognition applications to improve the accuracy of speech-to-text conversion.
- **Music composition**: LSTMs can be used to generate music compositions based on input patterns and historical data.
- **Grammar learning**: LSTMs can be applied to grammar learning tasks, such as identifying and correcting grammatical errors in text.

By integrating LSTM networks into the Near-RT RIC, AI/ML-driven optimization can be further enhanced, leading to more efficient and effective RAN operations.
![image](https://hackmd.io/_uploads/B1IPAnDFp.png)

## IV. RNN
**Recurrent Neural Networks** (RNNs) are a type of artificial neural network that uses **sequential data** or **time series data**. They are commonly used for ordinal or temporal problems, such as language translation, natural language processing (NLP), speech recognition, and image captioning. RNNs are particularly useful for tasks that require the processing of sequential data, as they can capture the context and dependencies between input elements. Key characteristics of RNNs include:
1. **Sequential processing**: RNNs process input sequences sequentially, making them computationally efficient and easy to parallelize.
2. **Memory of past inputs**: RNNs have a memory of past inputs, allowing them to capture information about the context of the input sequence.
3. **Parameter sharing**: RNNs share the same set of parameters across all time steps, reducing the number of parameters and making the model more efficient.
4. **Advanced architectures**: RNNs can be enhanced with advanced architectures like Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) to address the vanishing gradient problem and improve memory capacity.


In the context of Near-RT RIC, RNNs can be used for various AI/ML applications, such as:
- **Time series prediction**: RNNs can be used to predict network traffic patterns and optimize network resource allocation based on historical data.
- **Language translation**: RNNs can be employed in language translation applications to improve the accuracy of translation.
- **Speech recognition**: RNNs can be used to improve the accuracy of speech-to-text conversion.
- **Image captioning**: RNNs can be applied to generate captions for images based on input patterns and historical data.
![image](https://hackmd.io/_uploads/Hy1mkaPtp.png)
