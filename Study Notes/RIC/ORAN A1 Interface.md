# O-RAN A1 Interface


## General Overview
A1 interface is the interface that connects the Non-RT RIC and Near-RT RIC.

<img src="https://imgur.com/mzrWI4X.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

The purpose of the A1 interface is to enable the Non-RT RIC function to provide policy-based guidance, support for AI/ML workflows, and enrichment information to the Near-RT RIC function so that the RAN can optimize e.g. RRM under certain conditions.

### Service Architecture
#### **A1 - P** (Policy Management Service)
The Non-RT RIC can define policies that are provided to the Near-RT RIC via the A1 Interface. The purpose of this policy is to improve the overall RAN performance. This policies contains policy objectives and policy resoruces applilcable to UEs and cells.

The Non-RT RIC can manage the policies based on feedback from the Near-RT RIC and network status provided by the O1. The Non-RT RIC can use the O1 observables to continuously evaluate the impact of the A1 policies towards fulfilment of the RAN intent and based on internal conditions it can decide to issue/update the goals expressed in the A1 policies.


#### **A1 - EI** (Enrichment Information Service)
In ORAN external systems can provide enrichment data to the SMO. SMO can collect information from O-RAN internal and O-RAN external information sources. The A1 interface is used for discovery, request, and delivery of A1 enrichment information The A1 interface is also used for the discovery of external enrichment information and the SMO / Non-RT RIC is responsible for the authentication of the source and the security of the direct connection.


#### **A1 - ML** (Model Management Service)
To support the ML model inference in the Near-RT RIC, the Non-RT RIC can provide enrichment information over the A1 interface. 

### A1 Principles
- Logical interface between Non-RT RIC in SMO and Near-RT RIC in RAN
- Enables multi vendor operations, indepenent from SMO, Non-RT RIC, and Near-RT RIC
- Way for enabling new services and data types without changing protocol stack or procedures
- Enables policy-based guideline for the RRM
- Way for Near-RT RIC to provide info regarding A1 Policies
- Required for policy enforcement services in Near RT RIC
- A1 Policy are created, modified, and deleted by Non-RT RIC
- A1 Policies are enforced until deleted
- EI Jobs are created, modified, and deleted by the Near-RT RIC, with enrichment information from the Non-RT RIC
  
### A1 Objectives
- Interconnection between Non-RT RIC in SMO and Near-RT RIC in RAN from different vendors
- Policy provisioning for UEs and cells
- Status feedback provosioning from Near-RT RIC towards Non-RT RIC to monitor the enforcement policies

### A1 Capabilites
- Transfer policy management Non-RT RIC to Near-RT RIC
- Policy status and feedback info Near-RT RIC --> Non-RT RIC
- Discovery and request of A1 EI from Near-RT RIC --> Non-RT RIC and delivery of it vice versa.


## Application Protocol
 <img src="https://imgur.com/pTZziEt.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

 ### Policy Management Service
The A1 application protocol for A1-P is based on signaling between the A1-P Consumer residing in the Non-RT RIC and the A1-P Producer residing in the Near-RT RIC. Both the A1-P Consumer and the A1-P Producer contain an HTTP Client and an HTTP Server.
 <img src="https://imgur.com/cjR8BIo.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

 - Policy is represented as PolicyObject in JSON format.
 - A Policy object contains a scope ID and >1 policy statement
 - A policy is identified by policyId, assigned by A1-P Consumer.
 - A1-P Prroducer cannot modify or delete a policy
 - PolicyObject does not contain any info regarding the internal Near-RT RIC function to evaluate it
 - A1-P Producer indicates which policy type creation is supported
 - The A1-P Consumer cannot create, modify, or delete policy types.

**Represenation objects**
| **Object**            | **Description**                                                                            |
|-----------------------|--------------------------------------------------------------------------------------------|
| **PolicyTypeObject**  | Contains the JSON schemas used to validate a PolicyObject and a PolicyStatusObject.         |
| **PolicyObject**      | JSON representation of an A1 policy.                                                       |
| **PolicyStatusObject**| JSON representation of the enforcement status of an A1 policy.                             |
| **ProblemDetails**    | JSON representation of the content in a response message with other HTTP error codes (4xx/5xx). |

**URI**

<img src="https://imgur.com/ClS2iAB.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

| **Description**                                         | **URI**                                                                      |
|---------------------------------------------------------|------------------------------------------------------------------------------|
| **URI for A1 policy types**                             | …/policytypes                                                                |
| **Single policy type identified by policy type ID**     | …/policytypes/{policyTypeId}                                                 |
| **URI for A1 policies**                                 | …/policytypes/{policyTypeId}/policies                                        |
| **Single policy identified by policy ID**               | …/policytypes/{policyTypeId}/policies/{policyId}                             |
| **URI for status of a single policy**                   | …/policytypes/{policyTypeId}/policies/{policyId}/status                      |
| **URI for policy notification (notificationDestination)** | A callback URI provided when creating a policy.                              |


