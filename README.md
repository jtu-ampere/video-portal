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
kubectl apply -f deploy_django.yaml -n poc1 
```

# The folders matching phases:

### [Folder: myapp](https://github.com/liangliang1120/vod_portal/tree/main/myapp)
- PoC1-Design a container using Django and PostgreSQL
### [Folder: processapp](https://github.com/liangliang1120/vod_portal/tree/main/processapp)
- Poc2-Call Kubernetes API in Django
### [Folder: uploadvideo](https://github.com/liangliang1120/vod_portal/tree/main/uploadvideo)
- PoC3-A HTML form for uploading file to Object storage
### [Folder: processvideoapp](https://github.com/liangliang1120/vod_portal/tree/main/processvideoapp)
- PoC4-Triggering Video Processing
### [Folder: videoplayer](https://github.com/liangliang1120/vod_portal/tree/main/videoplayer)
- PoC5-A Video Portal for listing all processed videos with thumbnail and preview animated GIF
- Final demo: Integrate all PoCs into a Video Portal
### [Folder: uploadpod](https://github.com/liangliang1120/vod_portal/tree/main/uploadpod)
- PoC6-Upload MinIO file to Kubernetes Pod in Django
