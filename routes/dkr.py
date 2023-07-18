from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.dkr import DKR
from config.db import connection
from schemas.dkr import DewanKerja, DewansKerja
from bson import ObjectId
import pymongo

dkr = APIRouter()

@dkr.get('/')
async def find_all_dkr():
    dkr_cursor = connection.local.dkr.find()
    dkr_list = list(dkr_cursor)
    if not dkr_list:
        return "Maaf, Anda tidak memiliki data apapun"
    result = [DewanKerja(dkr) for dkr in dkr_list]
    return result


@dkr.post('/')
async def create_dkr(dkr : DKR):
    connection.local.dkr.insert_one(dict(dkr))
    return DewansKerja(connection.local.dkr.find())

@dkr.put('/{id}')
async def update_dkr(id, dkr: DKR):
    updated_dkr = connection.local.dkr.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(dkr)},
        return_document=pymongo.ReturnDocument.AFTER
    )
    return DewanKerja(updated_dkr)

@dkr.delete('/{id}')
async def delete_dkr(id):
    dkr = connection.local.dkr.find_one_and_delete({"_id": ObjectId(id)})
    if dkr:
        return DewanKerja(dkr)
    else:
        return {"message": "Student not found"}
