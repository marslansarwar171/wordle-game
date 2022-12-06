# MongoDB Atlas with FastAPI

This is a small project demonstrating how to build an API with [MongoDB Atlas](https://www.mongodb.com/atlas/database) and [FastAPI](https://fastapi.tiangolo.com/).

## How to Run Project Locally

Python Version `3.9.15`   
If you want to get up and running,
activate your Python virtualenv, and then run the following from your terminal (edit the `MONGODB_URI` first!):

```bash
# Install the requirements:
pip install -r requirements.txt

# Configure the location of your MongoDB database:
export MONGODB_URI="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

# Start the service:
uvicorn app:app --reload
```

Now you can load http://localhost:8000/docs in your browser ... but there won't be much to see until you've inserted some data.