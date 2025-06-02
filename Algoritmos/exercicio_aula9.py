import pathlib

'''
Criar uma função recursiva chamada ler_arquivos_recursivamente que:​

Recebe um caminho inicial (string).​
Acessa todos os arquivos .txt dentro dessa estrutura.​
Imprime na tela o caminho do arquivo e seu conteúdo.​​
A função deve ser recursiva — ou seja, você não pode usar laços como while ou for para explorar diretórios.
'''

def ler_arquivos_recursivamente(caminho):
    p = pathlib.Path(caminho)
    if p.is_dir():
        # Chama recursivamente para cada item no diretório
        for item in p.iterdir():
            ler_arquivos_recursivamente(str(item))
    elif p.suffix == '.txt':
        with p.open('r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(f'Arquivo: {p}\nConteúdo:\n{conteudo}\n')
