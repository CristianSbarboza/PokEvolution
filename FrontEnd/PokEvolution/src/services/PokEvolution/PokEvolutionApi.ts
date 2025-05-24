import type { Pokemon } from "../../types/Pokemon"

const ApiUrl = `https://localhost:8000/api/v1/pokemon/`

export async function getPokemon():Promise<Pokemon[]>{
    const response = await fetch(`${ApiUrl}/id`);
    if (!response.ok){
        throw new Error('Erro ao buscar pokemon')
    }

    console.log(response)
    return response.json()
}