**A1-P API**
| Resource                            | URI                                             | HTTP Method | Description                                |
|-------------------------------------|-------------------------------------------------|-------------|--------------------------------------------|
| All Policy Type Identifiers         | /policytypes                                    | GET         | Query all policy type identifiers          |
| Individual Policy Type Object       | /policytypes/{policyTypeId}                     | GET         | Query single policy type                   |
| Individual Policy Object            | /policytypes/{policyTypeId}/policies/{policyId} | PUT         | Create single policy, Update single policy |
|                                     |                                                 | GET         | Query single policy                        |
|                                     |                                                 | DELETE      | Delete single policy                       |
| Individual Policy Status Object     | /policytypes/{policyTypeId}/policies/{policyId}/status | GET         | Query policy status                        |
| All Policy Identifiers              | /policytypes/{policyTypeId}/policies            | GET         | Query all policy identifiers               |
| Notify Policy Status                | {notificationDestination}                       | POST        | Notify policy status                       |


### Service operations for A1 policy types
 <img src="https://imgur.com/Czn5niz.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

 Service operations on policy types is handled using HTTP method

 #### Query policy type identifiers
 <img src="https://imgur.com/QXLzGyu.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

1) The A1-P Consumer sends an HTTP GET request to the A1-P Producer targeting "/policytypes". The message body is empty.
2) The A1-P Producer returns a "200 OK" response with an array of policy type identifiers if successful. If there is an error, the appropriate error code and additional error information are returned.

#### Query policy type
<img src="https://imgur.com/IA7kRPB.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

1) The A1-P Consumer sends an HTTP GET request to the A1-P Producer targeting "/policytypes/{policyTypeId}". The message body is empty.
2) The A1-P Producer returns a "200 OK" response with a PolicyTypeObject if successful. If there is an error, the appropriate error code and additional error information are returned.

To query multiple policy types, process above is done in sequence. For querying all policy types, process above is done for each ID retreived

### Service operations for A1 Policy Types
<img src="https://imgur.com/AQ4wGOk.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">


#### Query Policy ID
<img src="https://imgur.com/St0kjIf.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

1) The A1-P Consumer sends an HTTP GET request to the A1-P Producer targeting "/policytypes/{policyTypeId}/policies". The message body is empty.
2) The A1-P Producer returns a "200 OK" response with an array of policy identifiers if successful. If there is an error, the appropriate error code and additional error information are returned.

For querying all policy ID, operation is done based on each policy type or for each policy type identifier


#### Create Ploicy
<img src="https://imgur.com/F6YwfbV.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

1) The A1-P Consumer generates the policyId and sends an HTTP PUT request to the A1-P Producer at "/policytypes/{policyTypeId}/policies/{policyId}" with a PolicyObject in the message body.
2) The A1-P Producer responds with "201 Created", including the URI of the new policy in the "Location" header and the PolicyObject in the message body. On failure, the appropriate error code and additional error information are returned.

A1-P Consumer shall include a policyTypeId in the URI for the PUT request. The policyTypeId shall be used by the A1-P Producer to select the appropriate schemas to use for validation of the PolicyObject and for PolicyStatus.

For multiple policies creation, operations above is done in sequence


#### Update Policy
<img src="https://imgur.com/l15mwws.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

1) The A1-P Consumer sends an HTTP PUT request to the A1-P Producer at "/policytypes/{policyTypeId}/policies/{policyId}" with a PolicyObject in the message body.
2) The A1-P Producer responds with "200 OK" and the updated PolicyObject. On failure, the appropriate error code and additional error information are returned.
   
The A1-P Consumer may subcribe to policy status and feedback notifications related to the updated policy. Policy status and feedback notifications are subscribed to by including the notificationDestination as a query parameter in the PUT request.

Updating multiple policies is done by above operation done in sequence

#### Query Policy
<img src="https://imgur.com/Ztll8o3.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

1) The A1-P Consumer sends an HTTP GET request to the A1-P Producer at "/policytypes/{policyTypeId}/policies/{policyId}" with an empty message body.
2) The A1-P Producer responds with "200 OK" and the PolicyObject. On failure, the appropriate error code and additional error information are returned.

Multiple policies query is done in sequence of operation above, for all policies it goes through the given id.

#### Delete Policy
<img src="https://imgur.com/9HVFu5G.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

1) The A1-P Consumer sends an HTTP DELETE request to the A1-P Producer at "/policytypes/{policyTypeId}/policies/{policyId}" with an empty message body.
2) The A1-P Producer responds with "204 No Content" on success. On failure, the appropriate error code and additional error information are returned.

#### Query Policy Status
<img src="https://imgur.com/zHChKHT.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

1) The A1-P Consumer sends an HTTP GET request to the A1-P Producer at "/policytypes/{policyTypeId}/policies/{policyId}" with an empty message body.
2) The A1-P Producer responds with "200 OK" and a PolicyStatusObject on success. On failure, the appropriate error code and additional error information are returned.
   
#### Notify Policy Status
<img src="https://imgur.com/ywyVTKw.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

1) The A1-P Producer sends an HTTP POST request to the A1-P Consumer at the notificationDestination URI with a PolicyStatusObject in the message body.
2) The A1-P Consumer responds with "204 No Content" and an empty message body.


