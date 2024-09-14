# Flask appliction to render colorful HTML pages and to upload files flask-backgroud-color-upload-file
This is a flask application which have a background color for the rendered HTML page. The color are defined in the app.py file and a random from `[red, green, blue, blue2, pink and darkblue]` or based on the environment variable passed while executing the docker container.


There is one more feature in this application you can upload file and can store inside your container. To access this feature hit the `http://<public-ip-of-vm>:8080/upload-title` URL.

Inside app.py I have defined a varaible named `UPLOAD_FOLDER` which holds the value for the folder name where we want to store the file inside container. The value of `UPLOAD_FOLDER` is hardcoded to `/rahees-uploaded-files` inside app.py this folder will be created inside the container. If you want to pass any other path to store the files you can pass it using environment variable.

Execute below command to activate python environment 
source /home/ubuntu/my-venv/bin/activate

Execute below command for unit test execution 
(my-venv) root@ip-172-31-34-134:/home/ubuntu/flask-html-backgroud-color-change/run-in-docker# python -m pytest -v unit-test-for-app.py 

Execute below command for static code analysis using pylint
(my-venv) root@ip-172-31-34-134:/home/ubuntu/flask-html-backgroud-color-change/run-in-docker# python -m pylint -v app.py 



----
### Docker build
The docker build command is used to create a Docker image from a Dockerfile. 
```
docker build -t image-name:tag .
docker build -f Dockerfile.dev -t myapp:dev .
docker build -f Dockerfile.prod -t myapp:prod .
docker build --build-arg MY_VAR=value -t myapp:1.0 .
docker build --no-cache -t myapp:1.0 .
```
Above commands explanation
```
-f Dockerfile.dev: Specifies the Dockerfile to use for the build.

-t myapp:dev: Tags the image as myapp with the tag dev.

.: Uses the current directory as the build context.
```

#### <span style="color: green;">Additional Options and Flags</span>
> [!NOTE]
> **-t, --tag:** Tags the image with a name and optionally a tag in the format name:tag.
> 
> **-f, --file:** Specifies a different Dockerfile name or path (default is Dockerfile).
>
> **--build-arg:** Passes build-time arguments to the Dockerfile.
>
> **--no-cache:** Ignores cache when building the image.
>
> **--rm:** Removes intermediate containers after a successful build (default behavior).
>
> **--target:** Builds a specific stage from a multi-stage Dockerfile.

----
### Docker login
The docker login command is used to authenticate with a Docker registry. This allows you to pull images from or push images to a private Docker registry, such as Docker Hub, or a custom registry.

Basic Usage of docker login
1. Login to Docker Hub
```
docker login
```
2. Login to a Custom Docker Registry
3. Use --password-stdin for Secure Login  
To securely provide your password from stdin, use:
```
echo "mypassword" | docker login myregistry.example.com -u myusername --password-stdin
echo "Rahees-ka-pass" | docker login docker.io/rahees9983 -u rahees9983 --password-stdin
```
This method avoids exposing your password in the command line history.

<img width="906" alt="image" src="https://github.com/user-attachments/assets/514bff14-879e-480d-b2f9-5f01a3edb667">

##### Managing Credentials
Docker stores login credentials in a configuration file located at ~/.docker/config.json. This file contains authentication tokens and is used for subsequent login sessions. The file may look like:
```
{
  "auths": {
    "https://index.docker.io/v1/": {
      "auth": "dXNlcjpwYXNzd29yZA=="
    },
    "myregistry.example.com": {
      "auth": "dXNlcjpwYXNzd29yZA=="
    }
  }
}
```
#### Common Use Cases
**Push and Pull Images:** Authenticate to push images to or pull images from a private Docker registry or Docker Hub.

**Automation:** Use docker login in scripts and CI/CD pipelines to automate deployments and image management.

**Access Control:** Ensure that only authenticated users can access private images and repositories.

