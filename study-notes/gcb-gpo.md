# Global Central Bank

#### This one really needs to be rechecked... and approved.

In the context of blueteaming, GCB stands for Global Central Bank, which is an Enterprise Windows and Active Directory Cyber Range and in the context of cybersecurity typically refers to a central bank that operates on a global scale, dealing with the financial stability and security of the global financial system. It’s designed to help enterprises test the capabilities of both their Red and Blue teams within an Enterprise Windows network. GCB provides a multi-forest environment that mimics a financial institution’s network, allowing teams to practice current and futuristic threats, test lateral movement, and analyze adversary attack methodologies using logs.

# Group Policy Object

![image](https://github.com/bmw-ece-ntust/internship/assets/138283247/e65a2661-b5bc-477f-96e8-f69d9c34b7d2)

GPO, on the other hand, typically refers to Group Policy Object in the context of Windows environments. It’s a feature of Microsoft Windows that provides centralized management and configuration of operating systems, applications, and users’ settings in an Active Directory environment. In blueteaming, GPOs can be used to simulate security policies and configurations that a Blue team would need to defend against or a Red team would need to exploit.

### Common GPO Security Best Practices

It is important to test any changes on a small group of users and computers before rolling them out across your entire network. Each Active Directory environment is unique, so tailor these practices to fit your specific needs.

1. Enable Audit Logs: Monitor activity on your network by enabling audit logs. At a minimum, enable Audit System Events.
2. Screen Lockout Time: Set a lock-out time from inactivity on domain computers to protect data and privacy.
3. Password Policy: Enforce a strong password policy to secure your domain. This includes setting password complexity requirements and expiration policies.
4. Account Lockout Policy: Implement an account lockout policy to prevent brute force attacks by locking accounts after a certain number of failed login attempts.
5. Removable Media: Restrict or disable the use of removable media to prevent the introduction of malware into the network.
6. Command Prompt and PowerShell Access: Limit access to the command prompt and PowerShell to prevent unauthorized commands from being run.
7. Do Not Modify Default Domain Policy: Avoid modifying the Default Domain Policy for settings other than account policy, password policy, account lockout policy, and Kerberos policy.
8. Good Organizational Unit (OU) Design: Create a clear OU structure for easier application and troubleshooting of GPOs.
9. Apply GPOs at the Root OU: Apply GPOs at the root of an OU to allow sub-OUs to inherit these policies, simplifying management.
10. GPO Security Filtering: Use GPO security filtering to apply policies only to specific users or groups within an OU.

### Secure The Active Directory!

![image](https://github.com/bmw-ece-ntust/internship/assets/138283247/05504f72-4dea-421b-94fb-06e9707b513b)

Securing an AD environment is an ongoing process that requires constant vigilance and adaptation to new security challenges. It is crucial for protecting your organization’s data and resources.

1. Enforce Least Privilege: Ensure that users have only the permissions they need to perform their jobs.
2. Monitor for Suspicious Activity: Use monitoring tools to keep an eye on AD for any unusual activity that could indicate a security breach.
3. Regularly Update and Patch: Keep all systems up-to-date with the latest security patches and updates.
4. Implement Strong Password Policies: Enforce complex passwords and regular password changes to prevent unauthorized access.
5. Secure Administrative Accounts: Use multi-factor authentication and limit access to administrative accounts.
6. Use Group Policy Objects (GPOs) Wisely: Configure GPOs to enforce security settings across your network.
7. Backup Regularly: Regularly back up your AD environment to recover from potential data loss or corruption.
8. Educate Users: Train users on security best practices and the importance of following them.
9. Limit Access to Domain Controllers: Restrict physical and network access to domain controllers to prevent unauthorized changes.
10. Audit and Review Security Settings: Periodically audit your AD security settings and review them for any potential vulnerabilities.

Note: For more informations, please refer to https://nics.nat.gov.tw/GCB.htm?lang=zh when it's available.
