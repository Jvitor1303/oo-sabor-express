class Restaurante: 
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria 
        self.ativo = False  
    
    def __str__(self): 
        return f'{self.nome} | {self.categoria}'   

restaurante_pizza = Restaurante('Pizzaria do Papaléguas', 'Italiana') 
 
restaurante_macarrao = Restaurante('Macarronada da Dna. Joana', 'Massas em geral') 

restaurantes = [restaurante_macarrao, restaurante_pizza] 

print()
print(restaurante_pizza) 
print()
print(restaurante_macarrao)
print()
