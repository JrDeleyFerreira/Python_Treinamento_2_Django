from fastapi import APIRouter
from modelo_endpoint.products import Products

router = APIRouter(prefix='/modelo-endpoint')

@router.get('/', response_model= list[Products])
def listar_contas():
    return [
        Products(
            name= 'Carré de Cordeiro',
            price= 55.7,
            quantity= 1
        ),
        Products(
            name= 'Desodorante Dove',
            price= 18.9,
            quantity= 2
        ),
    ]
    
@router.post('/', response_model= Products, status_code= 201)
def cria_novo_produto(prod: Products):
    return Products(
        name= prod.name,
        price= prod.price,
        quantity= prod.quantity
    )