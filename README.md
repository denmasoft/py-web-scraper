## Getting Started
### Clone Project
Clone the GitHub repo to your local machine:

```bash
git clone https://github.com/denmasoft/py-web-scraper.git
```
Go to the directory where you cloned the repo...
```bash
cd py-web-scraper
```

### Dependencies installation
Now, install the project dependencies.

Requirements:

* Python 3.6+

```bash
python install -r requirements.txt
```

## Environment Variables

### `.env`
```bash
cp .env.dist .env
```
This is where you should put all of your secrets as well as configuration depending on your environment.


### Running the Project
After completing the installation step, you're ready to start the project.

| script | Description                       |
| ------|-----------------------------------|
| start | Serves your app at localhost:5000 |


`python app.py` running locally! Your app should now be running on [localhost:5000](http://localhost:5000/scrape).

## Containerization with Docker

### Build a Docker Image

In your terminal, navigate to the directory py-web-scraper and run the following command to build a Docker image:

```bash
docker build -t scrapper-api:latest .
```
- This command builds a Docker image using the Dockerfile in the current directory.
- The `-t` flag is used to tag the image with a name of your choice. In this case, the image is tagged with the name `scrapper-api`.
- The `.` at the end of the command line indicates that the Dockerfile is in the current directory.
- This image can be used to create containers that run your Flask application.
- `:latest` is the version of the image. This allows you to update or differentiate images (e.g., rc1). You should use it whenever you create an image. 
- You can list all the images on your machine using the `docker images` command.

### Create a Docker Container

Now that the Docker image is ready, create a container that runs the app. To do this, run the following command:

```bash
docker run -d -p 5000:5000 scrapper-api:latest
```
- The `-d` flag is used to run the container in detached mode (in the background).
- The `-p` flag is used to map the host port 5000 to the container port 5000. This way you can access the app running inside the container at http://localhost:5000.

#### API Endpoints

The Flask application exposes the following API endpoints:

- `POST /scrape`: Start scraping the specified url.

#### Application Logic

Here's a high-level overview of how this app works:

- **POST /scrape**: When you access this endpoint, the application start scraping the specified url. You can also send some payload as detailed in the postman collection.

#### Postman
You can import the postman collection located in the root directory to see some of the payload you can use.