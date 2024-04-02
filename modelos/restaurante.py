class Restaurante: 
    nome = ''
    categoria = '' 
    ativo = False 

restaurante_pizza = Restaurante() 
restaurante_pizza.nome = 'Pizzaria do Papaléguas'
restaurante_pizza.categoria = 'Pizzaria' 



restaurante_macarrao = Restaurante() 

restaurantes = [restaurante_macarrao, restaurante_pizza] 

print(vars(restaurante_pizza))

