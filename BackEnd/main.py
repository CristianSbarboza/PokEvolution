from webbrowser import get
from fastapi import FastAPI, Response
import uvicorn
 

app = FastAPI()

@app.get('/')
async def GetAll():
  return Response('Resposta')


if __name__ == '__main__':
  uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)