# Video Portal for Video Processing Pipeline PoC demo 





### deploy Video Portal
For Kubernetes:
Update the parameters for MinIO, and the ones like Host IP, port and credential for postgresql

```
kubectl apply -f video-portal-deployment.yaml -n video-portal 
```
