from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('João', 5) 
restaurante_praca.receber_avaliacao('Rodiney', 10) 
restaurante_praca.receber_avaliacao('Neymar Jr.', 7) 
restaurante_praca.receber_avaliacao('Iguinho Brioche', 1) 
restaurante_praca.receber_avaliacao('Neide', 9) 



def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
