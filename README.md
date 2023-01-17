# Cleaner & Smaller AWS Lambda Container Images

Some base container images and examples to apply in AWS Lambdas.

Because AWS has some bloated images, you can find in this repository some images as clean and small as possible. This way we have faster load times, cold starts, and we reduce the attack surface.


## Golang Container Images

AWS Lambda Golang 1.18  >  832MB<br>
(based on Amazon Linux v2)

Alpine Lambda **Golang 1.19**  >  **22MB**<br>
(based on Alpine Linux 3.17)

**NOTE**:
- The Alpine image has the same functionalities of the AWS image.

### Build & Run container images

```
cd ./golang-alpine

DOCKER_BUILDKIT=1 docker build --tag [TAG] .
docker run --rm -it -p 9000:8080 [TAG]
```

BuildKit required: https://docs.docker.com/build/buildkit/

### Vulnerability scan

Vulnerability scan is recommended. [Trivy](https://aquasecurity.github.io/trivy/) is used to scan these images.
```
trivy image [TAG]
```

### Container local testing

With cURL:
```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"type":"event","data":{"key":"value"}}'
```

### Lambda Start times

```
LAMBDA   |  60KB |  * 0.475s  0.247s  0.242s  0.225s  0.238s  * 0.468s  0.262s  0.160s

DOCKER
  AWS    | 832MB |  * 1.053s  0.258s  0.434  0.259s  * 1.368s  0.283s  0.267s
  ALPINE |  22MB |  * 1.474s  0.254s  0.416  0.247s  * 0.832s  0.242s  0.179s

* Cold Start
```


## Python Container Images

AWS Lambda Python 3.9  >  595MB<br>
(based on Amazon Linux v2)

Alpine Lambda **Python 3.10**  >  **140MB**<br>
(based on Alpine Linux 3.16)

**NOTE**:
- The Alpine image has the same functionalities of the AWS image.
- The AWS image has a lot of unnecessary packages, like Python 2.7.

### Build & Run container images

```
cd ./python-alpine

DOCKER_BUILDKIT=1 docker build --tag [TAG] .
docker run --rm -it -p 9000:8080 [TAG]
```

BuildKit required: https://docs.docker.com/build/buildkit/

### Vulnerability scan

Vulnerability scan is recommended. [Trivy](https://aquasecurity.github.io/trivy/) is used to scan these images.
```
trivy image [TAG]
```

### Container local testing

With cURL:
```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"type":"event","data":{"key":"value"}}'
```

### Lambda Start times

```
LAMBDA   |  60KB |  * 0.475s  0.247s  0.242s  0.225s  0.238s  * 0.468s  0.262s  0.160s

DOCKER
  AWS    | 595MB |  * 1.054s  0.181s  0.218s  0.238s  * 1.025s  0.266s  0.258s
  ALPINE | 140MB |  * 0.876s  0.264s  0.273s  0.178s  * 0.843s  0.293s  0.192s

* Cold Start
```
