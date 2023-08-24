import yaml
from django.conf import settings

def generate_yaml_file(UUID, filename, endpoint):
   template = '''apiVersion: v1
kind: Pod
metadata:
  name: vpp-app-{UUID}
  labels:
    app: vpp-app-{UUID}
spec:
  volumes:
  - name: credentials
    configMap:
      name: miniocredentials
  containers:
  - name: vpp-app-{UUID}
    image: docker.io/mrdojojo/video-processor-ffmpeg:1.2
    env:
    - name: ENDPOINT_URL
      value: "http://{endpoint}/"
    - name: SRC_OBJECT_KEY
      value: "{filename}"
    - name: SRC_S3_BUCKET
      value: "{SRC_BUCKET}"
    - name: SRC_S3_REGION
      value: ""
    - name: DST_S3_REGION
      value: ""
    - name: DST_S3_BUCKET
      value: "{DST_BUCKET}"
    resources:
      limits:
        cpu: "30"
      requests:
        cpu: "15"
    volumeMounts:
    - name: credentials
      readOnly: true
      mountPath: "/home/altrauser/.aws/credentials"
      subPath: credentials
  restartPolicy: OnFailure
   '''

   yaml_content = template.replace("{UUID}", UUID).replace("{filename}", filename).replace("{endpoint}", endpoint).replace("{SRC_BUCKET}", settings.MINIO_SRC_BUCKET_NAME).replace("{DST_BUCKET}", settings.MINIO_DST_BUCKET_NAME)

   filename = f"videoplayer/job.yaml"

   with open(filename, "w") as yaml_file:
       yaml_file.write(yaml_content)

   print(f"YAML file '{filename}' has been generated.")
   return yaml_content
