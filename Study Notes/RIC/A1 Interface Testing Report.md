# A1 Interface Testing Report

## Southbound (Near-RT RIC as the DUT)

### Conformance Test Cases for A1-P Producer

| **DUT** |                      |
|---------------|--------------------------------------|
| **OS**        | Ubuntu Desktop 20.04                 |
| **RIC**       | OSC Release I                        |
| **DUT IP**    | 192.168.106.157                      |
| **apiRoot**   | `192.168.106.157:8000/a1mediator`    |
| **baseUrl**   | `192.168.106.157:8000/a1mediator/A1-P/v2` |


---
#### 6.2.1.1 Query All Policy Type Identifiers (Positive Case)
- [x] Test passed, response code and body match the TS

- **Test URI**: `{{baseUrl}}/policytypes`
- **Method**: GET
- **Curl Command**: <br>
    ```sh
    curl --location '192.168.106.157:8000/a1mediator/A1-P/v2/policytypes'
    ```
- **Response**:<br>
    <img src="https://imgur.com/BiF2smJ.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
- **a1mediator log**:<br> 
    ```
    {"ts":1721630796941,"crit":"DEBUG","id":"a1","mdc":{},"msg":"keys : [a1.policy_inst_metadata.21003.0001 a1.policy_inst_metadata.20008.100 a1.policy_type.20009 a1.policy_instance.21003.0001 a1.policy_inst_metadata.20008.1000 a1.policy_inst_metadata.20008.200 a1.policy_inst_metadata.21003.100 a1.policy_instance.21003.200 a1.policy_inst_metadata.21003.200 a1.policy_type.20008 a1.policy_inst_metadata.20008.400 a1.policy_instance.21003.100 a1.policy_type.21003 a1.policy_inst_metadata.20008.300]"}
    ```



#### 6.2.1.2 Query Single Policy Type (Positive Case)
- [x] Test passed, response code and body match the TS
- **Test URI**: `{{baseUrl}}/policytypes/:policyTypeId`
- **Method**: GET
- **Curl Command**: <br>
    ```sh
    curl --location '192.168.106.157:8000/a1mediator/A1-P/v2/policytypes/21003'
    ```
- **Response**:<br>
    <img src="https://imgur.com/kyd63f2.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
- **a1mediator log**:<br> 
    <img src="https://imgur.com/bA2CV15.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">


#### 6.2.1.3 Query Single Policy Type (Negative Case) - PolicyTypeId Not Supported
- [x] Test passed, response code match the TS
- **Test URI**: `{{baseUrl}}/policytypes/:policyTypeId`
- **Method**: GET
- **Curl Command**: <br>
    ```sh
    curl --location '192.168.106.157:8000/a1mediator/A1-P/v2/policytypes/100'
    ```
- **Response**:<br>
    <img src="https://imgur.com/ApJ5z7O.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
- **a1mediator log**:<br> 
    <img src="https://imgur.com/d8xo8pb.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
#### 6.2.2.1 Create Single Policy (Positive Case)
- [ ] 201 Response Code
- [ ] Response Body include PolicyObject representing the created object
- [ ] Response header contains location
- **Test URI**: `{{baseUrl}}/policytypes/:policyTypeId/policies/:policyId`
- **Method**: PUT
- **Curl Command**: <br>
    ```sh
    curl --location --request PUT '192.168.106.157:8000/a1mediator/A1-P/v2/policytypes/21003/policies/003' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --data '{
    "name": "tsapolicy",
    "description": "tsa parameters",
    "policy_type_id": "20008",
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
    }'
    ```
- **Response**:<br>
    <img src="https://imgur.com/3aP5JeG.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
- **a1mediator log**:<br> 
    <img src="https://imgur.com/tujAY9k.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
#### 6.2.2.2 Create Policy (Negative Case) - Schema Validation Failure
- [x] 400 Bad Request Response Code
- **Test URI**: `{{baseUrl}}/policytypes/:policyTypeId/policies/:policyId`
- **Method**: PUT
- **Curl Command**: <br>
    ```sh
    curl --location --request PUT '192.168.106.157:8000/a1mediator/A1-P/v2/policytypes/21003/policies/0002' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --data '{
        "class":12,
        "enforce":true,
        "window_length":20,
        "blocking_rate":20,
        "trigger_threshold":10
    }'
    ```
- **Response**:<br>
    <img src="https://imgur.com/bwb4D0u.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
- **a1mediator log**:<br> 
    <img src="https://imgur.com/2NYrgVa.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">

#### 6.2.2.3 Create Policy (Negative Case) - PolicyTypeId Not Supported
- [ ] 404 Not Found Response Code
- **Test URI**: `{{baseUrl}}/policytypes/:policyTypeId/policies/:policyId`
- **Method**: PUT
- **Curl Command**: <br>
    ```sh
    curl --location --request PUT '192.168.106.157:8000/a1mediator/A1-P/v2/policytypes/21003/policies/0002' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --data '{
        "class":12,
        "enforce":true,
        "window_length":20,
        "blocking_rate":20,
        "trigger_threshold":10
    }'
    ```
- **Response**:<br>
    <img src="https://imgur.com/3aP5JeG.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
- **a1mediator log**:<br> 
    <img src="https://imgur.com/tujAY9k.png" alt="Chart" width="300" style="background-color: white; padding: 10px; border-radius: 5px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5);">
#### 6.2.3.1 Query All Policy Identifiers (Positive Case)
#### 6.2.3.2 Query All Policy Identifiers (Negative Case) - PolicyTypeId Not Supported
#### 6.2.3.3 Query Single Policy (Positive Case)
#### 6.2.3.4 Query Single Policy (Negative Case) - Policy Does Not Exist
#### 6.2.3.5 Query Policy Status (Positive Case)
#### 6.2.3.6 Query Policy Status (Negative Case) - Policy Does Not Exist
#### 6.2.4.1 Update Single Policy (Positive Case)
#### 6.2.4.2 Update Single Policy (Negative Case) – Schema Validation Failure
#### 6.2.5.1 Delete Single Policy (Positive Case)
#### 6.2.5.2 Delete Single Policy (Negative Case) – Policy Does Not Exist
#### 6.2.6.1 Notify Policy Status (Positive Case)
