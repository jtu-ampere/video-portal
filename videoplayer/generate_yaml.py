import yaml

def generate_yaml_file(UUID, filename):
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
  - name: vpp-app1
    image: docker.io/mrdojojo/video-processor-ffmpeg:1.2
    env:
    - name: ENDPOINT_URL
      value: "http://console.minio.mk8snode4.hhii.ampere/"
    - name: SRC_OBJECT_KEY
      value: "{filename}"
    - name: SRC_S3_BUCKET
      value: "vod-poc"
    - name: SRC_S3_REGION
      value: ""
    - name: DST_S3_REGION
      value: ""
    - name: DST_S3_BUCKET
      value: "vpp-dst"
    resources:
      limits:
        cpu: "60"
      requests:
        cpu: "16"
    volumeMounts:
    - name: credentials
      readOnly: true
      mountPath: "/home/altrauser/.aws/credentials"
      subPath: credentials
  restartPolicy: OnFailure
   '''

   yaml_content = template.replace("{UUID}", UUID).replace("{filename}", filename)
   filename = f"processvideoapp/job.yaml"

   with open(filename, "w") as yaml_file:
       yaml_file.write(yaml_content)

   print(f"YAML file '{filename}' has been generated.")
   return yaml_content