FROM public.ecr.aws/lambda/python:3.9


COPY src/ "${LAMBDA_TASK_ROOT}"

RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"


CMD ["lambda_function.lambda_handler"]
