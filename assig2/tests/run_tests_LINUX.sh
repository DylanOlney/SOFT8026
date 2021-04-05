#! /bin/sh
sudo echo "Running Postman test suite in Newman (from Docker Image)!"
echo "Please wait..."
sudo docker run --net=host -v  "$(pwd)"/postman:/etc/newman -t postman/newman run collection.json 
echo "Tests complete!"
./helper/continue.o












