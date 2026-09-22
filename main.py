from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola Mundo desde FastAPI desde Python! desde un cachyOs con omarchy"

@app.get("/url")
async def get_url():
    return {"url": "https://www.cachyos.com"}

@app.get("/repo")
async def get_repo():
    return {"repo": "https://feliperivasdev.github.io/DavidFelipeGustinRivas/"}