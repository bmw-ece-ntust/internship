> Michael Harditya (TEEP)
# Retrieved Augmented Generation (RAG) Review Summary
RAG is a system that use natural language processing  for generation task, added with a retriever system. This summary is going to define it's components, and how it works, and possible application. Several informations are gathered from sources, but some are deductive based on the same sources.
## **Table of Contents**
- [**Table of Contents**](#table-of-contents)
- [**RAG Components**](#rag-components)
    - [**Text Generator Model**](#text-generator-model)
    - [**Retriever**](#retriever)
    - [**Data Framework**](#data-framework)
- [**How RAG Works**](#how-rag-works)
- [**LangChain**](#langchain)
- [**Example Application**](#example-application)

## RAG Components
RAG have two main components that makes RAG different than others. The first one is the usage of Large-Language Model (LLM) to generate a response based on the user prompt, added with the usage of a retriever system that process the prompt first to a local database to find connected information before sending it into the LLM.

Both the LLM and the Retriever, are managed by a Data Framework which is the third component that make RAG ready to use.

### Text Generator Model
RAG use a LLM model that is specifically used to generate response. This type of LLM model is called **Sequence to Sequence Model, a machine learning model that takes a sequence of characters (and words) and give back another different sequence of characters (and also, words).** The main difference between a normal Sequence to Sequence model then a Question Answering (another name for a model that generate response based on the question) is the input of Question Answering model needed. The QA Model use two kind of inputs (in the shape of sequence), the first one is the prompt or the question that has to be answered by the model, and the second one is the context to provide additional information for the model to answer. RAG append the context part with the Retriever component.

There are many possible sequence to sequence LLM that is ready to be used, such as Llama, GPT, RoBERTa, T5, FLAN, and many others (see: [HuggingFace](https://huggingface.co/models)).

### Retriever
Retriever is a component that pulls information from local database that has connection to the prompt. NVidia use the term *Embedding Model* to find the matching document with the user prompt. **This model is an algorithmic program that group together closely related terms in a vector spaces**, some of the model use Machine Learning models. Pulling the related term in the document can be done easily by accessing the vector spaces, and find the closely related term from the prompt. Models can also be found in HuggingFace, with the type of Sentence Similarity.

### Data Framework
This framework is the tool to integrate both the LLM Generator and the Retriever. **Data Framework task is to direct inputs and outputs of each components.** One example of a data framework that can be used for RAG is [LangChain](https://www.langchain.com/).

## How RAG Works
RAG works by this:
1. User send a prompt to the Data Framework, usually in the shape of question.
2. Then the framework sends the prompt into the Embedding Model, to get the embeddings that can be used as query for the local database.
3. The framework forwards the query into the database (which is usually a vector database to haste the output). The database then generate a context, another sequence that usually used for a LLM to understand the context of the prompt.
4. The framework then forwards the prompt and the context to the LLM Model, and it generates the answer.
5. The answer then forwarded into the user as the final answer.

## LangChain
LangChain is a framework that specialize in building application for language models. It is easy to use, develop, and deploy, and the greatest of all, it can be used in python.

There are three types of components in LangChain especially for RAG implementation. Components in LangChain is called as Chains. Chains are component that is going to be executed sequentially, where the output of the previous Chain is connected to the next Chain. The first two components are Chains, which are:
- LLMModel, used to make inference or response based on the question asked previously.
- Retriever, used when the information is too big to be processed by the LLModel, so only few relevant information is selected before being passed into the LLMModel.

The last one is Agent, it serve for multi-sequence action, used to branch Chains to make it dynamically possible when generating a response.

## Example Application
here is the example published by LangChain itself: [LangChain RAG](https://python.langchain.com/docs/expression_language/cookbook/retrieval).