----
### Docker tag
The docker tag command is used to create a new tag for an existing Docker image. Tags are useful for organizing and managing images, allowing you to refer to images by a name and version (or other identifiers) rather than by their image ID.

Basic Usage of docker tag
1. Basic Syntax
The general syntax for tagging an image is:
```
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
```
SOURCE_IMAGE[:TAG]: The existing image you want to tag. If no TAG is specified, the latest tag is used by default.
TARGET_IMAGE[:TAG]: The new tag you want to assign to the image.
2. Tag and push an Image
```
docker tag myimage:latest mynewimage:v1.0
docker images | grep hello-world
docker tag hello-world:latest rahees9983/hello-world:v1.1
docker images | grep hello-world
docker login
docker push rahees9983/hello-world:v1.1
```
<img width="1727" alt="image" src="https://github.com/user-attachments/assets/c9998d46-999d-42cb-a75c-b3aece63c060">

<img width="1728" alt="image" src="https://github.com/user-attachments/assets/c6cf971c-1e84-4277-82ad-a4581164a2f8">

----
### Docker save
The docker save command is used to export Docker images to a tarball file, which can then be shared or archived. This is particularly useful for moving Docker images between environments or backing up images.

Basic Usage of docker save
1. Syntax
The basic syntax for the docker save command is:
```
docker save -o <output_file> <image_name>[:tag]
```
#### -o <output_file>: Specifies the file path where the tarball will be saved.
#### <image_name>[:tag]: The name (and optionally the tag) of the Docker image you want to save. If no tag is provided, Docker defaults to the latest tag.
##### Example Commands
1. Save a Single Image
To save a Docker image named myimage with the tag latest to a file named myimage.tar:
```
docker save -o myimage.tar myimage:latest
```
2. Save Multiple Images
To save multiple images into a single tarball file:
```
docker save -o all_images.tar myimage:latest anotherimage:latest
```
#### Common Use Cases
**Backup Docker Images:** Create backups of important Docker images to ensure they can be restored if needed.

**Transfer Images:** Share Docker images between systems or environments by exporting them to a tarball file and transferring the file.

**Archival:** Archive Docker images for long-term storage or compliance purposes.

<img width="958" alt="image" src="https://github.com/user-attachments/assets/a94e15a2-6878-4b37-8542-cb6a05ba3b89">

----
### Docker load
The docker load command is used to import Docker images from a tarball file, which was previously exported using docker save. This command is useful for restoring Docker images, transferring images between environments, or setting up Docker images on a new system.

Basic Usage of docker load
1. Syntax
The basic syntax for the docker load command is:
```
docker load -i <input_file>
```
-i <input_file>: Specifies the file path of the tarball that contains the Docker image you want to load.

To load the Docker image from hello-world.tar:
```
docker load -i hello-world.tar
```
<img width="1090" alt="image" src="https://github.com/user-attachments/assets/a556712c-1d77-45c4-8e25-180f1dc0e9cb">

----
### Docker export and import
The docker export command is used to create a tarball of a Docker container's filesystem. This command is useful for exporting the state of a container's file system to a file, which can then be transferred or archived. Unlike docker save, which exports Docker images, docker export deals specifically with the container's filesystem at a point in time.

Basic Usage of docker export
1. Syntax
The basic syntax for the docker export command is:
```
docker export [OPTIONS] CONTAINER_ID_or_NAME > <output_file>
```
CONTAINER_ID_or_NAME: The ID or name of the running or stopped container you want to export.
> <output_file>: Redirects the output to a file. Alternatively, you can use the -o option to specify the output file directly.

2. Example Commands
Export a Container to a Tarball

To export a container with the ID myapp to a tarball file named container-export.tar:
```
docker export myapp > container-export.tar
or use -o
docker export myapp -o container-export.tar
```
Extract and Inspect the Tarball

You can extract and inspect the contents of the tarball using:
```
tar -tf container-export.tar
```
##### Common Use Cases
**Backup Container Filesystem:** Create backups of the container’s filesystem to preserve its state or configuration.

