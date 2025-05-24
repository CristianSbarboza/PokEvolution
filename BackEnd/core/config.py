from pydantic_settings import BaseSettings
import requests

from core.schemas import Pokemon

class Settings(BaseSettings):
  PokeApiUrl: str = 'https://pokeapi.co/api/v2/pokemon/'
  API_VERSION: str = 'v1'
  
  def retrievePokemon(self, id:int, ) -> Pokemon:
    RetrievePokeApiUrl: str = f'https://pokeapi.co/api/v2/pokemon-form/{id}'
    response =   response = requests.get(RetrievePokeApiUrl).json()
    
    name = response['name']
    clicks=0
    template = response['sprites']['front_default']
    next = id + 1
    
    pokemon = Pokemon(id=id, name = name, clicks = clicks, template = template, next= next)
    
    return pokemon.__dict__
  
settings = Settings()