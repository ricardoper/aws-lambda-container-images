FROM public.ecr.aws/lambda/go:1 as build

COPY src/ ./

RUN yum install -y golang \
    && go env -w GOPROXY=direct \
    && go mod tidy \
    && go build -o /main


FROM public.ecr.aws/lambda/go:1

COPY --from=build /main "${LAMBDA_TASK_ROOT}"


CMD ["main"]
