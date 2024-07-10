# Non-RT RIC Installation

## Prerequisites

### Java
### Maven
### Lens
1. Get the Lens Desktop public security key and add it to your keyring:
    ```
    curl -fsSL https://downloads.k8slens.dev/keys/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/lens-archive-keyring.gpg > /dev/null
    ```
2. Add the Lens Desktop repo to your /etc/apt/sources.list.d directory.
    ```
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/lens-archive-keyring.gpg] https://downloads.k8slens.dev/apt/debian stable main" | sudo tee /etc/apt/sources.list.d/lens.list > /dev/null
    ```
3. Install Lens Desktop
    ```
    sudo apt update && sudo apt install lens
    ```
4. Run lens desktop  (You will be asked to create an account first)
    ```sh
    # Do it in linux desktop screen, otherwise it will produce screen not found error
    lens-desktop
    ```

### microk8s
1. Install microk8s
    ```
    snap install microk8s --classic
    ```
2. Get config settings
    ```
    microk8s config
    ```
3. Import config to lens
    via config -> clusters -> add from kubeconfig
4. Completion screen

### Install docker and docker-compose

## Non-RT RIC Installation
Do it as root, `sudo su` first and `cd ~`.
### Source Code download cloning
1. Download the parent source code
    ```
    git clone --recurse-submodules https://gerrit.o-ran-sc.org/r/it/dep.git
    ```
2. Next download for the H release for the nonrtric
    ```
    git clone --recurse-submodules -b h-release https://gerrit.o-ran-sc.org/r/nonrtric.git
    ```
3. Replace the nonrtric from the first step with the new one from the second step
   ```
   cp -r nonrtric dep
   ```










