# vod_backend_poc1

### deploy Django method 1:
Inside of this folder, run `docker-compose up` or `podman-compose up`


### deploy Django method 2:
```
docker run -d -p 8000:8000 -v $(pwd):/code gulianglily/vod_backend_poc1-app:latest python3 manage.py runserver 0.0.0.0:8000
```

### deploy Django method 3:
For Kubernetes:
```
kubectl apply -f deploy_django.yaml -n poc3
```

### deploy Video Portal
For Kubernetes:
Update the parameters for MinIO, and the ones like Host IP, port and credential for postgresql

```
kubectl apply -f video-portal-deployment.yaml -n video-portal 
```
