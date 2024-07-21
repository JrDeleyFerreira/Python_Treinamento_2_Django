from fastapi import APIRouter

router = APIRouter(prefix='/analyze')

@router.get('/', response_model= dict)
def returned_message():
    return {'id': 1, 'Rota 2' : 'Agora sim'}


@router.get('/id_pessoa/frases', response_model= list[dict])
async def alguma_coisa(id_pessoa: int | None = 0):
    citacoes = [
        {'id': 1, 'personalidade': 'Coringa', 'frase': 'Sabe qual é a chave do caos? O medo!'},
        {'id': 2, 'personalidade': 'Harvey Dent', 'frase': 'A noite é mais escura pouco antes de amanhecer.'},
        {'id': 1, 'personalidade': 'Coringa', 'frase': 'As pessoas são tão boas quanto o mundo permite.'},
        {'id': 1, 'personalidade': 'Coringa', 'frase': 'Por que você está tão triste?'},
        {'id': 2, 'personalidade': 'Harvey Dent', 'frase': 'A única justiça é o acaso.'}
    ]
    
    filtro = list(filter(lambda x : x['id'] == id_pessoa, citacoes))
    return filtro