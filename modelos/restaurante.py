class Restaurante: 
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria 
        self.ativo = False 

restaurante_pizza = Restaurante('Pizzaria do Papaléguas', 'Italiana') 
 
restaurante_macarrao = Restaurante('Macarronada da Dna. Joana', 'Massas em geral') 

restaurantes = [restaurante_macarrao, restaurante_pizza] 

print(vars(restaurante_pizza))
print(vars(restaurante_macarrao))

