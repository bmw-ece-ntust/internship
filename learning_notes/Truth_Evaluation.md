# Truthfulness Evaluation

## Table of Contents
- [Truthfulness Evaluation](#truthfulness-evaluation)
  - [Table of Contents](#table-of-contents)
  - [Ragas](#ragas)
    - [Available Metrics](#available-metrics)
      - [Faithfulness](#faithfulness)
      - [Answer Relevance](#answer-relevance)
  - [Heuristic Evaluation](#heuristic-evaluation)
    - [Consistency Check](#consistency-check)


## Ragas
Ragas is an open standard for RAG applications, it provides several tools to generate test dataset, LLM-assisted evaluation metrics, and quality monitoring. Ragas facilitate Metrics-Driven Development (MDD), an product development approach that relies on data to make well-informed decisions. Ragas use LLM in generating evaluation metric scores, so it can be inferred that Ragas use the game approach.
### Available Metrics
#### Faithfulness
Measures factual consistency of the generated answer against the given context, calculated from answer and retrieved context from 0 to 1, where higher is better. Generated answer said to be faithful if all the 'claims' in the response of the bot can be inferred came from the given context. 

$$ Faithfulness=\frac{\sum claims_{from context}}{\sum claims}$$

`ragas` library calculate this faithfulness by breaking response into individual statements, then each statements (as claims) verified back from the given context.

#### Answer Relevance
Measures the relevancy of the generated answer to the given prompt. Lower score indicate answers that are incomplete or contain redundant information while higher score indicate better relevancy. It is defined as the mean cosine similarity of the original question to a number of artificial questions, which is generated based on the answer. This resulting not the factuality of the question actually answered, but penalize if the answer lacks of completeness or contains redundant details.
$$ Relevance_{answer} = \frac{1}{N}\sum^N_{i=1}\frac{E_{gi}\cdot{E_o}}{||E_{gi}||||E_o||}$$
- $E_{gi}$ is the embedding of the generated question $i$.
- $E{o}$ is the embedding of the original question.
- $N$ is the number of generated questions.

## Heuristic Evaluation

### Consistency Check
This evaluation use multiple time of inferencing to get multiple responses from the same context and query. If the responses are similar (for the same context and prompt), it is likely to be truthful.