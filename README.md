# Flask appliction to render colorful HTML pages and to upload files flask-backgroud-color-upload-file
This is a flask application which have a background color for the rendered HTML page. The color are defined in the app.py file and a random from `[red, green, blue, blue2, pink and darkblue]` or based on the environment variable passed while executing the docker container.


There is one more feature in this application you can upload file and can store inside your container. To access this feature hit the `http://<public-ip-of-vm>:8080/upload-title` URL.

Inside app.py I have defined a varaible named `UPLOAD_FOLDER` which holds the value for the folder name where we want to store the file inside container. The value of `UPLOAD_FOLDER` is hardcoded to `/rahees-uploaded-files` inside app.py this folder will be created inside the container. If you want to pass any other path to store the files you can pass it using environment variable.

----
Commands to run the application inside a docker container

`docker run docker run -d -p 8080:8080 rahees9983/simple-webapp-color:v1` 

To pass the color value using environemt variable use the below docker command 

``docker run -d -p 8080:8080 -e APP_COLOR=green rahees9983/simple-webapp-color:v1``

To access the application via browser hit the below URL
htpp://<PUBLIC-IP-ADDRESS>:8080

http://3.141.165.177:8080/

If your VM is on a AWS then add below Security Group

<img width="1679" alt="image" src="https://github.com/user-attachments/assets/cbe27871-302d-4281-9d41-89b289c7213c">


Application accessibility image


<img width="1248" alt="image" src="https://github.com/user-attachments/assets/7d7abdd2-5c23-4c09-8d18-8267006e9efa">


`$ docker run --name my-flask-app -e UPLOAD_FOLDER="/usr/src/app/upload" -e APP_COLOR="green" -p 8080:8080 flask-upload-file:v2`

Upload file URL 

`http://PUBLIC-IP-OF-VM:8080/upload-title`


http://18.224.0.43:8080/upload-title


<img width="1728" alt="image" src="https://github.com/user-attachments/assets/106e9715-b2f6-4bbe-9d3e-6d4b52edb5de">

#### If my container get removed my data in my case my uploaded file will be lost to persist the uploaded file we have to use docker volumes

Volumes are a Docker-managed storage mechanism. They are stored in a part of the host filesystem which is managed by Docker (/var/lib/docker/volumes/ on Linux) and are designed to persist data beyond the lifecycle of individual containers.

##### Creating a Volume

You can create a volume using the docker volume create command:

```
docker volume create my_volume
```
###### Using a Volume

To use the volume with a container, you can mount it using the -v or --mount option:

```
docker run -d -v my_volume:/path/in/container my_image
```
or
```
docker run -d --mount source=my_volume,target=/path/in/container my_image
```
2. Bind Mounts
Bind mounts allow you to mount a specific path from your host into the container. This is useful for development or when you need to access files from a specific location on your host machine.

Using a Bind Mount

To use a bind mount, specify the path on the host and the path inside the container:

```
docker run -d -v /path/on/host:/path/in/container my_image
```

###### Choosing Between Volumes and Bind Mounts
Volumes are managed by Docker, so they are portable and better suited for production environments.
Bind Mounts are more flexible and allow you to access files from your host directly, which is useful for development and debugging.
### Example Use Case

###### If you are running a database container, you might want to persist the database data across container restarts. You could use a volume:

```
docker run -d -v db_data:/var/lib/mysql mysql
```
##### For a web application where you want to map source code changes from your host to the container, you could use a bind mount:

```
docker run -d -v /path/to/your/code:/usr/src/app my_web_image
```
This way, any changes you make to the code on your host will be reflected inside the container immediately.

---- 
#### Example of my application using docker volume

```
docker run -d --name myapp -p 8080:8080 -v rahees_volume:/env-upload-floder -e UPLOAD_FOLDER="/env-upload-floder" flask-upload-file:v2
```
```
docker volume ls
docker volume inspect rahees_volume
ls -ll /var/lib/docker/volumes/rahees_volume/_data
```

<img width="1728" alt="image" src="https://github.com/user-attachments/assets/ef218e41-400b-44d5-a1e4-a2668b020100">


#### Managing Volumes
###### To list volumes:

```
docker volume ls
```
##### To inspect a volume:

```
docker volume inspect rahees_volume
```
###### To remove a volume:

```
docker volume rm rahees_volume
```
----
#### If you want make any change to your application, to reflect those changes on the application you have to restart your container then only your changes will be reflected else there would be no chages in the applicaion though you have made the required changes.

Lets say you want to change the maessage on inside the hello.html page then follow the below steps

Current state of the application is available in the below image

<img width="1173" alt="image" src="https://github.com/user-attachments/assets/688a25a2-7e0a-42ea-a55e-f618ff7df355">

I have followed below steps to make the changes inside the continer
1. exec into the container
2. Installed the vim editor inside my container
3. Edited the /templates/hello.html file
4. docker restart myapp
5. Accesed my application using http://PUBLIC_IP:8080

Post making the changes inside the application new look is available in the below image


<img width="1375" alt="image" src="https://github.com/user-attachments/assets/c9e1f506-2845-40fb-81c2-e28b758da3c9">


### NOTE:- Remember, when using bind mounts, ensure the paths on the host exist and have the correct permissions.

---- 
#### The details inside of the docker container are below 

<img width="1521" alt="image" src="https://github.com/user-attachments/assets/8fe86c1d-9504-4099-872b-06da4330f1fa">
