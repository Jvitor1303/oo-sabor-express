class Restaurante:  
    restaurantes = []


    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title() 
        self._ativo = False  
        Restaurante.restaurantes.append(self)
    
    def __str__(self): 
        return f'{self.nome} | {self.categoria}'   
    
    @classmethod
    def listar_restaurantes(cls):  
        print()
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}') 
        print()
        for restaurante in cls.restaurantes: 
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}') 
    @property 
    def ativo(self): 
        return '✅' if self._ativo else '❌ '

restaurante_pizza = Restaurante('pizzaria do papaléguas', 'italiana') 

restaurante_macarrao = Restaurante('Macarronada da Dna. Joana', 'Massas em geral') 

Restaurante.listar_restaurantes()