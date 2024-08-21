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

### Docker volume

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
### Docker restart
```
docker restart container-name
```

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

> [!NOTE]
> #### Remember, when using bind mounts, ensure the paths on the host exist and have the correct permissions.

---- 
### Docker attach

Docker attach is a command used to connect to a running container, allowing you to interact with it as if you were directly connected to its standard input, output, and error streams. However, docker attach is not typically used for modifying files or reflecting changes like in my Flask app. Instead, it’s often used for debugging or interacting with the process running inside the container.
```
docker attach myapp4
```
Once attached, you’ll see the output from the container’s process in your terminal, and you can interact with it.

##### Limitations of docker attach
  1. Single Process: docker attach connects to the main process in the container. If that process is not interactive (e.g., it’s running a web server), attaching might not be particularly useful.
  2. Input and Output: It does not provide a shell environment. If the container’s main process is not interactive, you might not be able to interact meaningfully.
  3. Multiple Attachments: If multiple clients are attached to the same container, they all share the same standard input and output streams. This can lead to confusion if not managed properly.

##### Detach from the Container

To detach from the container without stopping it, use the detach sequence:

For Docker's default terminal: Press **Ctrl + P** followed by **Ctrl + Q**
This will detach your terminal from the container while keeping the container running.

##### Alternatives for Interactive Debugging
For most use cases, especially if you want to modify files or check the environment inside the container, you might prefer the following alternatives:

1. docker exec
2. Using Bind Mounts for Development
3. Logs and Monitoring `docker logs myapp4`

----
### Docker exec
```
docker exec -it container-name bash
docker exec -it container-name sh
docker exec -it container-name ls -ll /homee
docker exec -it container-name sh -c ping google.com
docker exec -it container-name apt update
```
#### If you want to login inside your running container then use docker exec command

----
### Docker cp
If you want to copy a file or folder inside a docker container from localhost use below command

```
docker cp file1.txt conatiner-name:/ur-destination
docker cp -r /folder container-name/ur-destination
```
If you want to copy a file or folder from a docker container to localhost use below command
```
docker cp conatiner-name:file1.tx /ur-destination-on-localhost
docker cp container-name/folder ur-destination-on-localhost
```
Example of docker cp
```
docker myapp4:/usr/src/app/templates ./          # this is will create a folder name templates
docker cp myapp4:/usr/src/app/templates ./akki   # this is will create a folder name akki
docker cp myapp4:/usr/src/app/templates/hello.html ./ 
```

----
### Docker create

The docker create command is used to create a new container from a Docker image, but unlike docker run, it does not start the container immediately. Instead, it creates the container and provides its ID, allowing you to start it later using docker start.

```
docker create --name mynginx -p 8080:80 nginx
```
<img width="1670" alt="image" src="https://github.com/user-attachments/assets/58322b15-2c8f-4159-871d-1c692651f4d4">

----
### Docker start

The docker start command is used to start a stopped Docker container that was previously created or stopped. It’s commonly used after you’ve created a container with docker create or stopped a running container and want to restart it.
```
docker start container-name
```
----
### Docker stop
The docker stop command is used to stop a running Docker container. It sends a SIGTERM signal to the main process inside the container, which gives it a chance to gracefully shut down. If the process does not stop within a specified timeout period, docker stop will send a SIGKILL signal to forcefully terminate the process.

Stop Multiple Containers
```
docker stop container1 container2 container3
```
Specify Timeout

By default, Docker will wait 10 seconds for the container to stop gracefully before sending a SIGKILL. You can change this timeout period by using the -t option followed by the number of seconds you want Docker to wait:
```
docker stop **-t 20** mynginx
```
In the above example, Docker will wait 20 seconds for the container to stop gracefully before forcefully terminating it.

> [!TIP]
> **Graceful Shutdown:** Containers should handle the SIGTERM signal gracefully and perform any necessary cleanup before exiting.
> **Forceful Stop:** If a container does not stop gracefully within the timeout period, Docker will forcefully terminate it with SIGKILL.

----
### Docker kill 

The docker kill command is used to immediately terminate a running Docker container by sending a SIGKILL signal to its main process. This is a more forceful way of stopping container compared to docker stop, which first tries to stop the container gracefully by sending a SIGTERM signal and waits for a specified timeout before sending SIGKILL.

```
docker kill container-name
```
----
### Docker pause
The docker pause command is used to pause all processes within a running Docker container by sending a SIGSTOP signal. This effectively suspends the container’s execution, putting its processes into a paused state without terminating them. This can be useful for temporarily halting the container’s operations without stopping or killing it, allowing you to resume later.

```
docker pause container-name
```
> [!TIP]
> **Paused State:** When a container is paused, all processes inside it are frozen. The container’s state remains, but it does not perform any actions or consume CPU resources.
>
> **Use Cases:** Pausing a container can be useful for troubleshooting, performing maintenance, or temporarily suspending processes without losing their state.
> 
> **Resource Management:** Although paused containers do not consume CPU resources, they still occupy memory and disk space. Consider this when managing system resources.

> [!IMPORTANT]
> **Debugging**: If you need to investigate or debug a container’s state without stopping its execution, pausing it can help.
> 
> **Maintenance:** For performing system maintenance or configuration changes without stopping the container and potentially disrupting ongoing operations.
> 
> **Testing:** In testing scenarios where you need to temporarily halt the container’s processes and then resume them.

----
### Docker unpause 

The docker unpause command is used to resume a Docker container that has been previously paused using docker pause. When you pause a container, Docker sends a SIGSTOP signal to all processes in the container, effectively freezing them. The docker unpause command sends a SIGCONT signal to resume these processes, allowing the container to continue its operations where it left off.
```
docker unpause container-name
```
> [!TIP]
> **Pausing and Unpausing:** Pausing a container is a way to freeze its operations without stopping it. Unpausing resumes operations. This can be useful for temporarily halting activities for maintenance or debugging.
> 
> **Resource Management:** Paused containers do not use CPU resources but still occupy memory and disk space. Unpausing will resume their CPU and memory usage.
> 
> **Process Continuity:** When a container is unpaused, it continues from the exact state it was in when it was paused, including its internal processes and open files.
----
### Docker events
Docker events is a command used to monitor real-time events from the Docker daemon. This command is particularly useful for tracking the activities and status changes of Docker containers, images, volumes, and networks. You can use it to see events such as container start, stop, or other changes in real time.

In the below image you can see I have executed some command then events happened are available in the second image


<img width="384" alt="image" src="https://github.com/user-attachments/assets/60d80fcd-3d75-4b01-be44-1fcdd2e3227a">

<img width="1728" alt="image" src="https://github.com/user-attachments/assets/350a030c-30d4-4948-8ab5-55265a08b0b6">

##### Filtering Events
We can filter events by various criteria using options such as:

Event Type: You can filter for specific event types like create, start, stop, destroy, etc.

```
docker events --filter event=start
docker events --filter container=<container_id>
docker events --filter type=container|image|network|volume
```

##### Example Scenarios
1. Monitor Container Lifecycle Events
  ```
  docker events --filter event=start --filter event=stop --filter event=restart
  ```
2. Debugging Issues
3. Tracking Image Changes
  ```
    docker events --filter event=pull --filter event=delete
  ```  
4. Volume and Network Events 
 ```
    docker events --filter type=volume
    docker events --filter type=network
  ```  





#### The details inside of the docker container are below 

<img width="1521" alt="image" src="https://github.com/user-attachments/assets/8fe86c1d-9504-4099-872b-06da4330f1fa">


