# Log Parsing with Self-Generated In-Context Learning and Self-Correction


This paper introduces introduces AdaParser, an adaptive log parsing framework leveraging large language models (LLMs). It addresses the limitations of existing log parsers by utilizing self-generated in-context learning (SG-ICL) and a self-correction mechanism to enhance accuracy and adaptability to evolving log data.

Key contributions include:
1. A tree-based parser for efficiency.
2. SG-ICL, which maintains a dynamic candidate set to guide the LLM in parsing evolving log data.
3. A template corrector that refines LLM-generated templates to reduce parsing errors.

Extensive experiments on large-scale datasets demonstrate AdaParser's superior performance and robustness compared to state-of-the-art methods, even in zero-shot scenarios. The framework also proves generalizable across various LLMs, significantly improving their log parsing capabilities.

## Problem
This paper identifies two major problems in log parsing, especially using large language models (LLMs):

1. **Inaccuracies in Log Parsing:**
   - LLMs have strong text understanding and generation capabilities, but often produce inaccurate parsing templates. This problem occurs in two forms:
     - Plausible Template: The generated template does not fully match the input log message, for example breaking important information into incorrect variables.
     - Broad Template: The template includes information that should be an important part of the log as variables, thus reducing accuracy for further analysis such as troubleshooting.

4. **Inability to Adapt to Growing Logs:**
  Many LLM-based parsers rely on historical log data to select candidates for demonstration. However, due to frequent software updates, logs grow, making sufficient historical data unavailable. In extreme cases, such as launching a new service, no historical log data is available, resulting in a significant decrease in parsing accuracy.