**HTTP RESPONSE Code**
| Service Operation    | HTTP Method | HTTP Status Codes               |
|----------------------|-------------|---------------------------------|
| Query policy identifiers | GET     | 200, 404                        |
| Create policy        | PUT         | 201, 400, 404, 409              |
| Update policy        | PUT         | 200, 400, 409                   |
| Query policy         | GET         | 200, 404                        |
| Delete policy        | DELETE      | 204, 404                        |
| Query policy status  | GET         | 200, 404                        |
| Notify policy status | POST        | 204, 400                        |


### EI Service

<img src="https://imgur.com/74oC0SQ.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

| Resource                     | URI                              | HTTP Method | Description                                |
|------------------------------|----------------------------------|-------------|--------------------------------------------|
| All EI Type Identifiers      | /eitypes                         | GET         | Query all EI type identifiers              |
| Individual EI Type           | /eitypes/{eiTypeId}              | GET         | Query EI type                              |
| All EI Jobs                  | /eijobs                          | GET         | Query all EI job identifiers               |
| Individual EI Job            | /eijobs/{eiJobId}                | GET         | Query EI job                               |
|                              |                                  | PUT         | Create/Update EI job                       |
|                              |                                  | DELETE      | Delete EI job                              |
| Individual EI Job Status     | /eijobs/{eiJobId}/status         | GET         | Query EI job status                        |
| Notify EI Status             | {jobStatusNotificationUri}       | POST        | Notify EI job status                       |
| Deliver EI                   | {jobResultUri}                   | POST        | Deliver EI job result           


---



## Test Specification - Non-RT RIC Part
<img src="https://imgur.com/vBlLajk.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

<img src="https://imgur.com/XPtdh01.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">


### Conformance test cases for A1-P Consumer

#### Query Policy Type Test Scenarios
1. **Query All Policy Type Identifiers (Positive Case)**
   - **Description:** Validates querying all policy type identifiers.
   - **Criteria:** DUT must support this query.
   - **Methodology:** Validate GET request with correct URI and empty body.
   - **Expected Result:** Test passes if request validation is successful.

2. **Query Single Policy Type (Positive Case)**
   - **Description:** Validates querying a single policy type by ID.
   - **Criteria:** DUT must support this query.
   - **Methodology:** Validate GET request with correct URI, policyTypeId, and empty body.
   - **Expected Result:** Test passes if request validation is successful.

#### Create Policy Test Scenarios
1. **Create Single Policy (Positive Case)**
   - **Description:** Validates creating a single policy.
   - **Criteria:** DUT must support this creation.
   - **Methodology:** Validate PUT request with correct URI, policyTypeId, policyId, and valid JSON body.
   - **Expected Result:** Test passes if request validation is successful.

#### Query Policy Test Scenarios
1. **Query All Policy Identifiers (Positive Case)**
   - **Description:** Validates querying all policy identifiers.
   - **Criteria:** DUT must support this query.
   - **Methodology:** Validate GET request with correct URI and empty body.
   - **Expected Result:** Test passes if request validation is successful.

2. **Query Single Policy (Positive Case)**
   - **Description:** Validates querying a single policy by ID.
   - **Criteria:** DUT must support this query.
   - **Methodology:** Validate GET request with correct URI, policyTypeId, policyId, and empty body.
   - **Expected Result:** Test passes if request validation is successful.

3. **Query Policy Status (Positive Case)**
   - **Description:** Validates querying the status of a policy.
   - **Criteria:** DUT must support this query.
   - **Methodology:** Validate GET request with correct URI, policyTypeId, policyId, and empty body.
   - **Expected Result:** Test passes if request validation is successful.

#### Update Policy Test Scenarios
1. **Update Single Policy (Positive Case)**
   - **Description:** Validates updating a single policy.
   - **Criteria:** DUT must support this update.
   - **Methodology:** Validate PUT request with correct URI, policyTypeId, policyId, and valid JSON body.
   - **Expected Result:** Test passes if request validation is successful.

#### Delete Policy Test Scenarios
1. **Delete Single Policy (Positive Case)**
   - **Description:** Validates deleting a single policy.
   - **Criteria:** DUT must support this deletion.
   - **Methodology:** Validate DELETE request with correct URI, policyTypeId, policyId, and empty body.
   - **Expected Result:** Test passes if request validation is successful.

#### Notify Policy Status Test Scenarios
1. **Notify Policy Status (Positive Case)**
   - **Description:** Validates notifying policy status.
   - **Criteria:** DUT must support this notification.
   - **Methodology:** Validate notification with correct URI, valid JSON body, and proper status.
   - **Expected Result:** Test passes if the DUT responds with "204 No content".

2. **Notify Policy Status – Schema Validation Failure (Negative Case)**
   - **Description:** Validates failure due to schema validation error.
   - **Criteria:** DUT must support this notification.
   - **Methodology:** Introduce error in the PolicyStatusObject.
   - **Expected Result:** Test passes if the DUT responds with "400 Bad request".

3. **Notify Policy Status – Callback URI Not Supported (Negative Case)**
   - **Description:** Validates failure due to invalid callback URI.
   - **Criteria:** DUT must support this notification.
   - **Methodology:** Introduce error in the callback URI.
   - **Expected Result:** Test passes if the DUT responds with "400 Bad request".
  

