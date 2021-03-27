#! /bin/sh
python3 -m grpc_tools.protoc  -I./ --python_out=./grpc-server --grpc_python_out=./grpc-server streamer.proto
python3 -m grpc_tools.protoc  -I./ --python_out=./grpc-client --grpc_python_out=./grpc-client streamer.proto
sudo docker-compose build


