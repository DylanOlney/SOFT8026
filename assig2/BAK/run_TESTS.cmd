@echo off
echo "Running Postman test suite in Newman (from Docker Image)!"
echo "Please wait..."
docker run --net=host -v  "%~dp0/tests":/etc/newman -t postman/newman run collection.json 
echo "Tests complete!"
pause












