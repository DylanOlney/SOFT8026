#! /bin/sh
sudo echo "Running Postman test suite in Newman (from Docker Image)!"
echo "Please wait..."
sudo docker run --net=host -v  "$(pwd)"/tests:/etc/newman -t postman/newman run collection.json 
echo "Tests complete!"
./continue.o