### Conformance test cases for A1-EI Producer


#### Query EI Types Test Scenarios

1. **Query EI Type Identifiers (Positive Case)**
- **Purpose:** Test functionality to retrieve EI type identifiers.
- **Entrance Criteria:** DUT supports query EI type identifiers procedure.
- **Methodology:** Send HTTP GET request with correct URI format to DUT.
- **Expected Result:** Receive "200 OK" and validate response body based on DUT's EI type availability.

2. **Query EI Type (Positive Case)**
- **Purpose:** Test functionality to retrieve EI type object.
- **Entrance Criteria:** DUT supports query EI type procedure.
- **Methodology:** Send HTTP GET request with correct URI containing eiTypeId.
- **Expected Result:** Receive "200 OK" with EI type object in response body.

3. **Query EI Type (Negative Case) – eiTypeId Not Supported**
- **Purpose:** Test failure scenario when eiTypeId is not supported.
- **Entrance Criteria:** Same as positive case, but eiTypeId is not available in DUT.
- **Methodology:** Send HTTP GET request with unsupported eiTypeId.
- **Expected Result:** Receive "404 Not Found".

#### Create EI Job Test Scenarios

1. **Create EI Job (Positive Case)**
- **Purpose:** Test functionality to create an EI job.
- **Entrance Criteria:** DUT and test simulator agree on EI type and schemas.
- **Methodology:** Send HTTP PUT request with correct URI and EI job object.
- **Expected Result:** Receive "201 Created" with created EI job object.

2. **Create EI Job (Negative Case) – eiTypeId Not Supported**
- **Purpose:** Test failure scenario when eiTypeId is not supported.
- **Entrance Criteria:** Same as positive case, but eiTypeId is not available in DUT.
- **Methodology:** Send HTTP PUT request with unsupported eiTypeId.
- **Expected Result:** Receive "404 Not Found".

3. **Create EI Job (Negative Case) – Schema Validation Failure**
- **Purpose:** Test failure scenario due to schema validation failure.
- **Entrance Criteria:** DUT and test simulator agree on EI type and schemas.
- **Methodology:** Send HTTP PUT request with incorrect schema.
- **Expected Result:** Receive "400 Bad Request".

#### Query EI Jobs Test Scenarios

1. **Query EI Job Identifiers for a Single EI Type (Positive Case)**
- **Purpose:** Test functionality to retrieve EI job identifiers for a single EI type.
- **Entrance Criteria:** DUT supports query EI job identifiers procedure.
- **Methodology:** Send HTTP GET request with correct URI and eiTypeId.
- **Expected Result:** Receive "200 OK" with EI job identifiers in response body.

2. **Query EI Job Identifiers for a Single EI Type (Negative Case) – eiTypeId Not Supported**
- **Purpose:** Test failure scenario when eiTypeId is not supported.
- **Entrance Criteria:** Same as positive case, but eiTypeId is not available in DUT.
- **Methodology:** Send HTTP GET request with unsupported eiTypeId.
- **Expected Result:** Receive "400 Bad Request".

3. **Query EI Job Identifiers for All EI Types (Positive Case)**
- **Purpose:** Test functionality to retrieve EI job identifiers for all EI types.
- **Entrance Criteria:** DUT supports query EI job identifiers procedure.
- **Methodology:** Send HTTP GET request without specifying eiTypeId.
- **Expected Result:** Receive "200 OK" with EI job identifiers for all EI types in response body.

4. **Query EI Job (Positive Case)**
- **Purpose:** Test functionality to retrieve an EI job.
- **Entrance Criteria:** DUT supports query EI job procedure and EI job exists.
- **Methodology:** Send HTTP GET request with correct URI containing eiJobId.
- **Expected Result:** Receive "200 OK" with EI job object in response body.

5. **Query EI Job (Negative Case) – EI Job Does Not Exist**
- **Purpose:** Test failure scenario when EI job does not exist.
- **Entrance Criteria:** Same as positive case, but eiJobId does not exist in DUT.
- **Methodology:** Send HTTP GET request with non-existent eiJobId.
- **Expected Result:** Receive "404 Not Found".

#### Update EI job test scenarios
Here's a summarized breakdown of the test scenarios for the A1-EI Producer functionality based on the detailed document you provided:

1. **Positive Case:**
- **Purpose:** Test the successful update of an EI job.
- **Entrance Criteria:** DUT supports Update EI job procedure, test simulator can initiate it, EI job exists with known details.
- **Methodology:** Send HTTP PUT request to DUT with correct URI and JSON EiJobObject.
- **Expected Result:** Receive "200 OK" response with updated EiJobObject.

2. **Negative Case - Schema Validation Failure:**
- **Purpose:** Test failure to update EI job due to schema validation error.
- **Entrance Criteria:** Same as positive case.
- **Methodology:** Introduce schema validation error in EiJobObject.
- **Expected Result:** Receive "400 Bad Request" response.

#### Delete EI Job Scenarios