**Transfer Container State:** Share the container's filesystem with others by exporting it to a tarball file.

**Archive:** Archive the container’s state for compliance or long-term storage purposes.

##### Difference Between docker export and docker save
**docker export:** Exports the filesystem of a container. It does not include metadata or image history and is specific to the container’s current state.

**docker save:** Exports the image and its layers, including metadata and history, but not the state of any specific container.

<img width="1425" alt="image" src="https://github.com/user-attachments/assets/c5e8498c-cd31-4130-82ad-134e2c482635">

----
### Docker commit
The docker commit command is used to create a new image from an existing container. This is useful for capturing changes made to a container's filesystem after it has been started from an image. You can think of docker commit as a way to "snapshot" a container's state and turn it into a reusable Docker image.

Basic Usage of docker commit
1. Syntax
The basic syntax for the docker commit command is:
```
docker commit [OPTIONS] CONTAINER_ID_or_NAME [REPOSITORY[:TAG]]
```
2. Example Commands
Create a New Image from a Container
```
docker commit abc123 mynewimage:v1
docker commit -m "Added new feature" abc123 mynewimage:v1
docker commit -a "Rahees Khan <john.doe@example.com>" abc123 mynewimage:v1
```
##### Common Use Cases
**Save Changes:** Capture changes made to a container's filesystem after it has been started.

**Create Custom Images:** Build custom Docker images that include updates or modifications specific to your use case.

**Reproduce Environments:** Save the state of a container to reproduce the environment or configuration across different systems or teams.

<img width="1475" alt="image" src="https://github.com/user-attachments/assets/f1f9d908-a27b-4c3e-8933-7b9354fdc1bc">

----
### Docker rmi
The docker rmi command is used to remove Docker images from your local Docker environment. This command is helpful for cleaning up unused images, freeing up disk space, and managing your image repository.

1. Remove a Single Image
```
docker rmi <image_name_or_id>
```
2. Remove Multiple Images
```
docker rmi myimage:latest myimage:old
```
4. Remove All Unused Images
```
docker image prune
```
5. This command will prompt you for confirmation before deleting the unused images. To bypass the confirmation prompt, use:
```
docker image prune -f
```
6. Remove all unused images, not just dangling ones, with:
```
docker image prune -a
```
<img width="1019" alt="image" src="https://github.com/user-attachments/assets/31b363d6-eab5-4ae1-991d-04201fb192a7">

----
### Docker run
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

----
### Docker logs
Commands to check the logs inside the docker container

```
docker logs container-name
docker logs my-flask-app
```
To see the live logs of the container use -f parameter
```
docker logs -f my-flask-app
```
----
### Docker volume

#### If my container get removed my data in my case my uploaded file will be lost to persist the uploaded file we have to use docker volumes

Volumes are a Docker-managed storage mechanism. They are stored in a part of the host filesystem which is managed by Docker (/var/lib/docker/volumes/ on Linux) and are designed to persist data beyond the lifecycle of individual containers.

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
The docker rm command is used to remove one or more Docker containers. This command is useful for cleaning up containers that are no longer needed or for freeing up system resources. Containers need to be stopped before they can be removed.

#### Basic Usage of docker rm
```
docker rm <container_name_or_id>
docker rm mycontainer
```
1. Remove Multiple Containers
```
docker rm container1 container2 container3
```
2. Remove All Stopped Containers
```
docker container prune
```
3. The above command will prompt you for confirmation before deleting all stopped containers. To bypass the confirmation prompt, use:
```
docker container prune -f
```
4. Alternatively, you can use the following command to remove all stopped containers directly:
```
docker rm $(docker ps -a -q -f status=exited)
```
##### Additional Options and Flags
**-f, --force:** Forces the removal of a running container by first stopping it.
**-v, --volumes: **Removes the volumes associated with the container.

