# Project Overview Chart

![TEEP-Progress(2)](https://hackmd.io/_uploads/BJFxIt4tC.png)

In this guide one of the challange is that :

1. O-RAN srsCU-srsDU customization 7.2x split option still not on the container format form to run
2. srsRU-Emu still not tested and integrated with srsDU and srsUE
3. Clocking Sync Integration with Linux PTP
4. Separated workspace due to limited computing resource

> Notes:
> 1. On srsRAN on Kubernetes Docs: showed that RU is not Emulation, CU & DU is not yet validated an O-RAN customized solution  

Also this playground directory provides an overview of the directory structure for the srsRAN Project including CU, DU, gNB, and UE components.

```plaintext
.
├── README.md
├── srs-cu
│   ├── Chart.yaml
│   ├── README.md
│   ├── docker-cu
│   │   ├── Dockerfile
│   │   └── cu.yaml
│   ├── templates
│   │   ├── configmap.yaml
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── values.yaml
├── srs-du
│   ├── Chart.yaml
│   ├── README.md
│   ├── docker-du
│   │   ├── Dockerfile
│   │   └── du.yaml
│   ├── templates
│   │   ├── configmap.yaml
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── values.yaml
├── srs-gnb
│   ├── Chart.yaml
│   ├── README.md
│   ├── charts
│   │   └── common
│   │       ├── Chart.yaml
│   │       ├── README.md
│   │       ├── templates
│   │       │   ├── _affinities.tpl
│   │       │   ├── _capabilities.tpl
│   │       │   ├── _errors.tpl
│   │       │   ├── _images.tpl
│   │       │   ├── _ingress.tpl
│   │       │   ├── _labels.tpl
│   │       │   ├── _names.tpl
│   │       │   ├── _secrets.tpl
│   │       │   ├── _storage.tpl
│   │       │   ├── _tplvalues.tpl
│   │       │   ├── _utils.tpl
│   │       │   ├── _warnings.tpl
│   │       │   └── validations
│   │       │       ├── _cassandra.tpl
│   │       │       ├── _mariadb.tpl
│   │       │       ├── _mongodb.tpl
│   │       │       ├── _mysql.tpl
│   │       │       ├── _postgresql.tpl
│   │       │       ├── _redis.tpl
│   │       │       └── _validations.tpl
│   │       └── values.yaml
│   ├── templates
│   │   ├── configmap-entrypoint.yaml
│   │   ├── configmap.yaml
│   │   ├── deployment.yaml
│   │   └── hpa.yaml
│   └── values.yaml
└── srs-ue
    ├── Chart.yaml
    ├── README.md
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

## Summary

- **README.md**: General information about the project.
- **srs-cu**: Contains the Helm chart for the CU (Central Unit) including Dockerfile, YAML configurations, and templates.
- **srs-du**: Contains the Helm chart for the DU (Distributed Unit) including Dockerfile, YAML configurations, and templates.
- **srs-gnb**: Contains the Helm chart for the gNB (gNodeB) including common dependencies and templates.
- **srs-ue**: Contains the Helm chart for the UE (User Equipment) including common dependencies and templates.