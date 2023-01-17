#
# docker build --tag [TAG] .
# docker run --rm -it -p 9000:8080 [TAG]
#
# Vulnerability scan recommended (https://aquasecurity.github.io/trivy/):
#  trivy image [TAG]
#
# Local test with cURL:
# curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"type":"event","data":{"key":"value"}}'
#

FROM alpine:3.17 AS go-app-builder

ENV LAMBDA_TASK_ROOT /var/task
ENV LAMBDA_RUNTIME_DIR /var/runtime


WORKDIR "${LAMBDA_TASK_ROOT}"

RUN apk add --no-cache \
        curl \
        go \
    && curl -Lo /usr/bin/aws-lambda-rie https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie \
    && chmod +x /usr/bin/aws-lambda-rie

COPY src/ "${LAMBDA_TASK_ROOT}"

RUN go mod tidy \
    && go build -o go-app


# == New Stage ==


FROM alpine:3.17

ENV LAMBDA_TASK_ROOT /var/task
ENV LAMBDA_RUNTIME_DIR /var/runtime


WORKDIR "${LAMBDA_TASK_ROOT}"

COPY --from=go-app-builder "${LAMBDA_TASK_ROOT}/go-app" "${LAMBDA_TASK_ROOT}/go-app"
COPY --from=go-app-builder --chmod=0755 /usr/bin/aws-lambda-rie /usr/bin/aws-lambda-rie

COPY --chmod=0755 lambda-entrypoint.sh /lambda-entrypoint.sh

RUN ln -s "${LAMBDA_TASK_ROOT}/go-app" /go-app


ENTRYPOINT ["/lambda-entrypoint.sh"]

CMD ["/go-app"]
