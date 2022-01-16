---
title: K8s on GCP(GKE)
tags: Kubernetes
lang: en-us
---

{%hackmd theme-dark %}

# Step
1. ![](https://i.imgur.com/PmFklHA.png)
2. ![](https://i.imgur.com/woh4CeF.png)
3. ![](https://i.imgur.com/pqvCvZo.png)
4. ![](https://i.imgur.com/UT679Fn.png)

# Basic
## K8s 介紹
- 用於自動部署、擴充和管理`容器化（containerized）`應用程式的開源系統。
- 由 Google 設計並捐贈給 Cloud Native Computing Foundation（今屬Linux基金會）來使用。
- 旨在提供`跨主機叢集(Cluster)`的`自動部署`、`擴充`以及執行應用程式容器的`平台`。
- 可以做到：
    - 同時部署多個容器到多台機器上（Deployment）。
    - 服務的乘載量有變化時，可以對容器做自動擴展（Scaling）。
    - 管理多個容器的狀態，自動偵測並重啟故障的容器（Management）。

## K8s 架構
### 主要架構
![](https://i.imgur.com/477ffKi.png)
- Clusters(叢集)：
    - 由 masters 和 nodes 組成。
- Master：
    - 大總管，可做為主節點。
- Node：
    - 主要工作的節點，上面運行了許多容器。
    - 可想作一台虛擬機。
    - K8S 可操控高達 1,000 個 nodes 以上。

### 細部架構
![](https://i.imgur.com/eXHZwQj.png)


## Reference
- [GKE 教學系列 (一)](https://ikala.cloud/kubernetes-gke-introduction/)
- [K8s Wiki](https://zh.wikipedia.org/wiki/Kubernetes)
- [Kubernetes 基礎教學（一）原理介紹](https://cwhu.medium.com/kubernetes-basic-concept-tutorial-e033e3504ec0)