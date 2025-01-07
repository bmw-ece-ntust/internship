# Enabling BLV Developers with LLM-driven Code Debugging Paper Review

BLVRUN is a command line shell script designed to assist developers in the blind low vision (BLV) community by providing a concise and informative summary of traceback errors that occur when running Python code.

## 1. Problem
Debugging Challenges for BLV Developers: Developers with blindness and low vision (BLV) face difficulties in understanding and processing lengthy and unstructured error messages (tracebacks) when running Python code. This process can be time-consuming and frustrating, especially since errors are typically presented in a format that is hard to comprehend.

## 2. Contribution of the Paper
Development of BLVRUN: This paper introduces BLVRUN, a command-line application designed to provide clear and informative summaries of error tracebacks. The main contributions of this research include:
- Providing a tool that enhances accessibility for BLV developers in the debugging process.
- Utilizing a large language model (LLM) that has been fine-tuned to generate more understandable error summaries.
- Allowing BLV developers to continue using their existing workflows without needing to adapt to new tools.

## 3. System Architecture & Basic Concept of the Proposed Method & Performance Metrics
- System Architecture:
  -   Shell Application: BLVRUN is a shell application written in Rust, designed to monitor the output of Python code execution and capture any errors that occur.
  -   CodeLlama Model: It employs the CodeLlama model, which has been fine-tuned with 7 billion parameters, specifically trained on traceback data to generate error summaries.
- Basic Concept:
  -   BLVRUN captures errors generated during code execution and uses the model to produce concise and informative summaries.
  -   The model is optimized by reducing parameter precision to enhance text generation speed.
- Performance Metrics:
  -   The model's performance is evaluated using metrics such as cosine similarity and ROUGE-1 to compare the generated summaries against gold standard summaries of errors.

## 4. 4. How They Use the Results to Ensure the Goal is Achieved?
- Evaluation and Testing: The research includes an evaluation of BLVRUN's performance by comparing the generated summaries with those from larger models. Results indicate that BLVRUN can produce accurate and informative summaries, helping BLV developers understand errors more quickly.
- User Study Plans: The study also outlines plans for conducting user studies to measure the impact of using BLVRUN on the development process for BLV developers, including task performance metrics and psychological impacts such as stress and frustration. The results from these studies will be used to improve the design and functionality of BLVRUN in the future.
