# Istio

- Dowload istio
```
curl -L https://istio.io/downloadIstio | sh -
```

```
export PATH=$PWD/istio-11.2/bin:$PATH
```

- Install Istio on cluster
```
istioctl install --set profile=demo -y
```