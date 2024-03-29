# **EVE-NG Installation Guide on VMWare Workstation**

- [**EVE-NG Installation Guide on VMWare Workstation**](#eve-ng-installation-guide-on-vmware-workstation)
  - [VMWare Workstation Setup](#vmware-workstation-setup)
  - [EVE-NG CLI](#eve-ng-cli)
  - [Open EVE-NG in Browser](#open-eve-ng-in-browser)
  - [WinSCP Installation](#winscp-installation)
  - [Lab Creation on EVE-NG](#lab-creation-on-eve-ng)


##  VMWare Workstation Setup
1. Download the Community Edition of EVE-NG. Use the MEGA/Google links Full ISO.
   
    ![image](/images/Eve/1.png)

2. Create a New Virtual machine, click on **File > New Virtual Machine** choose **Custom (Advanced**) click Next. 

    ![image](/images/Eve/2.png)

3. Choose the default Virtual machine hardware compatibility and click Next.

    ![image](/images/Eve/33.png)

4. Select "l will install the operating system later" and click Next.

    ![image](/images/Eve/3.png)

5. Select a Guest Operating system: Linux and select the version: Ubuntu 64-bit

    ![image](/images/Eve/4.png)

6. Enter the name for your EVE-COMM VM and select Location where your EVE VM will be stored on the host PC and click Next.

    ![image](/images/Eve/5.png)

7. Select max Number of processors, and Number of cores per processor = 1

    ![image](/images/Eve/6.png)

8. Assign desirable memory for your EVE VM and click Next.

    ![image](/images/Eve/7.png)

9. Select then network for your EVE VM. For Laptop it is recommended to use NAT Adaptor

    ![image](/images/Eve/8.png)

10. Leave recommended 1/0 settings, LSI Logic and click Next.

    ![image](/images/Eve/9.png)

11. Leave recommended Disk Type (SCSI) settings and click Next.
    
    ![image](/images/Eve/10.png)

12. Select Create a new virtual disk and click Next.

    ![image](/images/Eve/34.png)

13. Select your desirable disk size. It is recommended to set minimum 20GB or more. Select Store virtual disk as single file or split into multiple sizes and click Next.

    ![image](/images/Eve/11.png)

14. Specify Disk File location click Next.

15. Select Customize Hardware
    ![image](/images/Eve/12.png)


    IMPORTANT! Select CPU and Enable **Virtualize Intel VT-x/EPT** option
    ![image](/images/Eve/13.png)

16. Select CD/DVD Option: "Use ISO image file." Browse to your downloaded eve-ce-prod-5.O.1-22-full.iso (actual name can be different) file.

    ![image](/images/Eve/14.png)

17. Click Finish to complete VM setup and power on the virtual machine.

    ![image](/images/Eve/15.png)

18. Chose Install EVE-NG Community Server and confirm with Enter. 

    ![image](/images/Eve/16.png)

19. Select English language and make sure if English US keyboard is selected and confirm with Enter

    ![image](/images/Eve/17.png)

20. If your DHCP IP settings are correct, select Done and confirm with Enter.

    ![image](/images/Eve/18.png)

21. If you have proxy in use for your internet, assign your network proxy settings. If no proxy in use,
with Tab ke select Continue and confirm with Enter.

    ![image](/images/Eve/19.png)

22. Select "Continue" and confirm with Enter.

    ![image](/images/Eve/20.png)

23. After the Ubuntu "Install Complete" select "Reboot Now" and hit Enter to continue.
    
    ![image](/images/Eve/21.png)

24. Without powering off the EVE VM, open the EVE VM settings, remove CD/DVD ISO Device, and tick the device status on 'Connected.' Save VM Settings.

    ![image](/images/Eve/22.png)

25. Return back to EVE console screen and confirm Continue with Enter, EVE VM will reboot and continue installation

    ![image](/images/Eve/23.png)

26. Depending on your internet speed EVE installation will take some time. After installation EVE VM will auto reboot and EVE login screen will appear, login in CLI with root/eve

    ![image](/images/Eve/24.png)

## EVE-NG CLI
27. After your EVE is rebooted, Login to EVE CLI

    ![image](/images/Eve/25.png)

28. Type in a new password.
    
    ![image](/images/Eve/26.png)

29. Type the hostname (default is eve-ng). Press enter to select hostname.

    ![image](/images/Eve/27.png)

30. Type the domain name (default is example.com)

    ![image](/images/Eve/28.png)

31. Select if management IP address should be static or configured by DHCP (default is DHCP, use arrow keys and space to select, then enter to confirm): Static IP address will ask for IP address, netmask, default gateway, primary and secondary DNS servers.

    ![image](/images/Eve/29.png)

32. Type or leave blank if not used (default is blank):
Type the NTP server

    ![image](/images/Eve/30.png)

33. Configure how the EVE VM can access Internet (default is direct connection, use arrow keys and space to select then enter to confirm :

    ![image](/images/Eve/31.png)

34. After the last confirm EVE will reboot. Once you see the login prompt, the system is successfully configured.

## Open EVE-NG in Browser
35. EVE-NG is now ready. Open a browser and enter the IP address of the VM in the address bar then click go or press enter. The following page will load. 

    Default Sign in credentials:

    Username : admin

    Password : eve

    ![image](/images/Eve/32.png)

## WinSCP Installation

1. Download the [supported OS image](https://www.eve-ng.net/index.php/documentation/supported-images/) of your device based on the EVE-NG documentation. Example: for Aruba 2540 24G PoE+ 4SFP+ (JL356A) switch, the OS is supported (Aruba CX Switch).
   
    ![image](/images/Eve/35.png)

2. Download the latest version of WinSCP from [this website](https://winscp.net/eng/download.php)
    ![image](/images/Eve/46.png)

3. In the login page, select 'SFTP' for the file protocol and port number 22. As for the hostname, enter the website address given in the EVE-NG CLI. For username is root and the password is eve.
    ![image](/images/Eve/40.png)

4. There will be two different windows, in the right window, direct from /root to / < root >

    ![image](/images/Eve/41.png)

5. From there, direct to /opt/unetlab/addons/qemu
    ![image](/images/Eve/42.png)

6. On the left side of the window, search the downloaded OS image for the hardware, then drag and drop the folder to the qemu folder.
    ![image](/images/Eve/43.png)
    
## Lab Creation on EVE-NG

1. Create new lab on the browser dashboard

    ![image](/images/Eve/36.png)

3. Complete the lab details, only the lab name is mandatory.

    ![image](/images/Eve/37.png)

4. After the lab is opened, to add the OS image to the lab, select 'Add an object' and select 'Node'.

    ![image](/images/Eve/38.png)

5. If the image is already inserted correctly in the WinSCP, the OS name will appear blue, select that image.

    ![image](/images/Eve/39.png)

6. Select the image of the specified OS (in this case: arubacx-10.04), then add prefix and icon for the hardware.

    ![image](/images/Eve/44.png)

7. The result will look like below

    ![image](/images/Eve/45.png)
