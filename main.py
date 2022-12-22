from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return { 'data': { 'msg': "Thank God !"}}