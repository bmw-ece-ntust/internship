> Michael Harditya (TEEP)
# **GenAI Usage Review Summary**
GenAI (Generation Artificial Intelligence) is an algorithms or called as AI model that create new content, including audio, text, and videos [3].

GenAI have many branches divided by models and architecture of the algorithms, and the data that is going to be generated. Most of the models and architectures divided into Autoencoder (have its own new branch called Transformers [6]), Autoregressive, Generative Adverarial Network (GAN), Diffusion & Flow-based, and Foundation Model [5]. While the data to be generated are mainly Text and Image, or both (Multimodal).

## **Table of Contents**
- [**GenAI Usage Review Summary**](#genai-usage-review-summary)
  - [**Table of Contents**](#table-of-contents)
  - [**GenAI Usage in Computer Engineering Fields**](#genai-usage-in-computer-engineering-fields)
    - [**TestPilot by Max Schafer et. al.**](#testpilot-by-max-schafer-et-al)
  - [**GenAI Usage in 5G**](#genai-usage-in-5g)
    - [**Network Management**](#network-management)
      - [**LLM-Assisted Intent-Based 5G Core Network Management and Orchestration**](#llm-assisted-intent-based-5g-core-network-management-and-orchestration)
    - [**Interoperability**](#interoperability)
      - [**Poster: A Novel Adaptor Approach for O-RAN Interoperability**](#poster-a-novel-adaptor-approach-for-o-ran-interoperability)
    - [Optimization](#optimization)
      - [**O-RAN Transformer-based Traffic Prediction and Network Optimization**](#o-ran-transformer-based-traffic-prediction-and-network-optimization)
    - [**Usage Guide**](#usage-guide)
      - [**O-RAN Chatbot by Nvidia**](#o-ran-chatbot-by-nvidia)
  - [**References**](#references)

## **GenAI Usage in Computer Engineering Fields**
### **TestPilot by Max Schafer et. al.**
TestPilot is built for generating unit tests for npm packages written in JavaScript/TypeScript using a Large Language Model. it uses Open-AI gpt3.5-turbo on 25 npm packages to create a test case for the code using those 25 npm packages. There are no fine-tuning approach, but mainly about deployment into GitHub releases.

![alt text](../images/TestPilot.png)
TestPilot Architecture [1].

TestPilot uses five main components:
1. API Explorer, analyzes the PUT to determine its API, includes set of functions, methods, constants, etc that is not private in the package (the code used as test case).
2. Documentation Miner, extract code snippets and comments from both separated documentation files, and inside code snippets. Authors mentioned about the limitation of the miner and using the doc comment (/**...*/)
3. Prompt Generator, constructs an initial prompt to send to the LLM for generating a test for a given function f, which has one signature and let the prompt refiner creates more metadata.
4. Test Validator, validate the candidate tests generated from the LLM, especially in syntatic errors using Mocha test runners.
5. Prompt Refiner, generate additional prompts to use for querying the model. It adds another prompts based on the cases happened in Test Validator.

LLM Model only used to generate candidate tests from the prompt generator, and all components in TestPilot doesn't use any LLM or AI algorithm, only hard coded rules. Note that the model using OpenAI inference server using it's API, without any training or architecture process.

## **GenAI Usage in 5G**
### **Network Management**
#### **LLM-Assisted Intent-Based 5G Core Network Management and Orchestration**
The paper proposes intent-based 5G Core by adding Semantic Router to process user prompts that translates the prompts into various commands to the core. Semantic Router itself is a method of deterministic decision-making of semantic meaning to route an input to the desired output. Semantic router enhance stability and reliability in LLM deployment, because its ability to define explicit routes without performance deterioration due to LLM hallucinations. There are 6 routes used in the semantic router: deployment, modification, performance assurance, intent report, intent feasibility, and regular notification.

![alt text](../images/intent-based.png)

Semantic Router Intents used in the paper [8].

Each routes use base utterances, and re-generated with three kind of prompts that has the same output. The paper mentioned about accuracy improvements between normal prompting with the usage of Semantic Router. 
dataset can be found in https://github.com/Western-OC2-Lab/

The LLM used by building prompts for each intents, consists of Role, Task Description, Background Context, and Expected Behaviour.

| Intent Type | Intent Structure Example |
| --- | --- |
|Deployment Intent|"Deploy a new network in [region] with the following specifications..."|
|Modification Intent| “Modify the existing [network] to address the performance issues caused by high loading...” |
|Performance Assurance Intent| “Ensure that the deployed network can support a [QoS Level] application with the following requirements...”|
|Intent Report Request|“Summarize the results of the previous request.”|
|Intent Feasibility Check|“Before proceeding, ensure that capacity exists in [region] to perform the required changes.”|
|Regular Notification Request|“Notify me of the status of [network] every [frequency].”|

5G Core intent types and examples [9]

### **Interoperability**
#### **Poster: A Novel Adaptor Approach for O-RAN Interoperability**
The paper [10] proposed AOR (Adaptor for O-RAN) that supposed to be a middleware between RAN components and its RIC (Near-Real-Time RAN Intelligent Controller). It serve as a bridge for multi-vendor and components of O-RAN devices, as another option of the current O-RAN E2 Application Protocol. AOR divided by three stage procedures:
1. Spec. Extraction: extracts a formal model from specifications using LLM, it will describe the standardized behaviour of O-RAN component when initiating new procedure and behaviour according to input message.
2. Testing-based Fine-tuning: capture discrepancies in implementation, by cross-validates model through online testing. It is done by learning differences in terms of implementation and service models by analyzing the real-time traffic and record any behaviour that is different from the standardized model.
3. Adapting Path Searching: after each component have its fine tuned model, AOR then check once more for possible compatibility issues. For each issue, AOR search for adapting paths from state machines.

### Optimization

#### **O-RAN Transformer-based Traffic Prediction and Network Optimization**
Transformer is an architecture of a machine learning algorithm that is popular in processing sequence data. It is implemented in this scenario to predict traffic in 5G, and optimize the network by defining a threshold for RIC application using the predicted values. The anticipated traffic generated by the Transformer is used in reinforcement leanring-based traffic steering xApp, or cell sleeping rApp to enhance the performance of the network [7]. The author mentions the energy efficiency gone up by 39.7% compared to the 'always on traffic steering xApp' and 10.1% increase in throughput compared to the 'always on cell sleeping rApp'.

![alt text](../images/traffic-pred.png)

Traffic prediction and network optimization [7].

### **Usage Guide**

#### **O-RAN Chatbot by Nvidia**
O-RAN Chatbot is another example of GenAI Examples from Nvidia that showcase the usage of Nvidia environments and products, especially Nvidia AI Foundation Endpoints and NIM. NVIDIA NIM is a set of easy-to-use microservices for accelerating the deployment of foundation models on any cloud or data center and helps keep your data secure. The chatbot implements Retrieval Augmented Generation that works by storing related documents into a vector database, then using similarity algorithm between the prompt and use the similar data as context in chatbot model to generate a response based on the context alone.

![alt text](../images/demo-debrief.png)
O-RAN Chatbot demo [4].

From the codes, the example uses streamlit as the front end UI. The framework uses LangChain which is possible for multiple processes as one chain. Some features also introduced in the example.

The Chatbot model use Mixtral 8x7B, which is a large language model with 7B parameters specialized in generating responses. Only one LLM Model used in the whole architecture.

## **References**
[1] Max Schafer, et. al.; An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation; https://arxiv.org/pdf/2302.06527

[2] Nvidia; GenerativeAIExamples: O-RAN ChatBot Multimodal; https://github.com/NVIDIA/GenerativeAIExamples/tree/main/experimental/oran-chatbot-multimodal

[3] McKinsey; What is generative AI?; https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-generative-ai#/

[4] Nvidia; Demo Debrief: O-RAN Chat Bot; Feb 19, 2024.

[5] B. Decardi-Nelson, et. al.; Generative AI and process systems engineering: The next frontier; Computers and Chemical Engineering; 2024; https://doi.org/10.1016/j.compchemeng.2024.108723

[6] Yi Tay, et. al.; Efficient Transformers: A Survey; ACM Computing Surveys 55 No. 6; 2022; https://doi.org/10.1145/3530811

[7] Md Arafat Habib, et. al.; Tranformer-Based Wireless Traffic Prediction and Network Optimization in O-RAN; IEEE; 2023; https://arxiv.org/pdf/2403.10808

[8] Dimitrios Michael Manias, et.al.; Semantic Routing for Enhanced Performance of LLM-Assisted Intent-Based 5G Core Network Management and Orchestration; 2024; ArXiv; https://arxiv.org/pdf/2404.15869

[9] Dimitrios Michael Manias, et.al.;Towards Intent-Based Network Management: Large Language Model for Intent Extraction in 5G Core Networks; 2024; ArXiv; https://arxiv.org/pdf/2404.15869

[10] Sixu Tan; et. al.; Poster: A Novel Adaptor Approach for O-RAN Interoperability; 2024; Proceedings of the 25th International Workshop on Mobile Computing Systems and Applications; HOTMOBILE '24: Proceedings of the 25th International Workshop on Mobile Computing Systems and Applications
; ACM Digital Library