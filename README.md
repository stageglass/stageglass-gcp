# stageglass-gcp
Stageglass backedn deployed to GCP

This is the initial deployed code for the backend.  I'm not including all the gcp cli steps required for full deployment (but I can add that later if required).

There is a python venv with all the required dependencies; you can activate it with `venv\Scripts\activate`

## python files
- central_server.py: this is the actual running backend.  
- datastore.py: an abstraction layer over the gcp datastore. enforces shaped data using proto files.
- create_link_code_record.py: calls into gcp to make a new datastore object.
- central_client.py: (for testing) makes a test request to either a local or remote grpc server.
- mock_builder.py: (for testing) creates mock datastore objects.
- fetch_link_code_record.py: (for testing) calls into gcp to get a datastore object
- send_request.py: (for testing) hits a remote endpoint

## codegen python files
Anything with `_pb2` in the name is a codegen file created from the .proto files.

Here is codegen command:
```
python -m grpc_tools.protoc --include_imports --include_source_info --proto_path=. --descriptor_set_out=api_descriptor.pb --python_out=. --grpc_python_out=. common.proto central.proto
```

## proto files
These define the service api and the shaped data.
- central.proto: defines the service
- common.proto: defines the shaped data
