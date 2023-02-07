import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_hello():
    return {'message': 'Hello World'}

if __name__ == '__main__':
    uvicorn.run(app)
