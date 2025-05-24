from fastapi.responses import JSONResponse
from fastapi import FastAPI
import uvicorn

from core.config import settings

app = FastAPI(title='PokEvolution')

@app.get('/pokemon/{id}')
async def retrieve_pokemon(id:int):
  
  response = settings.retrievePokemon(id)
  
  return JSONResponse(response)

if __name__ == '__main__':
  uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)