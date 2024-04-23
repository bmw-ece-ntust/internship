# **GNS-3 Installation Guide on VMWare Workstation**

## GNS3 Setup with GMS3 VM

1. [Download GMS3 VM](https://www.gns3.com/software/download-vm) for VMWare Workstation from GNS3's website.
![images](/images/gns3/1.png)

2. [Download GMS3 for Windows](https://www.gns3.com/software/download).
![images](/images/gns3/2.png)

3. Extract the GMS3 VM for VMWare.

4. Open the .ovf file in VMWare Workstation and import the GNS3 VM without altering its name.
![images](/images/gns3/3.png)

5. Ensure that in the VM settings > Processors > Virtualization engine, "Virtualize Intel VT-x/EPT or AMD-V/RVI" is enabled.
![images](/images/gns3/4.png)

6. Run the GNS3 VM.
7. On the displayed page, confirm that "KVM support available" is set to true, and no errors are shown.
![images](/images/gns3/5.png)


8.  Install GMS3 for Windows, proceeding without modifying any settings.
![images](/images/gns3/6.png)

9.  Complete the installation process by clicking "Next" consecutively.

10.  After installation, launch GNS3. If a Setup Wizard appears, choose "Run appliances in a virtual machine."
![images](/images/gns3/7.png)
![images](/images/gns3/8.png)

11.  Select VMWare as the virtualization software, ensuring the VM name matches the .ovf file from earlier steps (usually 'GNS3 VM' by default). Customize vCPU cores and RAM size as desired.
![images](/images/gns3/9.png)
![images](/images/gns3/10.png)


12.  Review the summary and click "Finish" to complete the setup.
![images](/images/gns3/11.png)


## Installing Aruba CX in GNS3 through VMWare:

1. Visit the [GNS3 marketplace website](https://www.gns3.com/marketplace/featured), navigate to appliances, search for Aruba, and select "ArubaOS-CX Simulation Software" to download.
![images](/images/gns3/13.png)
![images](/images/gns3/14.png)


2. Visit the [Aruba website](https://networkingsupport.hpe.com/downloads)'s Software and Documents section, filter software for Aruba switches, and ensure the file format is .ova. Download the ArubaOS-CX file.
![images](/images/gns3/15.png)


3. Extract the ArubaOS-CX.ova file using [7zip](https://www.7-zip.org/), resulting in two files: .ovf and .vmdk

    ![images](/images/gns3/16.png)


4. Return to GMS3 in Windows, click "File" > "Import appliance," and select the file downloaded from the marketplace.
![images](/images/gns3/17.png)


5. Choose the necessary files for installation, ensuring their status is "Ready to Install," and proceed by clicking "Next."
![images](/images/gns3/18.png)
![images](/images/gns3/19.png)
![images](/images/gns3/20.png)


6. If completed successfully, the new PoE switch will appear on the screen when clicking the browse templates button. To utilize the switch, drag it from the switches section onto the workspace.
![images](/images/gns3/21.png)
