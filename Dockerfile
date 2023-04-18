FROM python:3.10-slim

WORKDIR /srv/grpc

COPY *.py *.proto requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt && \
    python -m grpc_tools.protoc \
        -I. \
        --python_out=. \
        --grpc_python_out=. \
        common.proto central.proto

CMD ["python", "central_server.py"]