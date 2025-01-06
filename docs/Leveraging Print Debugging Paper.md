# LEVERAGING PRINT DEBUGGING paper review

https://openreview.net/pdf?id=zfLf2qniFH

## 1. Problem
- Limitations of LLMs: Although large language models (LLMs) have shown significant advancements in code generation tasks, their performance remains suboptimal when faced with programming problems involving complex data structures and algorithms. For instance, the accuracy of GPT-4 on easy Leetcode problems reaches about 76%, but only 26% for medium-level problems and 7% for hard-level problems.
- Existing Debugging Methods: Existing debugging methods, such as Reflexion and Self-debug, do not provide access to real-time variable values or the ability to trace execution flow, which are crucial for debugging code involving complex algorithms.
## 2. Contribution of the Paper
- New Approach: This paper proposes a contextual learning approach that leverages print debugging to assist LLMs in fixing code. This involves adding print statements to track and analyze logs to identify and correct bugs.
- Dataset and Evaluation: The authors collected a dataset of Leetcode problems and evaluated their method using the Leetcode online judging system. Experimental results show that this approach outperforms other debugging techniques, such as rubber duck debugging, with significant accuracy improvements.
## 3. System Architecture & Basic Concept of the Proposed Method & Performance Metrics
- System Architecture: The proposed method involves three main steps:
    - Adding Print Statements: LLMs insert print statements into the problematic code to track variable values and execution flow.
    - Execution: The modified code is executed, and the output from the print statements is collected as logs.
    - Analysis and Correction: LLMs analyze the logs and explain test cases to identify inconsistencies indicating bugs, then correct the code based on that analysis.
- Performance Metrics: Accuracy is used as the evaluation metric, representing the percentage of problems that successfully pass all test cases.
## 4.  How They Use the Results to Ensure the Goal is Achieved
- Iterative Debugging: The debugging process is conducted iteratively until all test cases are passed or a predetermined stopping criterion is reached. If the LLM fails on a specific test case, it is prompted to add print statements, run the code, and analyze the output to find the bug.
- Ablation Study: The authors conducted an ablation study to analyze the effectiveness of different components in their method. Results showed that removing parts of the analysis process led to a decrease in performance, emphasizing the importance of both test case explanations and logs in effective debugging.
- Experimental Results: Experimental results indicate that the print debugging method significantly enhances the performance of LLMs in solving Leetcode problems, particularly at the easy and medium levels, compared to other debugging methods.