```
docker rm -v mycontainer
```
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
### Docker port
The docker port command is used to display the public-facing ports for a specific container. It shows how ports on the container are mapped to ports on the host machine. This command is useful for understanding the port mappings for a running container and diagnosing network-related issues.

```
docker port container
```
<img width="1632" alt="image" src="https://github.com/user-attachments/assets/2d54b98e-effb-47f5-bda8-7e51940eb5ec">

### <span style="color: green;">Common Use Cases.</span>
> [!TIP]
> **Debugging:** Verifying that the container’s ports are mapped correctly to the host ports, especially when troubleshooting connectivity issues.
>
> **Configuration:** Ensuring that the correct ports are exposed and mapped for containers running services that need to be accessed from outside the host.
>
> **Testing:** Checking port mappings to ensure that services running inside containers are accessible at the expected ports on the host machine.

----
### Docker rename
The docker rename command is used to change the name of an existing Docker container. This can be useful for organizing and managing containers, especially in environments with many containers or when a more descriptive name is needed for clarity.

```
docker rename old_name new_name
docker rename myapp1 my-new-app1
````
#### Additional Tips
> [!TIP]
> **Container Names:** Each container must have a unique name within a Docker host. If you attempt to rename a container to a name that is already in use, Docker will return an error.
> 
> **Container IDs:** You can also use the container ID instead of the name in the docker rename command.
> 
> **Updating Scripts:** If you have scripts or tools that reference container names, update them to reflect the new container names after renaming.
> 
> **Networking and Volumes:** Renaming a container does not affect its networking or volume configurations; only the container name is changed.

----
### Docker network
Docker networking is a core aspect of how Docker containers communicate both with each other and with the external world. Docker provides several options for networking, each designed to address different use cases, from simple container-to-container communication to complex, multi-host setups.

#### Types of Docker Networks

1. Bridge Network (Default Network)
This is the default network for standalone containers.
Containers in the same bridge network can communicate with each other using their IP addresses or container names.
If you don't specify a network when running a container, it gets attached to this default bridge network.
```
docker network create rahees-bridge
docker run -d --network rahees-bridge --name container1 my-app
docker run -d --network rahees-bridge --name container2 my-app
```

2. **Host Network**
In this mode, the container shares the host’s networking stack and IP address.
It bypasses Docker’s own network isolation and allows the container to communicate directly with the host's network.
Useful when you need to minimize network latency or directly access host services.
```
docker run --network host my-app
```

3. **Overlay Network**

Typically used in Docker Swarm or Kubernetes setups.
It enables containers on different Docker hosts to communicate with each other.
It requires a key-value store (like Consul, etcd, or ZooKeeper) to maintain the network state.
```
docker network create --driver overlay my-overlay
docker service create --name my-service --network my-overlay my-app
```
4. **None Network**

Completely disables networking for the container.
Used in cases where you need full isolation from the network (for example, for security purposes).
```
docker run --network none my-app
```
5. **Macvlan Network**

Provides the ability to assign a MAC address to containers.
Containers can appear as physical devices on the network, and they get their own IP addresses.
Used when containers need to be directly accessible on the local network with a dedicated IP.
```
docker network create -d macvlan --subnet=192.168.1.0/24 --gateway=192.168.1.1 -o parent=eth0 my-macvlan
docker run --network my-macvlan --ip 192.168.1.100 my-app
```

#### Types of Docker Drivers:

The following network drivers are available by default, and provide core networking functionality:

Driver	Description
1. **bridge**  
   The default network driver.

2. **host**  
   Remove network isolation between the container and the Docker host.

3. **none**  
   Completely isolate a container from the host and other containers.

4. **overlay**  
   Overlay networks connect multiple Docker daemons together.

5. **ipvlan**  
   IPvlan networks provide full control over both IPv4 and IPv6 addressing.

6. **macvlan**  
   Assign a MAC address to a container.

#### Key Docker Networking Commands:
```
docker network ls
docker network inspect <network_name_or_id>
docker network create --driver bridge my-network
docker network connect <network_name> <container_name>
docker network disconnect <network_name> <container_name>
docker network rm <network_name_or_id>
docker network prune
```
#### DNS in Docker Networks:
Docker has an internal DNS server that maps container names to their IP addresses. Containers can communicate with each other by referring to their container names.
Example: Multi-container Setup with Bridge Network
Create a bridge network:

docker network create rahees-bridge
Run two containers on the same network:
```
docker run -d --network rahees-bridge --name web nginx
docker run -d --network rahees-bridge --name db postgres
docekr run --name cntr-in-other-ntwrk nginx
docker exec -i db sh -c "ping web"
docker exec -i web sh -c "ping db"
docker exec -i web sh -c "cat /etc/resolve.cof"
docker exec -i cntr-in-other-ntwrk sh -c "ping db"  ## will fail
docker network connect rahees-bridge cntr-in-other-ntwrk
docker exec -i cntr-in-other-ntwrk sh -c "ping db"  ## will pass and able to ping
docker inspect network rahees-bridge
docker network disconnect rahees-bridge cntr-in-other-ntwrk
docker network prune
```
Containers can now communicate with each other by their names (e.g., web can communicate with db using the hostname db).

## Give the demo and take referene from UR Google Doc explain internal DNS and use docker network connect command as well

#### Basic Usage of docker wait
Wait for a Container to Stop
To use the docker wait command, provide the container ID or name. The command will block until the container stops and then output the exit code of the container.

Example Walkthrough
First, start a container. For example, run an Nginx container with the name mynginx:
```
docker run --name mynginx nginx
```
> [!NOTE]  By default, Nginx containers run indefinitely because the Nginx service doesn’t exit on its own. For this example, you might use a container that exits after completing its task.

In a real scenario, if you have a container that performs a task and then stops, you can use docker wait to wait for it to stop. For example, if you run a container with a command that exits:
```
docker run --name mytask -d alpine /bin/sh -c "echo 'Learn DevOps with Rahees Khan ' && sleep 60"
docker wait mytask
```
##### Expected Output:

The command will print the exit code of the container after it stops. For example, if the container exits successfully, you might see:
0

<img width="1721" alt="image" src="https://github.com/user-attachments/assets/399b32aa-c57d-4508-a87a-3fc6f0bcc1b1">

> [!TIP]
> **Exit Codes:** The exit code provides information about how the container finished. A code of 0 usually indicates success, while non-zero codes indicate errors.
>
> **Scripting:** docker wait is particularly useful in shell scripts or CI/CD pipelines where you need to ensure a container has finished its task and to capture its result.
>
> **Blocking Behavior:** The command blocks until the container stops, so it is not suitable for use in interactive environments where you need to continue working while waiting for the container to stop.

Common Use Cases

> [!IMPORTANT]
> **Automation:** In automated workflows, you might need to run a container, wait for it to complete, and then take actions based on its exit status.
> 
> **Testing:** During automated testing, waiting for a container to complete its execution and checking the exit code helps determine if tests passed or failed.
>
> **Resource Cleanup:** Waiting for containers to stop before performing cleanup or resource release operations.

----
### Docker diff
The docker diff command is used to inspect changes made to the filesystem of a Docker container compared to its original image. It shows the differences in the filesystem of a container since it was started from the image, including files added, modified, or deleted. This command is useful for debugging and understanding what changes a container has made during its execution.

Basic Usage of docker diff

```
docker diff container-name
```
#### Interpreting the Output
The command outputs a list of changes made to the container’s filesystem, with each change listed with a prefix indicating the type of change:

> [!NOTE]
> A: A file or directory was added.
> 
> C: A file or directory was changed.
>
> D: A file or directory was deleted.
<img width="1728" alt="image" src="https://github.com/user-attachments/assets/f860674f-9440-4c47-a60d-7f6cd0950227">

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
