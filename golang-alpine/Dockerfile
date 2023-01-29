#
# docker build --tag [TAG] .
# docker run --rm -p 9000:8080 [TAG]
#
# Vulnerability scan recommended (https://aquasecurity.github.io/trivy/):
#  trivy image [TAG]
#
# Local test with cURL:
# curl \
#    -X POST \
#    -H 'Content-Type: application/json' \
#    -d @_events/apigateway-proxy.json \
#    'http://localhost:9000/2015-03-31/functions/function/invocations'
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
COPY --from=go-app-builder /usr/bin/aws-lambda-rie /usr/bin/aws-lambda-rie

COPY lambda-entrypoint.sh /lambda-entrypoint.sh

RUN chmod +x /usr/bin/aws-lambda-rie \
    && chmod +x /lambda-entrypoint.sh \
    && ln -s "${LAMBDA_TASK_ROOT}/go-app" /go-app


ENTRYPOINT ["/lambda-entrypoint.sh"]

CMD ["/go-app"]
