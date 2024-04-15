class Restaurante:  
    restaurantes = []


    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.title() 
        self._ativo = False  
        Restaurante.restaurantes.append(self)
    
    def __str__(self): 
        return f'{self.nome} | {self.categoria}'   
    
    def listar_restaurantes():  
        print()
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}') 
        print()
        for restaurante in Restaurante.restaurantes: 
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}') 
    @property 
    def ativo(self): 
        return '✅' if self._ativo else '❌ '

restaurante_pizza = Restaurante('pizzaria do papaléguas', 'italiana') 

restaurante_macarrao = Restaurante('Macarronada da Dna. Joana', 'Massas em geral') 

Restaurante.listar_restaurantes()