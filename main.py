from fastapi import FastAPI
from routes.dkr import dkr

app = FastAPI(
    title="Dira Abinawa - DKR",
    version="1.0.0"
)

app.include_router(dkr)