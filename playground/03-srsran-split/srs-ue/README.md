
# srs-ue Helm Chart

## Overview

The `srs-ue` Helm chart deploys a User Equipment (UE) component in the srsRAN system. It is built using Kubernetes and Helm, and allows for scalable, flexible deployment of the UE in a cloud-native environment.

## Chart Structure

Here is the structure of the `srs-ue` Helm chart:

```
srs-ue/
├── Chart.yaml
├── charts
│   └── common
│       ├── Chart.yaml
│       ├── README.md
│       ├── templates
│       │   ├── _affinities.tpl
│       │   ├── _capabilities.tpl
│       │   ├── _errors.tpl
│       │   ├── _images.tpl
│       │   ├── _ingress.tpl
│       │   ├── _labels.tpl
│       │   ├── _names.tpl
│       │   ├── _secrets.tpl
│       │   ├── _storage.tpl
│       │   ├── _tplvalues.tpl
│       │   ├── _utils.tpl
│       │   ├── _warnings.tpl
│       │   └── validations
│       │       ├── _cassandra.tpl
│       │       ├── _mariadb.tpl
│       │       ├── _mongodb.tpl
│       │       ├── _mysql.tpl
│       │       ├── _postgresql.tpl
│       │       ├── _redis.tpl
│       │       └── _validations.tpl
│       └── values.yaml
├── templates
│   ├── configmap-ue.yaml
│   ├── deployment.yaml
│   ├── hpa.yaml
│   └── service-gtpu.yaml
└── values.yaml
```

## Files and Directories

- **Chart.yaml**: Contains metadata about the Helm chart.
- **charts/common**: Common templates and configurations used across multiple Helm charts. This directory contains reusable templates like `_affinities.tpl`, `_capabilities.tpl`, and others, that are shared among different components of the srsRAN system.
- **templates/**: Contains Kubernetes manifests and configuration files for deploying the UE component.
  - **configmap-ue.yaml**: ConfigMap for UE-specific configuration.
  - **deployment.yaml**: Deployment configuration for the UE.
  - **hpa.yaml**: Horizontal Pod Autoscaler (HPA) configuration.
  - **service-gtpu.yaml**: Service definition for GTP-U interface.
- **values.yaml**: Default values for the Helm chart.

## Deployment Instructions

1. **Install Helm**: Ensure Helm is installed on your system.

   ```bash
   curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
   ```

2. **Deploy the Chart**: Navigate to the directory containing the `srs-ue` Helm chart and run:

   ```bash
   helm install srs-ue ./srs-ue
   ```

   This will deploy the UE component using the default values in `values.yaml`.

3. **Verify Deployment**: Check that the pods are running:

   ```bash
   kubectl get pods
   ```

## Customization

- **Override Default Values**: You can override the default values in `values.yaml` by providing your own `values.yaml` file:

   ```bash
   helm install srs-ue ./srs-ue -f my-values.yaml
   ```

- **Scale the Deployment**: To scale the UE deployment, you can modify the `replicaCount` value in `values.yaml` or use the HPA configuration.

   ```bash
   kubectl scale deployment srs-ue --replicas=<number-of-replicas>
   ```

## Notes

- Ensure that the Kubernetes cluster is properly configured to support the srsRAN UE component.
- The `service-gtpu.yaml` is configured to expose the GTP-U interface which is essential for UE operation.