#  Flask server to simulate a fuctional concurrent program.

This project is designed to explain how functional concurrency works in a practical way. 
The server expose 12 endpoints, one of each musical tone. 12+ people must access to each endpoint to get a html response that renders a button that produces the sound of his assigned musical note.

Each person works as a thread, with the button working as a function and the time that press the button and produces sound, as the input of the function

If all the users are coordinated, a functional concurrent program that creates songs is born!

----------------------

### How to run it.

This program requires

  * docker
  * internet access

Also, if you are using Linux, is recommended to use 

  * ufw

to easly expose a port for the server.

----------------------

### How to run it.

Inside the directory

`Server presentacion funcional`

run

`sudo docker build -t server_presentacion_funcional .`

to build the docker image.

As this project is builded using poetry, all the dependencies are self installed when the image is builded.

Now lets supouse that you want to run the server at port 33. In that case you will need to expose it. You can do it using ufw.

`sudo ufw enable`
`sudo ufw allow 33`

Then, as poetry gives you an entry point to run the server, you can start the server using.

`sudo docker run -p 33:5000 server_presentacion_funcional poetry run server`

To check if server is working, you can curl it from another node inside the same net

`curl YOUR-IP:33 -v`

