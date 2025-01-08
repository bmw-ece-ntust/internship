# OAI Logging Facilities

## Overview
The OAI (Open Air Interface) logging facility is an essential component of the Open Air Interface project, designed to provide detailed logs for debugging, monitoring, and analyzing the performance of the OAI software. Understanding how to effectively use and interpret these logs is crucial for diagnosing issues and ensuring optimal operation.

  ## 1. Logging Levels
  OAI uses various logging levels to categorize the importance and verbosity of log messages:
  * DEBUG: Detailed information for diagnosing problems.
  * INFO: General information about the system's operation.
  * WARN: Indications of potential issues or important situations.
  * ERROR: Critical problems that require immediate attention.
  * FATAL: Severe errors leading to application termination.

  ## 2. Log Categories
  Logs are also categorized to identify which module or component generated the message:
  - RRC: Radio Resource Control
  - MAC: Medium Access Control
  - PHY: Physical Layer
  - S1AP: S1 Application Protocol
  - NAS: Non-Access Stratum
  
  ## 3. Configuration
  Logging behavior can be configured via configuration files or at runtime:
  - Config Files: Specify log levels and output destinations (console, files, etc.).
  - Runtime Controls: Adjust logging levels dynamically without restarting the system.

  ## 4. **Output Destinations**
  Logs can be directed to various output destinations:
  - **Console**: For immediate visibility during development or debugging.
  - **Files**: For long-term storage and post-mortem analysis.
  - **Remote Servers**: Using syslog or similar protocols for centralized log management.

  ## 5. **Log Message Format**
  Each log message typically includes:
  - **Timestamp**: When the log was generated.
  - **Severity Level**: The log level (e.g., INFO, ERROR).
  - **Category**: The system component (e.g., MAC, RRC).
  - **Message Content**: Descriptive information about the event or issue.

  ## 6. **Log Rotation and Management**
  To prevent log files from consuming too much disk space, OAI supports log rotation. Logs are periodically archived, and old logs can be compressed or deleted.

  ## 7. **Debugging with Logs**
  Logs are a critical tool for debugging. By analyzing logs, developers can:
  - Identify the sequence of events leading up to an issue.
  - Correlate messages across different components to diagnose system-wide problems.
  - Verify that system behavior matches expectations during development and testing.



## Reference:
https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/common/utils/LOG/DOC/log.md

