# Função que lê dois números sem repetir a frase
def leitora_numeros() -> list:
    """Esta função insere os número base para a função que o usuário deseja realizar"""
    i = 0
    numeros = []
    while i < 2:
        numeros.append(float(input(f"Digite o primeiro número {i+1} que deseja operar")))
        i+=1
    return numeros        
    
    
def leitora_operacao() -> str:
    operacao = input("""Digite a operação que deseja realizar. 
Pressione + para adição; 
- para subtração; 
/ para divisão; 
* para multiplicação""")
    return operacao



def leitora() -> list:
    lista_numeros = leitora_numeros()
    operacao = leitora_operacao()
    return [lista_numeros, operacao]


def escritora(resultado:float) -> None:
    """Esta função coloca o resultado na tela"""
    print(f"O resultado da operação é igual a {resultado}.")