from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  PokeApiUrl = 'https://pokeapi.co/api/v2/pokemon/ditto'
  
settings = Settings()