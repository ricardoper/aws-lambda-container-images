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

FROM alpine:3.17 AS aws-builder

ENV LAMBDA_TASK_ROOT /var/task
ENV LAMBDA_RUNTIME_DIR /var/runtime
ENV PATH="${PATH}:${LAMBDA_RUNTIME_DIR}/bin"


RUN apk add --no-cache \
        autoconf \
        automake \
        cmake \
        curl \
        curl-dev \
        g++ \
        git \
        libtool \
        make \
        python3-dev \
        py3-pip \
    && curl -Lo /usr/bin/aws-lambda-rie https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie \
    && chmod +x /usr/bin/aws-lambda-rie

COPY aws-runtime/ "${LAMBDA_RUNTIME_DIR}"
COPY src/ "${LAMBDA_TASK_ROOT}"

# libexecinfo-dev depency for awslambdaric
RUN git clone https://github.com/mikroskeem/libexecinfo.git /tmp/libexecinfo \
    && cd /tmp/libexecinfo \
    && make install PREFIX=/usr

RUN chmod +x "${LAMBDA_RUNTIME_DIR}/bootstrap" \
    \
    && pip3 install --no-cache-dir --upgrade -r "${LAMBDA_RUNTIME_DIR}/requirements.txt" --target "${LAMBDA_RUNTIME_DIR}" \
    && pip3 install --no-cache-dir --upgrade -r "${LAMBDA_TASK_ROOT}/requirements.txt" --target "${LAMBDA_RUNTIME_DIR}"


# == New Stage ==


FROM alpine:3.17

ENV LAMBDA_TASK_ROOT /var/task
ENV LAMBDA_RUNTIME_DIR /var/runtime
ENV PATH="${PATH}:${LAMBDA_RUNTIME_DIR}/bin"


RUN apk add --no-cache \
        curl \
        python3

COPY --from=aws-builder "${LAMBDA_RUNTIME_DIR}" "${LAMBDA_RUNTIME_DIR}"
COPY --from=aws-builder "${LAMBDA_TASK_ROOT}" "${LAMBDA_TASK_ROOT}"
COPY --from=aws-builder /usr/bin/aws-lambda-rie /usr/bin/aws-lambda-rie

COPY lambda-entrypoint.sh /lambda-entrypoint.sh

RUN chmod +x /usr/bin/aws-lambda-rie \
    && chmod +x /lambda-entrypoint.sh


ENTRYPOINT ["/lambda-entrypoint.sh"]

CMD ["lambda_function.lambda_handler"]
