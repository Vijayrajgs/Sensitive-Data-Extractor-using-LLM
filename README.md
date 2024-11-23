# Aruva
Sensitive Data Detection with Dockerized Flask Application

# Flask Web Application with MongoDB in Docker

This project provides a Flask-based web application that connects to a MongoDB database running inside a Docker container. The web application allows users to upload files, extract sensitive data, and view the extracted information in the web interface. It also includes functionalities for viewing previous scans and deleting entries from the database.

## Project Setup

### Prerequisites

Before running the application, ensure that you have the following installed:
- Docker and Docker Compose: [Install Docker](https://docs.docker.com/get-docker/)
- Python 3.x: [Install Python](https://www.python.org/downloads/)
- Flask: `pip install Flask`
- MongoDB (If you prefer running MongoDB outside Docker, make sure MongoDB is installed and running on port 27017)

### Docker Setup (for MongoDB)

This project uses Docker to run the MongoDB service. The MongoDB instance will be accessible from the Flask web application running locally.

#### Steps to run MongoDB in Docker

1. **Clone the project repository: or download zip file of it**

    ```bash
    git clone https://github.com/Vijayrajgs/Aruva
    ```

2. **Run MongoDB using Docker Compose:**

    Make sure you are in the project root directory (where `docker-compose.yml` is located) and execute the following command to start MongoDB in a Docker container:

    ```bash
    docker-compose up -d
    ```

    This will:
    - Pull the official MongoDB image.
    - Start the MongoDB container.
    - Expose MongoDB on port `27017`.

3. **Verify MongoDB is running:**

    After running `docker-compose up -d`, MongoDB should be up and running. You can check its status by running:

    ```bash
    docker ps
    ```

    You should see an entry for the MongoDB container with port `27017` exposed.

### Setting Up Flask Web Application

1. **Create a Python Virtual Environment (optional but recommended):**

    I used a virtual env, It's best to set up a Python virtual environment to manage dependencies.

    ```bash
    python3 -m venv venv
    venv\Scripts\activate
    ```

2. **Install the dependencies:**

    Make sure all required Python libraries are installed by running:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the Database Connection:**

    In the `config.py` file, the Flask app connects to MongoDB running at `localhost:27017`.

    ```python
    class Config:
        MONGO_URI = "mongodb://localhost:27017/scans_db"  # MongoDB connection URI
    ```

    This setup assumes MongoDB is running locally on port `27017`, which is the default port exposed by the Docker container.

4. **Run the Flask Web Application:**

    After setting up your environment, start the Flask web application by running:

    ```bash
    python app.py
    ```

    This will start the Flask app on `http://localhost:5000`.

### Application Features

The web app provides the following features:

- **File Upload**: Upload text files and extract sensitive data (PII, PHI, PCI).
- **View Extracted Data**: After uploading a file, you can view the extracted sensitive data in a clean, user-friendly interface.
- **History**: View a history of previously uploaded files and the extracted data.
- **Delete Entry**: Delete any previously uploaded scan entries from the database.

### Routes

- **Home Page (`/`)**: Displays the main interface.
- **Upload Page (`/Upload`)**: Allows users to upload a file.
- **History Page (`/History`)**: Displays all previously uploaded scans.
- **Delete Entry (`/Delete_entry/<scan_id>`)**: Deletes a specific scan entry from the database.

### Directory Structure
project/

│ ├── app/ 
│ ├── init.py 
│ ├── app.py 
│ ├── config.py 
│ ├── routes.py 
│ ├── detection/ 
│ │ └── llm_detector.py 
│ ├── models/ 
│ │ ├── database.py 
│ │ └── scan_model.py 
│ ├── static/
| | └──styles.css
│ ├── templates/ 
│ │ ├── index.html 
│ │ ├── upload.html 
│ │ ├── view_scan.html 
│ │ └── history.html 
│ └── utils/ 
│ └── file_utils.py 
│ ├── docker-compose.yml 
├── Dockerfile 
├── requirements.txt 
└── README.md

### Running the Application

1. **Start MongoDB** (if it's not already running):

    ```bash
    docker-compose up -d
    ```

2. **Start the Flask Web Application**:

    ```bash
    python app.py
    ```

3. **Access the application**:

    Open a browser and navigate to `http://localhost:5000` to interact with the app.

### Stopping the Application

To stop the application:
- Stop the Flask web app by pressing `Ctrl+C` in the terminal.
- To stop the MongoDB container, run:

    ```bash
    docker-compose down
    ```
