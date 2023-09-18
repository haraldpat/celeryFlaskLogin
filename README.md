***Code Navigation***

This project consists of a main folder `src` which contains all the project files. The files outside the source folder consists of `docker-compose.yml` and a `local.env` file which are used for running the docker containers. The `src` folder contains the entrypoint of the Flask project `app.py`, `settings` folder which contains your application settings and an `apis` folder that stores all your urls and views.

Specify the urls in `urls.py` file in the api folder as list of tuples with following format:

    (endpoint, view_func, methods, description)
example:

    ("/", views.index, ["GET"], "index page")

***Installation***

Running the scaffolding app is very easy. First [install](https://docs.docker.com/install/) docker for your operating system from the docs provided in the docker website. Also [install](https://docs.docker.com/compose/install/) docker-compose

Then run

    sudo docker-compose build
and then

    sudo docker-compose up
This will run the server at port http://localhost:8400/

The index view will be displayed in your browser.

***Logs***

A `logs` folder is created in the root of the project i.e outside the `src` folder, which is mounted using the docker-compose volume mount. It will contain a file `flask-scaffolding.log` and will contain the project logs.