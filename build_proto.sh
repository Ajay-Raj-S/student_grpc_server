#!/bin/bash
python3.8 -m grpc_tools.protoc \
	--proto_path=. \
	--python_out=. \
	--grpc_python_out=. \
	get_students.proto
