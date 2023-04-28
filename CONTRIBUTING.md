# TODO APP REST API using Flask

## Run the app locally using Docker

1. Build a docker container using the dockerfile provided in the root of the project folder using the command:
`docker build -t <IMAGE_NAME> .`

2. Run the container in a volume using the command:
`docker run -dp 5000:5000 -w /app -v "$(pwd):/app" <IMAGE_NAME> sh -c "flask run --host 0.0.0.0"`

3. Once the image is running, use the postman file provided in link below to interact with the API:
[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/20771641-78558435-933a-4a76-8496-6f5ef6bcce76?action=collection%2Ffork&collection-url=entityId%3D20771641-78558435-933a-4a76-8496-6f5ef6bcce76%26entityType%3Dcollection%26workspaceId%3Df7d0cbbf-27b3-4af2-b821-347154ded30d)

## Follow the steps below to use the app:

1. First register the user by using the '/register' endpoint in the 'User' collection and provide appropriate username and password
2. Then login with the same credentials using the '/login' endpoint
3. Once authenticated, copy the access_token which will be required when a particular task has to performed on the todo list
4. Can proceed to create tasks and their statuses using various endpoints provided in the 'todos' collection and add header as 'key'='Authorization' and 'value'='Bearer <access_token>' 