# LEVERAGING PRINT DEBUGGING paper review

https://openreview.net/pdf?id=zfLf2qniFH

## 1. Problem
- Limitations of LLMs: Although large language models (LLMs) have shown significant advancements in code generation tasks, their performance remains suboptimal when faced with programming problems involving complex data structures and algorithms. For instance, the accuracy of GPT-4 on easy Leetcode problems reaches about 76%, but only 26% for medium-level problems and 7% for hard-level problems.
- Existing Debugging Methods: Existing debugging methods, such as Reflexion and Self-debug, do not provide access to real-time variable values or the ability to trace execution flow, which are crucial for debugging code involving complex algorithms.
## 2. Contribution of the Paper
- New Approach: This paper proposes a contextual learning approach that leverages print debugging to assist LLMs in fixing code. This involves inserting print statements to track and analyze logs to identify and correct bugs.
- Dataset and Evaluation: The authors collected a dataset of Leetcode problems and evaluated their method using the Leetcode online judging system. Experimental results demonstrate that this approach outperforms other debugging techniques, such as rubber duck debugging, with significant accuracy improvements.

