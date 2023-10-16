from fastapi import FastAPI

app = FastAPI(title='Infrahub',
              description='Infrastructure Source of Truth',
              version="0.1",
              docs_url='/docs',
              redoc_url='/redoc')

@app.get("/")
async def home():
    return {"status": "Coming soon"}