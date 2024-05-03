## DMaaP
DMaaP is a premier platform for high performing and cost effective data movement services that transports and processes data from any source to any target with the format, quality, security, and concurrency required to serve the business and customer needs.

### DMaaP Functional Areas
1. Data Filtering, the data preprocessing at the edge via data analytics and compression to reduce the data size needed to be processed.
2. Data Transport, the transport of data intra & inter data centers. The transport will support both file based and message based data movement. The Data Transport process needs to provide the ability to move data from any system to any system with minimal latency, guaranteed delivery and highly available solution that supports a self-subscription model that lowers initial cost and improves time to market.
3. Data Processing, the low latency and high throughput data transformation, aggregation, and analysis. The processing will be elastically scalable and fault-tolerant across data centers. The Data processing needs to provide the ability to process both batch and near real-time data.  

### DMaaP Components
1. Message Router (MR), message Router is a reliable, high-volume pub/sub messaging service with a RESTful HTTP API. It is intended to be deployed by Platform Service providers so that it is available to Platform clients as a web service. The service is initially built over Apache Kafka.
2. Data Router (DR), the Data Routing System project is intended to provide a common framework by which data producers can make data available to data consumers and a way for potential consumers to find feeds with the data they require. The interface to DR is exposed as a RESTful web service known as the DR Publishing and Delivery API
3. Data Movement Director (DMD), a client to DMaaP platform to publish & subscribe data.
4. Data Bus Controller, provisioning API of the Data Movement Platform.

* Message Router
In DMaaP Message Router, Restful web service is exposed to client to perform any needed action with Kafka. After getting the request it calls the Message router service layer which is created using AJSC ( AT&T Java Service Container).
AJSC finally calls Kafka services and response is sent back.

  ![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/ca3394a9-07f6-4c64-91db-dab2574166d2)

    The Message Router includes pub/sub messaging, horizontal scalability, durability, high throughput, easy integration via RESTful HTTP APIs,
    and various authentication and authorization models, while optionally supporting network location services, message replication, different message bus technologies, standardized topic names,
    and recovery of partially delivered messages.

* Data Router
  
  ![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/95a21728-76fb-47da-8616-a644dffefc0b)

    The Data Router uses a pub/sub architecture that facilitates adding new subscribers without impacting publishers, remains agnostic to data sources and sinks such as RDBMS, NoSQL, other DBMS, and flat files, allows tracking completed file transmissions, uses HTTP for file transfer, automatically retries failed deliveries,
    requires user authentication and endpoint authorization, supports low-latency large file transmission, and offers a guaranteed delivery option even when subscribers are down for an extended period.

### Architecture Alignment
  DMaaP is indentified as a common service in ONAP Architecture which can be seen below:
  
   ![image](https://github.com/bmw-ece-ntust/internship/assets/145204053/53ff12c3-86e2-4d69-85fd-7f5dcaf7eae5)
