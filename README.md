Dira Abinawa - Dewan Kerja Ranting (DKR) API
This is a FastAPI-based API for managing Dewan Kerja Ranting (DKR) data of Dira Abinawa schools. It provides endpoints to perform CRUD (Create, Read, Update, Delete) operations on the DKR data.

Requirements
Make sure you have Python and the required libraries installed:

Python 3.x
FastAPI
Pydantic
pymongo
Installation
Clone the repository:

bash
Copy code
git clone <repository_url>
cd <repository_name>
Install the required libraries using pip:

bash
Copy code
pip install fastapi pydantic pymongo
Configuration
The API requires a MongoDB connection to store and retrieve data. Update the MongoDB connection string in the following line of code to match your MongoDB database:

python
Copy code
client = MongoClient("mongodb+srv://RDGalihRakasiwi:fkSeIRIz0aQ3NfVf@cluster0.ni5ltny.mongodb.net/?retryWrites=true&w=majority")
Data Model
The data model for the "dewan_kerja_ranting" collection in MongoDB is defined using Pydantic:

python
Copy code
from enum import Enum
from pydantic import BaseModel

class level(str, Enum):
    def __str__(self):
        return str(self.value)
    BANTARA = "Bantara"
    LAKSANA = "Laksana"
    GARUDA = "Garuda"

class DKR(BaseModel):
    name: str
    school_name: str
    level: level
    position: str
    period: str
Endpoints
GET - /dkr/
Retrieves all Dewan Kerja Ranting (DKR) records from the database.

POST - /dkr/
Adds a new Dewan Kerja Ranting (DKR) record to the database. The payload should be in JSON format and match the DKR model.

PUT - /dkr/{id}
Updates an existing Dewan Kerja Ranting (DKR) record in the database with the specified ID. The payload should be in JSON format and match the DKR model.

DELETE - /dkr/{id}
Deletes a Dewan Kerja Ranting (DKR) record from the database with the specified ID.

Usage
Start the FastAPI server:

bash
Copy code
uvicorn main:app --reload
Access the API at http://127.0.0.1:8000 in your browser or use a tool like curl or Postman to interact with the API endpoints.

Note
Ensure that your MongoDB server is running and accessible at the specified connection string.
This API is intended for educational purposes only and may not be suitable for production use without further modifications and security considerations.
Feel free to modify and enhance the API to fit your specific use case. Happy coding!