![image](https://github.com/bmw-ece-ntust/internship/assets/138283247/045aab7e-fe83-4487-a0ca-62bcdfeeebca)

# Threat Intelligence Survey and Collection

Threat intelligence survey and collection in cybersecurity blue teaming involve the systematic gathering and analysis of information about potential or current attacks that threaten the security of an organization. Blue teams use this intelligence to understand the tactics, techniques, and procedures (TTPs) of adversaries, which helps them to strengthen their defenses and prepare for potential cyber threats.

### First of all, survey.

This is the initial phase where blue teams identify and collect data on various cyber threats. They may use open-source intelligence (OSINT), social media, dark web monitoring, and other sources to gather information. The ‘survey’ phase in threat intelligence for cybersecurity blue teaming is a critical step that involves the systematic collection of information about potential or current cyber threats. This phase is about gathering as much data as possible to understand the threat landscape and identify any vulnerabilities that could be exploited by adversaries.

1. Data Collection: Blue teams collect data from a variety of sources, including open-source intelligence (OSINT), social media, dark web forums, and more. They use tools and techniques to monitor these sources for any signs of malicious activity or chatter that could indicate a looming threat.
2. Thread Identification: The collected data is then analyzed to identify potential threats. This involves looking for patterns, anomalies, and indicators of compromise (IoCs) that could signal an attack in progress or a planned one.
3. Prioritization: Not all threats are equal, so blue teams prioritize them based on factors such as the potential impact on the organization, the likelihood of an attack, and the value of the targeted assets.
4. Reporting: The findings from the survey phase are compiled into reports that provide actionable insights. These reports help inform decision-makers within the organization about the current threat landscape and guide them in strengthening their defenses.

The survey phase is essential because it sets the foundation for all subsequent actions in threat intelligence. By understanding what threats exist and where vulnerabilities lie, blue teams can develop targeted strategies to protect against cyber attacks. It’s a proactive approach that aims to stay one step ahead of potential adversaries.

### And then, collection.

In this phase, blue teams actively gather detailed information about specific threats. This can include malware samples, attack patterns, and indicators of compromise (IoCs). The ‘collection’ phase in threat intelligence for cybersecurity blue teaming is a detailed process that involves gathering specific information about cyber threats. This phase is crucial for building a comprehensive understanding of the threats that an organization may face.

1. Data Gathering: Blue teams use a variety of tools and techniques to collect data from multiple sources. This includes network traffic analysis, log file examination, and the use of specialized software to capture and analyze data.
2. Malware Analysis: When malware is detected, it is collected for analysis. This involves examining the malware’s code, behavior, and communication patterns to understand its capabilities and potential impact.
3. Threat Hunting: Blue teams actively search for threats that have not been detected by traditional security measures. This proactive approach involves looking for anomalies or patterns that could indicate a security incident.
4. Information Sharing: Collected threat intelligence is often shared with other organizations and security communities. This collaboration helps improve the overall security posture by leveraging shared knowledge and experiences.

The collection phase is essential because it provides the raw data needed for the subsequent analysis phase. By collecting detailed information about threats, blue teams can better understand the tactics, techniques, and procedures used by adversaries, which in turn helps them to develop more effective defense strategies.

### Those are the main tasks, but we need to analyze and disseminate too.

The collected data is then analyzed to identify trends, assess risks, and determine the potential impact on the organization. The insights gained from the analysis are shared with relevant stakeholders within the organization to inform decision-making and response strategies. By conducting threat intelligence surveys and collection, blue teams can proactively defend against cyber attacks by staying informed about emerging threats and adjusting their defense strategies accordingly.

### These are the necessary tools to do the tasks!

1. Network Scanners: Tools like Nmap, Masscan, and Angry IP Scanner are used for network discovery and mapping.
2. Vulnerability Scanners: OpenVAS, Nessus, and Nexpose help identify vulnerabilities within systems.
3. Security Monitoring Tools: Sysmon, Kibana, and Logstash are used for system monitoring and data visualization.
4. Threat Intelligence Platforms: Maltego, MISP, and ThreatConnect provide platforms for sharing and analyzing threat intelligence.
5. Malware Analysis Tools: CyberChef, YARA, and velociraptor are used for analyzing malware samples.
6. Incident Response Tools: Tools like chainsaw and freq assist in forensic analysis during incident response.

Then again, the rest can be seen in https://github.com/A-poc/BlueTeam-Tools.

# Detection Rule Implementation

In cybersecurity, the implementation of detection rules by The Blue Team is a critical part of blueteaming, as it involves setting up systems to identify and respond to potential security incidents. By implementing robust detection rules, Blue Teams play a vital role in maintaining the security and integrity of an organization’s information systems.

1. Identify Threats: The Blue Team starts by understanding the types of threats that could target their systems. This includes malware, phishing attacks, unauthorized access attempts, and more.
2. Develop Detection Rules: Based on the identified threats, the Blue Team develops detection rules. These rules are criteria or patterns that security tools use to identify suspicious activities. For example, a rule might flag multiple failed login attempts from a single IP address as potential unauthorized access.
3. Implement Security Tools: The Blue Team implements security tools like intrusion detection systems (IDS), security information and event management (SIEM) systems, and firewalls. These tools use the detection rules to monitor network traffic and system activities.
4. Monitor and Respond: With the detection rules in place, the Blue Team continuously monitors the security tools for alerts. When an alert is triggered, indicating a potential threat, the team investigates and responds accordingly to mitigate the risk.
5. Update Rules Regularly: Cyber threats evolve rapidly, so it’s essential for the Blue Team to regularly update their detection rules to keep up with new types of attacks and vulnerabilities.
6. Collaborate with Red Teams: Sometimes, Blue Teams work alongside Red Teams (who simulate attacks) to test and improve the effectiveness of detection rules. This collaboration helps ensure that the Blue Team is prepared for real-world cyberattacks.

### What are the common detection rule patterns?

Common detection rule patterns in cybersecurity are designed to identify potential threats by recognizing specific behaviors or attributes associated with malicious activities. These patterns are integral to the functionality of security tools like antivirus software and intrusion detection systems (IDS), helping to protect against a wide range of cyber threats.

1. Signature-based Patterns: These rules match known malware signatures, which are unique strings of data or characteristics of known malicious code.
2. Anomaly-based Patterns: These rules detect deviations from normal behavior or baseline patterns within a system. Any significant deviation could indicate a security threat.
3. Heuristic-based Patterns: These rules use algorithms to identify suspicious behavior that may not match any known signatures but resembles known malicious activities.
4. Policy-based Patterns: These rules enforce security policies and detect violations, such as unauthorized access attempts or changes to critical system files.
5. Behavior-based Patterns: These rules monitor for specific actions that could indicate a threat, such as repeated failed login attempts or unusual data transmissions.
6. Sandboxing Patterns: In sandboxing, detection rules observe the behavior of software in a controlled environment to determine if it’s benign or malicious.

### How to create custom detection rules?

Creating custom detection rules in cybersecurity involves defining specific criteria that, when met, will trigger an alert or response.

We need to identify the behavior first. Determine the specific behavior or pattern we want to monitor. This could be unusual network traffic, repeated login failures, or unexpected system changes. And then, define the rule. Use a query language like KQL (Kibana Query Language) or a similar tool to define the rule. The rule should clearly state the conditions that will trigger an alert.

After the rule has been defined, set up the rule with configuring the rule with the necessary details, such as the frequency of checks, alert thresholds, and any response actions. Before fully implementing the rule, test it to ensure it accurately detects the behavior without generating too many false positives.

Once tested, implement the rule in our security system and monitor its performance over time. Cyber threats evolve, so it’s important to regularly review and update our detection rules to maintain their effectiveness: update as needed.

As references, there are more detailed guidance from Microsoft Defender XDR (https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules) or Elastic Security Solution (https://www.elastic.co/guide/en/security/current/rules-ui-create.html) to study from.

### While making the rules, how to avoid the false positives within?

Avoiding false positives in cybersecurity detection rules is crucial for maintaining the efficiency and effectiveness of our security operations.

First, fine-tune rules; adjust the sensitivity of our detection rules to better match the normal behavior of our network and systems. Also use multiple sources, cross-reference alerts from multiple security tools to confirm the legitimacy of a threat. Keep our security tools and threat definitions up-to-date to ensure they can accurately identify new threats with regular updating.

Analyze the patterns; look for patterns in false positives to understand why they are occurring and adjust our rules accordingly. Establish proceduces; create clear procedures for handling alerts, including steps for verifying and responding to potential threats. Do continuous monitoring, regularly review and monitor the performance of our detection rules to catch any issues early.

In team, it's also important to always train ourselves to recognize false positives and understand the importance of accurate threat detection. By implementing these strategies, we can minimize the number of false positives and focus on genuine threats, thereby improving the overall security posture of our organization.

### Sensitivity vs. Specificity

Balancing sensitivity and specificity in cybersecurity detection rules is essential to ensure that our system effectively detects threats without generating excessive false positives. By carefully managing these aspects, we can create a more effective and efficient detection system that minimizes false positives while still catching genuine threats.

1. Understand the Trade-offs: Sensitivity refers to the ability of a rule to correctly identify true threats (true positives), while specificity refers to its ability to correctly identify non-threats (true negatives). Increasing sensitivity may lead to more false positives, and increasing specificity may lead to more false negatives.
2. Use a Baseline: Establish a baseline of normal behavior for our network or system. This will help us set thresholds that distinguish between normal and suspicious activities.
3. Implement Machine Learning: Utilize machine learning algorithms that can learn from data and improve over time, adjusting the balance between sensitivity and specificity based on feedback.
4. Regularly Update Rules: Cyber threats evolve, so it’s important to update our detection rules regularly to maintain their effectiveness.
5. Test and Validate: Continuously test our rules against known datasets to validate their accuracy and adjust them as needed.
6. Feedback Loop: Create a feedback loop where the security team reviews alerts and provides input on the accuracy of the detection rules, allowing for continuous improvement.

# Group Policy Implementation

Group policy implementation in cybersecurity blueteaming involves a set of strategies and actions taken by the Blue Team to protect an organization’s computer systems and networks from cyber threats. By implementing these measures, the Blue Team helps organizations maintain the confidentiality, integrity, and availability of their critical assets against cyber threats.

1. Identifying and Mitigating Vulnerabilities: The Blue Team conducts regular security assessments to identify potential vulnerabilities within the organization’s IT infrastructure. They then work to mitigate these vulnerabilities by implementing appropriate security controls.
2. Implementing Security Controls: Security controls are measures put in place to prevent unauthorized access and protect against network-based attacks. These can include firewalls, intrusion detection and prevention systems, anti-malware software, and endpoint security.
3. Monitoring and Responding to Incidents: Blue Team members continuously monitor network traffic and system configurations to detect any unusual activity that may indicate a security breach. Upon detection of an incident, they respond swiftly to isolate affected systems, analyze the nature of the attack, and implement measures to prevent further damage.
4. Incident Response Plans: An incident response plan is a predefined set of instructions or procedures to detect, respond to, and recover from network security incidents. The Blue Team ensures that these plans are up-to-date and effective in mitigating potential threats.
5. Employee Training and Awareness: Educating staff on best practices for cybersecurity is crucial. The Blue Team often conducts training sessions to raise awareness about potential cyber threats and how employees can contribute to the organization’s cybersecurity efforts.
6. Regular Updates and Patch Management: Keeping operating systems and software up-to-date with the latest patches is essential for preventing exploitation by malware. The Blue Team ensures that regular updates are applied promptly.

### About security controls...

Common security controls in cybersecurity are measures put in place to protect systems and data from cyber threats. These controls are part of a layered defense strategy to ensure comprehensive protection against a wide range of cyber threats.

1. Authentication Solutions: Verify the identity of users before granting access to systems.
2. Firewalls: Monitor and control incoming and outgoing network traffic based on predetermined security rules.
3. Antivirus Software: Protect against malware by detecting, preventing, and removing malicious software.
4. Intrusion Detection Systems (IDSs): Monitor network traffic for suspicious activity and known threats.
5. Intrusion Prevention Systems (IPSs): Actively block potential threats detected by the IDS.
6. Constrained Interfaces: Limit the ways in which users can interact with systems to reduce the risk of unauthorized actions.
7. Access Control Lists (ACLs): Define who or what is allowed to access certain resources within a network.
8. Encryption Measures: Secure data by converting it into a code to prevent unauthorized access.

Implementing encryption and firewall in security control group policy is a critical aspect of cybersecurity. By implementing these security controls through group policy, we can maintain a consistent security posture across all managed devices within an organization. It’s important to regularly review and update these policies to adapt to new threats and changes in the organization’s infrastructure.

### About encryption...

We can use BitLocker to encrypt drives on Windows devices. We can configure BitLocker through Group Policy Objects (GPOs) for devices joined to an Active Directory domain. This ensures that data at rest is protected against unauthorized access.

And then, Encrypting File System (EFS). EFS can be controlled using GPOs to manage encryption of files and folders on NTFS volumes.

### About firewall...

We can use Windows Firewall with Advanced Security to configure firewall rules using GPOs to manage inbound and outbound network traffic. This includes creating rules for specific ports, protocols, and IP addresses. 

Also setting the firewall state to ‘On’ for all network profiles (Domain, Private, Public) to ensure that the firewall is active and protecting the network.

### About intrusion detection and prevention systems (IDS/IPS)...

Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS) are critical components of network security. IDS' purpose is to monitor network traffic for surpicious activity and known threats. It uses various methods like signature-based detection, anomaly detection, and heuristics to identify potential threats. Upon detecting a threat, an IDS typically sends an alert to the network administrator but does not take action to stop the threat.

While IPS' purpose is similar to an IDS but with the added capability of taking action to prevent or block threats in real-time. It also uses signature-based detection, anomaly detection, and heuristics. However, when it detects malicious activity, it can automatically block the offending traffic or connection. The IPS can drop packets, reroute traffic to a quarantine area, or take other predefined actions to mitigate the threat.

Both systems are essential for a robust cybersecurity strategy, with IDS providing monitoring and alerting capabilities, and IPS offering active prevention measures. They often work together to provide comprehensive protection against cyber threats.

### Provide an example - of a group policy implementation!

This example will illustrate how group policies can be used as part of a comprehensive cybersecurity strategy to protect an organization’s assets and data.

#### Scenario

A company has recently experienced a phishing attack that compromised several employee accounts. The Blue Team is tasked with implementing a group policy to prevent such incidents in the future.

#### Implementation Steps

1. Policy Development: The Blue Team develops a new group policy that requires all employees to use multi-factor authentication (MFA) for accessing company resources.
2. Policy Testing: Before rolling out the policy company-wide, the Blue Team tests it in a controlled environment to ensure it doesn’t interfere with normal business operations.
3. Policy Deployment: Once tested, the policy is deployed across the organization using the company’s Group Policy Management Console (GPMC).
4. Training and Communication: The Blue Team conducts training sessions to educate employees about the new policy and its importance in preventing unauthorized access.
5. Monitoring and Enforcement: The Blue Team monitors compliance with the new policy and enforces it by restricting access for users who do not comply.
6. Incident Response Plan Update: The incident response plan is updated to include procedures for responding to potential MFA bypass attempts.
7. Regular Review and Update: The Blue Team regularly reviews the policy’s effectiveness and updates it as necessary to adapt to new threats or changes in the organization’s structure.
