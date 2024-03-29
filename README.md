# DKR API

This API provides a way to manage data about Dewan Kerja Ranting (DKR) in a MongoDB database.

## Endpoints

* `GET /`: Get all DKRs.
* `POST /`: Create a new DKR.
* `PUT /<id>`: Update a DKR.
* `DELETE /<id>`: Delete a DKR.

## Models

* `DKR`: A model representing a DKR.
* `DewanKerja`: A schema representing a DKR for the API.
* `DewansKerja`: A list of `DewanKerja` objects.

## Dependencies

* FastAPI
* PyMongo
* Enum

## Usage

To use the API, you will need to install the dependencies and start the server.

pip install fastapi pymongo enum
uvicorn main:app --reload


Once the server is started, you can access the API at `http://localhost:8000/`.

## Documentation

The API documentation is available at `http://localhost:8000/docs`.