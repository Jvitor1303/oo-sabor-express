from modelos.restaurante import Restaurante 

#instância é a 'variável' que atribuimos á classe. Essas duas variáveis são instâncias da classe Restaurante
restaurante_pizza = Restaurante('pizzaria do papaléguas', 'italiana') 

restaurante_macarrao = Restaurante('Macarronada da Dna. Joana', 'Massas em geral')  

restaurante_mexicano = Restaurante('Mexican food', 'Mexicana')
 


def main(): 
    Restaurante.listar_restaurantes()


if __name__ == '__main__': 
    main()