
# srs-du Helm Chart

This Helm chart deploys the `srs-du` (Distributed Unit) component of the srsRAN project into a Kubernetes cluster.

## Prerequisites

Before deploying the Helm chart, ensure you have the following:

- A Kubernetes cluster up and running
- `kubectl` configured to interact with your cluster
- Helm installed on your local machine

## Chart Structure

The Helm chart is organized as follows:

```
srs-du/
├── charts/
├── templates/
│   ├── configmap.yaml        # ConfigMap for DU configuration
│   ├── deployment.yaml       # Kubernetes Deployment for srs-du
│   ├── service.yaml          # Kubernetes Service to expose srs-du
│   ├── _helpers.tpl          # Helper template file for reusable templates
│   └── NOTES.txt             # Additional notes displayed after installation
├── Chart.yaml                # Chart metadata
└── values.yaml               # Default values for the chart
```

### Key Files and Directories

- **`charts/`**: Holds any dependent charts. (Empty in this case)
- **`templates/`**: Contains Kubernetes manifests that are processed by Helm to deploy your application.
  - **`deployment.yaml`**: Defines the Deployment resource for deploying the `srs-du` application.
  - **`service.yaml`**: Defines the Service resource for exposing the `srs-du` application.
  - **`configmap.yaml`**: Contains the configuration for the `srs-du` application, injected as a ConfigMap.
  - **`_helpers.tpl`**: Provides helper template functions.
  - **`NOTES.txt`**: Contains user notes and instructions displayed after chart installation.
- **`Chart.yaml`**: Contains the metadata for the Helm chart, such as its name, version, and description.
- **`values.yaml`**: Contains the default values for the Helm chart. You can override these values when installing the chart.

## Deploying the Helm Chart

### Step 1: Customize the Configuration

Edit the `values.yaml` file to customize the deployment. The default values should work for a basic deployment, but you may want to adjust parameters like `replicaCount`, `image.repository`, `image.tag`, and `service.port`.

If you have a custom `du.yml` configuration file, modify the `configmap.yaml` template or use an external ConfigMap by adjusting the `duConfigMap` value in `values.yaml`.

### Step 2: Package the Helm Chart (Optional)

If you want to package the Helm chart for distribution, run the following command in the directory containing the `Chart.yaml`:

```bash
helm package srs-du
```

This command will create a `srs-du-0.1.0.tgz` package file.

### Step 3: Install the Helm Chart

To deploy the chart to your Kubernetes cluster, run:

```bash
helm install my-srs-du ./srs-du
```

Replace `my-srs-du` with the desired release name. The chart will deploy the `srs-du` application using the provided or default configuration.

### Step 4: Verify the Deployment

After the chart is deployed, you can check the status of the deployment using:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

These commands will list the status of your Deployment, Pods, and Services in the cluster.

### Step 5: Access the `srs-du` Service

If you have exposed the `srs-du` service via a LoadBalancer or NodePort, you can access it using the external IP or port provided by the service.

### Step 6: Uninstall the Helm Chart

To uninstall the chart and remove the associated resources from your Kubernetes cluster, run:

```bash
helm uninstall my-srs-du
```

Replace `my-srs-du` with the release name you used during installation.

## Conclusion

This Helm chart makes it easy to deploy and manage the `srs-du` component of the srsRAN project in a Kubernetes environment. By leveraging Helm, you can scale, update, and maintain your deployment with ease.