1. **Positive Case:**
- **Purpose:** Test successful deletion of an EI job.
- **Entrance Criteria:** DUT supports Delete EI job procedure, job exists with known ID.
- **Methodology:** Send HTTP DELETE request with correct URI.
- **Expected Result:** Receive "204 No Content" response.

2. **Negative Case - EI Job Does Not Exist:**
- **Purpose:** Test failure to delete non-existent EI job.
- **Entrance Criteria:** Same as positive case, job ID known to not exist.
- **Methodology:** Send HTTP DELETE request with known non-existent ID.
- **Expected Result:** Receive "404 Not Found" response.

#### Query EI Job Status Scenarios

1. **Positive Case:**
- **Purpose:** Test successful retrieval of EI job status.
- **Entrance Criteria:** DUT supports Query EI job status procedure, job exists with known ID.
- **Methodology:** Send HTTP GET request with correct URI.
- **Expected Result:** Receive "200 OK" response with EiJobStatusObject.

2. **Negative Case - EI Job Does Not Exist:**
- **Purpose:** Test failure to query status of non-existent EI job.
- **Entrance Criteria:** Same as positive case, job ID known to not exist.
- **Methodology:** Send HTTP GET request with known non-existent ID.
- **Expected Result:** Receive "404 Not Found" response.

#### Notify EI Job Status Scenarios

1. **Positive Case:**
- **Purpose:** Test successful notification of EI job status.
- **Entrance Criteria:** DUT supports Notify EI job status procedure, job creation criteria apply.
- **Methodology:** Send HTTP POST request with jobStatusNotificationUri.
- **Expected Result:** 
  - Step 2: Receive "201 Created" response.
  - Step 4: Receive "200 OK" response.
  - Step 6: Receive "200 OK" response.

#### Deliver EI Job Result Scenarios

1. **Positive Case:**
- **Purpose:** Test successful delivery of EI job results.
- **Entrance Criteria:** DUT supports Deliver EI job result procedure, job creation criteria apply.
- **Methodology:** Send HTTP POST request with jobResultUri.
- **Expected Result:** 
  - Step 2: Receive "201 Created" response.
  - Step 4: Receive "200 OK" response.

2. **Negative Case - No Callback:**
- **Purpose:** Test failure to deliver EI job results due to missing callback.
- **Entrance Criteria:** Same as positive case, job creation criteria apply.
- **Methodology:** Send HTTP POST request without jobResultUri.
- **Expected Result:** Receive "400 Bad Request" response.


## Test Specification - Near-RT RIC Part


<img src="https://imgur.com/vBlLajk.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

<img src="https://imgur.com/IR3gFyo.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">


### Conformance Test Cases for A1-P Producer
#### Base URI
```{apiRoot}/A1-P/v2/<ResourceUriPart>```

#### Query Policy Type Test Scenarios
1. **6.2.1.1 Query All Policy Type Identifiers (Positive Case)**
   - **Description**: Tests A1-P Producer's query policy types functionality.
   - **Entrance Criteria**: DUT supports query all policy type identifiers.
   - **Methodology**: Sends HTTP GET request with empty body to DUT for different configurations.
     - DUT has single policy
     - DUT has multiple policies
     - DUT has no policies
   - **Method**: `GET`
   - **URI**: `/policytypes`
   - **Expected Result**: Receives "200 OK"; Array with all Policy ID.
  

2. **6.2.1.2 Query Single Policy Type (Positive Case)**
- **Description**: Tests query single policy type functionality.
- **Entrance Criteria**: DUT supports query single policy type.
- **Methodology**: Sends HTTP GET request with policyTypeId to DUT.
- **Method**: `GET`
- **URI**: `/policytypes/{policyTypeID}`
- **Expected Result**: Receives "200 OK"; response contains PolicyTypeObject.

1. **6.2.1.3 Query Single Policy Type (Negative Case) - PolicyTypeId Not Supported**
- **Description**: Tests failure scenario for unsupported policyTypeId.
- **Entrance Criteria**: Similar to positive case but with unsupported policyTypeId.
- **Methodology**: Sends HTTP GET request to DUT.
- **Method**: `GET`
- **URI**: `/policytypes/{policyTypeID}`
- **Expected Result**: Receives "404 Not Found".

#### Create Policy Test Scenarios
1. **6.2.2.1 Create Single Policy (Positive Case)**
- **Description**: Tests create single policy functionality.
- **Entrance Criteria**: DUT supports create single policy. No policy exists in the DUT for the agreed policy type with the same policyId that will be used by the test simulator. Make sure to use supported policyTypeId
- **Methodology**: Sends HTTP PUT request with PolicyObject to DUT. 
- **Method**: `PUT`
- **URI**: `/policytypes/{policyTypeId}/policies/{policyId}`
- **Body**: `PolicyObject`
   ```json
   {
   "name": "tsapolicy",
   "description": "tsa parameters",
   "policy_type_id": policy_type_id,
   "create_schema": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
         "threshold": {
         "type": "integer",
         "default": 0
         }
      },
      "additionalProperties": false
   }
   }
   ```
- **Expected Result**: Receives "201 Created"; response contains PolicyObject and location header.

