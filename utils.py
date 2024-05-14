import base64
import os
import json

from dotenv import load_dotenv
from openai import OpenAI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
load_dotenv()


# Function to encode the image
def encode_image(image):
    return base64.b64encode(image.read()).decode('utf-8')


def get_openai_client():
    api_key = os.environ.get('OPENAI_API_KEY')
    client = OpenAI(api_key=api_key)
    return client


def openai_query(image):
    # Get the OpenAI client
    client = get_openai_client()

    # Encode the image
    encoded_image = encode_image(image)

    # Call the OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user",
             "content": f"Can you extract the following info "
                        f"if I would give you an image of the receipt as follows: {encoded_image}?"
                        f"total"}
        ]
    )

    # Return the response
    return json.loads(response.choices[0].message.content)


def mongodb_connect():
    # Connect to the MongoDB database
    username = os.environ.get('MONGODB_USERNAME')
    password = os.environ.get('MONGODB_PASSWORD')
    uri = (f"mongodb+srv://{username}:{password}"
           f"@personal.if3xkx2.mongodb.net/?retryWrites=true&w=majority&appName=personal")
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return client
