# Chatbot Evaluation

## Table of Contents
- [Chatbot Evaluation](#chatbot-evaluation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Faithfulness](#faithfulness)
  - [About Indirect Claims](#about-indirect-claims)
  - [Answer Relevance](#answer-relevance)
  - [Tools](#tools)
    - [Ragas](#ragas)
  - [References](#references)

## Introduction
Chatbot evaluation is generally aligned with the ISO 9214 concept of usability, defined into three fields [1][2]:
1. **Efficiency**, related to the *performance* towards the goal.
2. **Effectiveness**, about *functionality* and *humanity*.
3. **Satisfaction**, about *affect* in emotional meanings, *ethics and behaviour*, also *accessibility*.

research paper usually doesn't use the three of them simultaneously, but only pick the nearest evaluation to give key points of what is the model has achieved towards the research goal [2].
[1] mention about the trend of research papers that evaluate **Efficiency**,**Effectiveness**, and **Satifaction** changes periodically.

## Faithfulness
[3] explained about the different faithfulness problem between open-ended Natural Language Generation (NLG) tasks, and Non-open-ended NLG task:
- In Non-open-ended NLG, NLG models generate text based on the input which provides complete/more information for the output text. The faithfulness problem in this field is the generated text is *factually consistent* with the input document.
- In open-ended NLG, models need to leverage knowledge in the knowledge base or corpus to create new content that is not from the input. The faithfulness problem in this field is whether the generated content is factually consistent with the world knowledge/commonsense, referred as *factual correctness*.

In term of RAG, it is derived from dialogue generation, so *factual consistency* is the goal of faithfulness evaluation.


Measures factual consistency of the generated answer against the given context, calculated from answer and retrieved context from 0 to 1, where higher is better. Generated answer said to be faithful if all the 'claims' in the response of the bot can be inferred came from the given context. 

$$ Faithfulness=\frac{\sum claims_{from context}}{\sum claims}$$

`ragas` library calculate this faithfulness by breaking response into individual statements, then each statements (as claims) verified back from the given context.

## About Indirect Claims
In term of our implementation to report a time series data, it is possible that the insights came not from the context, but from the context with additional analytical process. For example the average of one feature, or abnormalities. This leads to problem for existing **Faithfulness** method because it only score based on the texts.

Another option is *Human Evaluation*, another method that is more *human-centric* evaluation that relies on human intervention in evaluate a system. Most of human evaluation used to evaluate **Satifaction** since it is hard to be measured and very subjective [4].

Since **Faithfulness** is tends to evaluate *functionality* in **Effectiveness**, and the context is actually a numerical data, it is possible to use human evaluation objectively by doing analytical process in the context data to generate **ground truth**s. These ground truths then used to check the claims of the generated content, resulting an objective and countable evaluation.

![img](../images/oran-RAG-Faithfulness%20Evaluation.png)


## Answer Relevance
Measures the relevancy of the generated answer to the given prompt. Lower score indicate answers that are incomplete or contain redundant information while higher score indicate better relevancy. It is defined as the mean cosine similarity of the original question to a number of artificial questions, which is generated based on the answer. This resulting not the factuality of the question actually answered, but penalize if the answer lacks of completeness or contains redundant details.

$$ Relevance_{answer} = \frac{1}{N}\sum^N_{i=1}\frac{E_{gi}\cdot{E_o}}{||E_{gi}||||E_o||}$$

- $E_{gi}$ is the embedding of the generated question $i$.
- $E{o}$ is the embedding of the original question.
- $N$ is the number of generated questions.



## Tools
### Ragas
Ragas is an open standard for RAG applications, it provides several tools to generate test dataset, LLM-assisted evaluation metrics, and quality monitoring. Ragas facilitate Metrics-Driven Development (MDD), an product development approach that relies on data to make well-informed decisions. Ragas use LLM in generating evaluation metric scores, so it can be inferred that Ragas use the game approach.


## References
[1] J. Casas, et. al.; Trends & Methods in Chatbot Evaluation; ICMI '20 Companion; 2020; Netherlands

[2] R., Nicole and B., Morgan; Evaluating Quality of Chatbots and Intelligent Conversational Agents; ArXiv 1704.04579

[3] L. Wei, et. al.;Faithfulness in Natural Language Generation: A
Systematic Survey of Analysis, Evaluation and
Optimization Methods; working paper; arXiv:2203.05227v1

[4] G., Salvatore, et. al.; Human-Centered Metrics for Dialogue System Evaluation; working paper; arXiv:2305.14757v1