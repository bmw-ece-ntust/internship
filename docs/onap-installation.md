## Deployment

### 1. Download the IT/dep repository from gerrit

```bash=
mkdir workspace && cd workspace
git clone --recurse-submodules https://gerrit.o-ran-sc.org/r/it/dep.git
```

### 2. Setup Helm Charts
- Execute the following commands being logged as root.
```bash=
##Setup ChartMuseum
./dep/smo-install/scripts/layer-0/0-setup-charts-museum.sh

##Setup HELM3
./dep/smo-install/scripts/layer-0/0-setup-helm3.sh

## Build ONAP/ORAN charts
./dep/smo-install/scripts/layer-1/1-build-all-charts.sh
```

### 3. Deploy components
- Execute the following commands ==being logged as root==:
```bash=
./dep/smo-install/scripts/layer-2/2-install-oran.sh
```