2. **6.2.2.2 Create Policy (Negative Case) - Schema Validation Failure**
- **Description**: Tests failure scenario for schema validation.
- **Entrance Criteria**: Similar to positive case but with invalid PolicyObject.
- **Methodology**: Sends HTTP PUT request with invalid PolicyObject.
- **Method**: `PUT`
- **URI**: `/policytypes/{policyTypeId}/policies/{policyId}`
- **Body**: `PolicyObject`
   ```json
   {
      "name": "tsapolicy",
      "description": "tsa parameters",
      "policy_type_id": policy_type_id,
      "create_schema": {
         "$schema": "http://json-schema.org/draft-07/schema#",
         "type": "object",
         "properties": {
            "threshold": {
               "type": "integer",
               "default": 0
            }
         },
         "additionalProperties": false
      }
   }
- **Expected Result**: Receives "400 Bad Request".

3. **6.2.2.3 Create Policy (Negative Case) - PolicyTypeId Not Supported**
- **Description**: Tests failure scenario for unsupported policyTypeId.
- **Entrance Criteria**: Similar to positive case but with unsupported policyTypeId.
- **Methodology**: Sends HTTP PUT request with unsupported policyTypeId.
- **Method**: `PUT`
- **URI**: `/policytypes/{policyTypeId}/policies/{policyId}`
- **Body**: `PolicyObject`
   ```json
   {
      "name": "tsapolicy",
      "description": "tsa parameters",
      "policy_type_id": policy_type_id,
      "create_schema": {
         "$schema": "http://json-schema.org/draft-07/schema#",
         "type": "object",
         "properties": {
            "threshold": {
               "type": "integer",
               "default": 0
            }
         },
         "additionalProperties": false
      }
   }
   ```
- **Expected Result**: Receives "404 Not Found".

#### Query Policy Test Scenarios
1. **6.2.3.1 Query All Policy Identifiers (Positive Case)**
- **Description**: Tests query policies functionality.
- **Entrance Criteria**: DUT supports query all policy identifiers.
- **Method**: `GET`
- **URI**: `/policytypes/{policyTypeId}/policies`
- **Methodology**: Sends HTTP GET request to DUT.
- **Expected Result**: Receives "200 OK"; response body is an array varies based on DUT's policies availability.

2. **6.2.3.2 Query All Policy Identifiers (Negative Case) - PolicyTypeId Not Supported**
- **Description**: Tests failure scenario for unsupported policyTypeId.
- **Entrance Criteria**: Similar to positive case but with unsupported policyTypeId.
- **Method**: `GET`
- **URI**: `/policytypes/{policyTypeId}/policies`
- **Methodology**: Sends HTTP GET request to DUT.
- **Expected Result**: Receives "404 Not Found".

3. **6.2.3.3 Query Single Policy (Positive Case)**
- **Description**: Tests query single policy functionality.
- **Entrance Criteria**: DUT supports query single policy.
- **Methodology**: Sends HTTP GET request with policyId to DUT.
- **Method**: `GET`
- **URI**: `/policytypes/{policyTypeId}/policies/{policyId}`
- **Expected Result**: Receives "200 OK"; response contains PolicyObject.

1. **6.2.3.4 Query Single Policy (Negative Case) - Policy Does Not Exist**
- **Description**: Tests failure scenario for non-existent policy.
- **Entrance Criteria**: Similar to positive case but with non-existent policy.
- **Methodology**: Sends HTTP GET request with non-existent policyId to DUT.
- **Method**: `GET`
- **URI**: `/policytypes/{policyTypeId}/policies`
- **Expected Result**: Receives "404 Not Found".

1. **6.2.3.5 Query Policy Status (Positive Case)**
- **Description**: Tests query policy status functionality.
- **Entrance Criteria**: DUT supports query policy status.
- **Methodology**: Sends HTTP GET request with policyId to DUT.
- **Method**: `GET`
- **URI**: `/policytypes/{policyTypeId}/policies/{policyId}/status`
- **Expected Result**: Receives "200 OK"; response contains PolicyStatusObject.

1. **6.2.3.6 Query Policy Status (Negative Case) - Policy Does Not Exist**
- **Description**: Tests failure scenario for non-existent policy.
- **Entrance Criteria**: Similar to positive case but with non-existent policy.
- **Methodology**: Sends HTTP GET request with non-existent policyId to DUT.
- **Method**: `GET`
- **URI**: `/policytypes/{policyTypeId}/policies/{policyId}/status`
- **Expected Result**: Receives "404 Not Found".

#### Update policy test scenarios
1. **6.2.4.1 Update Single Policy (Positive Case)**
   - **Description**: Tests the update policy functionality of A1-P Producer.
   - **Entrance Criteria**: 
     1. The DUT supports the Update single policy procedure.
     2. The test simulator can initiate A1-P Update single policy procedure.
     3. A policy exists in the DUT and the `policyTypeId` and `policyId` are known to the test simulator.
   - **Method**: `PUT`
   - **URI**: `/policytypes/{policyTypeId}/policies/{policyId}`
   - **Methodology**:
     - **Initial Conditions**: The DUT has A1-P Producer service ready to receive HTTP requests from the test simulator.
     - **Procedure**:
       1. Send an HTTP PUT request from the test simulator to the DUT with the correct URI and message body containing the PolicyObject in JSON format.
       2. At the test simulator, record the received HTTP response.
   - **Expected Result**: 
     - The return code is "200 OK".
     - The response message body content matches the PolicyObject sent in Step 1.

2. **6.2.4.2 Update Single Policy (Negative Case) – Schema Validation Failure**
   - **Description**: Tests the update policy functionality of A1-P Producer for schema validation failure.
   - **Entrance Criteria**: 
     1. The DUT supports the Update single policy procedure.
     2. The test simulator can initiate A1-P Update single policy procedure.
     3. A policy exists in the DUT and the `policyTypeId` and `policyId` are known to the test simulator.
   - **Method**: `PUT`
   - **URI**: `/policytypes/{policyTypeId}/policies/{policyId}`
   - **Methodology**:
     - **Initial Conditions**: The DUT has A1-P Producer service ready to receive HTTP requests from the test simulator.
     - **Procedure**:
       1. Send an HTTP PUT request from the test simulator to the DUT with the correct URI and a message body containing the PolicyObject in JSON format with a spelling mistake introduced for schema validation error.
       2. At the test simulator, record the received HTTP response.
   - **Expected Result**: 
     - The return code is "400 Bad Request".
     - Note: Presence or validation of the optional ProblemDetails object in the response is not used to determine validation in this test.

#### Delete Policy Test Scenarios

1. **6.2.5.1 Delete Single Policy (Positive Case)**
   - **Description**: Tests the delete policy functionality of A1-P Producer.
   - **Entrance Criteria**:
     1. The DUT supports the Delete policy procedure.
     2. The test simulator can initiate the Delete policy procedure.
     3. A policy exists in the DUT and the `policyTypeId` and `policyId` are known to the test simulator.
   - **Method**: `DELETE`
   - **URI**: `/policytypes/{policyTypeId}/policies/{policyId}`
   - **Methodology**:
     - **Initial Conditions**: The DUT has A1-P Producer service ready to receive HTTP requests from the test simulator.
     - **Procedure**:
       1. Send an HTTP DELETE request from the test simulator to the DUT with the correct URI format as specified in A1AP [4] clause 6.2.3.
       2. At the test simulator, record the received HTTP response.
   - **Expected Result**: 
     - The return code is "204 No Content".
     - The response message body is empty.

2. **6.2.5.2 Delete Single Policy (Negative Case) – Policy Does Not Exist**
   - **Description**: Tests the delete policy functionality of A1-P Producer when the policy does not exist.
   - **Entrance Criteria**: 
     1. The DUT supports the Delete single policy procedure.
     2. The test simulator can initiate the Delete single policy procedure.
     3. The test simulator is aware of the `policyTypeId` and `policyId` for which no policy exists in the DUT.
   - **Method**: `DELETE`
   - **URI**: `/policytypes/{policyTypeId}/policies/{policyId}`
   - **Methodology**:
     - **Initial Conditions**: 
       1. The DUT has A1-P Producer service ready to receive HTTP requests from the test simulator.
       2. No policy exists in the DUT for the specified `policyTypeId` and `policyId`.
     - **Procedure**:
       1. Send an HTTP DELETE request from the test simulator to the DUT with the correct URI format as specified in A1AP [4] clause 6.2.3 and an empty message body.
       2. At the test simulator, record the received HTTP response.
   - **Expected Result**: 
     - The return code is "404 Not Found".

#### Notify Policy Status Test Scenarios

1. **6.2.6.1 Notify Policy Status (Positive Case)**
   - **Description**: Tests the policy status notification functionality of A1-P Producer.
   - **Entrance Criteria**:
     - The test entrance criteria for creating a single policy as specified in clause 6.2.2.1.2 applies.
   - **Method**: `POST`
   - **URI**: `{notificationDestination}`
   - **Methodology**:
     - **Initial Conditions**: The initial conditions for creating a single policy as specified in clause 6.2.2.1.3.1 apply.
     - **Procedure**:
       1. Same as for creating a single policy, see clause 6.2.2.1.3.2, including the `notificationDestination` query parameter.
       2. At the test simulator, record the received HTTP response.
       3. Repeat Step 1 with another `notificationDestination` query parameter included.
       4. At the test simulator, record the received HTTP response.
       5. Repeat Step 1 without a `notificationDestination` query parameter included.
       6. At the test simulator, record the received HTTP response.
       - Note: Steps 3-4 and 5-6 correspond to the procedure for updating a single policy, but it is not required that the PolicyObject in the message body is modified in the test case for notifying policy status.
   - **Expected Result**:
     - Check the HTTP response recorded in Steps 2, 4, and 6 of the procedure.
     - The test is considered passed if the following conditions are met:
       1. The return code is "201 Created" in Step 2.
       2. The return code is "200 OK" in Step 4.
       3. The return code is "200 OK" in Step 6.


### Conformance test cases for A1-EI Consumer

#### Base URI
```
{apiRoot}/A1-EI/v1/<ResourceUriPart>
```
#### Query EI types test scenarios

1. **6.3.1.1 Query EI type identifiers (positive case)**
   <img src="https://imgur.com/Lba5U2c.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
   - **Description**: Test query EI type identifiers functionality of A1-EI Consumer
   - **Entrance Criteria**: The DUT has functionality to initiate the A1-EI Query EI type identifiers procedure, and the test simulator supports this procedure.
   - **Method**: `GET`
   - **URI**: `/eitypes`
   - **Methodology**: The DUT will send an HTTP GET request to the simulator 
   - **Expected Result**: The simulator sucessfully receives the request by the DUT.

2. **6.3.1.2 Query EI type (positive case)**
   <img src="https://imgur.com/eRQNbWM.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
   - **Description**: Test query EI type functionality of A1-EI Consumer
   - **Entrance Criteria**: The DUT has functionality to initiate the A1-EI Query EI type procedure, and the test has EI types available.
   - **Method**: `GET`
   - **URI**: `/eitypes/{eiTypeId}`
   - **Methodology**: The DUT will send an HTTP GET request to the simulator 
   - **Expected Result**: The simulator sucessfully receives the request by the DUT.
  
#### Create EI job test scenarios

1. **6.3.2.1 Create EI job (positive case)**
   <img src="https://imgur.com/hnDCImq.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
   - **Description**: Test the create EI job functionality of A1-EI Consumer
   - **Entrance Criteria**:
     - The DUT has functionality to initiate the A1-EI Create EI jobs procedure, and the test simulator supports this procedure.
     - The eiTypeId and the JSON schemas of the EI type used for this test are available and used in DUT to formulate the
Create EI job request, and in test simulator to validate the request.
   - **Initial Confition**: No EI job exists in the test simulator for the agreed EI type with the same eiJobId that will be used by the DUT
   - **Method**: `PUT`
   - **URI**: `/eijobs/{eiJobId} (EiJobObject)`
   - **Body**: 
      ```json
      {
      "eiTypeId": "12345",
      "jobResultUri": "https://example.com/ei-job-results/12345",
      "jobOwner": "user@example.com",
      "jobStatusNotificationUri": "https://example.com/ei-job-status/12345",
      "jobDefinition": {}
      }
      ```
   - **Methodology**: The DUT will send an HTTP PUT request to the simulator 
   - **Expected Result**: The simulator sucessfully receives the request by the DUT.

#### Query EI jobs test scenarios

1. **6.3.3.1 Query EI job identifiers for a single EI type (positive case)**
   <img src="https://imgur.com/nOmrqT4.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
   - **Description**: Test query EI job identifiers functionality of A1-EI Consumer
   - **Entrance Criteria**:
     - The DUT has functionality to initiate A1-EI Query EI job identifiers procedure.
     - The test simulator supports at least one EI type.
   - **Initial Confition**: One or more EI jobs exist in the test simulator for each EI type supported.
   - **Method**: `GET`
   - **URI**: `/eijobs`
   - **Methodology**: The DUT will send an HTTP GET request to the simulator
   - **Expected Result**: The simulator sucessfully receives the request by the DUT.
  
2. **6.3.3.2 Query EI job identifiers for all EI types (positive case)**
   <img src="https://imgur.com/nOmrqT4.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
   - **Description**: Test query EI job identifiers functionality of A1-EI Consumer
   - **Entrance Criteria**:
     - The DUT has functionality to initiate A1-EI Query EI job identifiers procedure.
     - The test simulator supports at least one EI type.
   - **Initial Confition**: One or more EI jobs exist in the test simulator for each EI type supported
   - **Method**: `GET`
   - **URI**: `/eijobs`
   - **Methodology**: The DUT will send an HTTP GET request to the simulator 
   - **Expected Result**: The simulator sucessfully receives the request by the DUT.

3. **6.3.3.3 Query EI job (positive case)**
   <img src="https://imgur.com/3Z4EpZD.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
   - **Description**: Test query EI job identifiers functionality of A1-EI Consume
   - **Entrance Criteria**:
     - The test simulator supports at least one EI type.
   - **Initial Confition**: One or more EI jobs exist in the test simulator for each EI type supported
   - **Method**: `GET`
   - **URI**: `/eijobs/{eiJobId}`
   - **Methodology**: The DUT will send an HTTP GET request to the simulator
   - **Simulator Response**: 
   - **Expected Result**: The simulator sucessfully receives the request by the DUT.

#### Update EI job test scenarios

1. **6.3.4.1 Update EI job test scenarios**
   <img src="https://imgur.com/Pl5Cyj8.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
   - **Description**: Test update EI job functionality
   - **Entrance Criteria**:
     - An EI job exists in test simulator and DUT is aware of the eiTypeId and eiJobId
     - The eiTypeId and the JSON schemas of the EI job type used for this test are available in DUT to formulate the
Update EI job request and used by the test simulator for validation purpose.
   - **Method**: `PUT`
   - **URI**: `/eijobs/{eiJobId}`
   - **Methodology**: The DUT will send an HTTP GET request to the simulator
   - **Simulator Response**: 
   - **Expected Result**: The simulator sucessfully receives the request by the DUT.



