# View 

def inicio_do_programa():
    print('''
-----------------------------------------
 
##### Sistema de palavras do Spelling Bee #####
          
Esse programa foi desenvolvido a partir das palavras do
Spelling Bee do Senac RS 2025.

------- O que esse programa faz? --------

Neste programa, você pode:
    - filtrar as palavras por tamanho ou letra presente
    - jogar de forma escrita para adivinhar as palavas 
          
-----------------------------------------
          ''')

def imprimir_menu_inicial():
    print('''
------------ Menu inicial -------------

Escolha uma opção:
          
          1 - Consultar e filtrar palavras
          2 - Jogar
          3 - Encerrar programa

''')

def imprimir_menu_jogos():
    print(f'''
------------ Menu de opções -------------

O que você gostaria de jogar:
          
        1 - Jogo de adivinhação
        2 - Jogo da forca
        3 - Voltar ao menu inicial

''')

def imprimir_menu():
    print(f'''          
------------ Menu de opções -------------
          
       1 - Filtrar palavras pela quantidade total de letras
       2 - Filtrar palavras pela quantidade mínima de letras
       3 - Filtrar palavras por alguma letra ou conjunto de letras
       4 - Ver todas as palavras
       5 - Voltar ao menu inicial
''')
    
def imprimir_menu_jogo_adivinhar():
    print('''
O que deseja fazer? 

    1 - Iniciar nova tentativa
    2 - Ver palavras acertadas e erradas
    3 - Voltar ao menu inicial
        ''')

def imprimir_menu_jogo_forca():
    print(f'''
------------ Menu de opções -------------

        1 - Fazer uma tentativa
        2 - Ver estatísticas
        3 - Voltar ao menu inicial

''')

def aperte_enter():
    print(f'''
-----------------------------------------

Aperte Enter para voltar ao menu
          
-----------------------------------------
''')
    input()
    menu()

def aperte_jogar():
    print(f'''
-----------------------------------------

Aperte Enter para iniciar
          
-----------------------------------------
''')
    input()
    menu()

def encerrar_programa():
    print("""
---------- Programa encerrado. ----------
          """)
    
### Menus

def menu_inicial():
    imprimir_menu_inicial()
        
    opcao_menu_inicial = input('Digite a opção desejada: ')

    consultar = {
        "1" : menu,
        '2' : menu_jogos,
        '3' : encerrar_programa
    }

    try:
        consultar[opcao_menu_inicial]()
    except KeyError:
        print('Opção inválida! Digite uma opção válida!')

        menu_inicial()

def menu():
    imprimir_menu()    
    item_menu = input("Digite a opção escolhida: ")

    consultar = {
        '1' : filtro_quant_letras,
        '2' : filtro_min_letras,
        '3' : filtro_letra,
        '4' : ver_todas_palavras,
        '5' : menu_inicial
    }

    try:
        consultar[item_menu]()

    except KeyError:
        print('Opção inválida! Digite uma opção válida!')
        menu()

def menu_jogos():
    imprimir_menu_jogos()

    opcao_menu_jogos = input('Digite a opção desejada: ')

    consultar = {
        '1' : menu_jogo_adivinhar,
        '2' : menu_jogo_forca,
        '3' : menu_inicial

    }

    try:
        consultar[opcao_menu_jogos]()
    except KeyError:
        print('Opção inválida! Digite uma opção válida!')

        menu_inicial()

def menu_jogo_adivinhar():
    imprimir_menu_jogo_adivinhar()

    escolha_menu_adivinhar = input('Digite a opção desejada: ')

    consultar = {
        '1' : jogo_adivinhar,
        '2' : desempenho_jogo_adivinhar,
        '3' : menu_inicial
    }
    
    try:
        consultar[escolha_menu_adivinhar]()
    except KeyError:
        print('Opção inválida! Digite uma opção válida!')

        menu_jogo_adivinhar()

def menu_jogo_forca():
    imprimir_menu_jogo_forca()

    escolha_menu_forca = input('Digite a opção desejada: ')

    consultar = {
        '1' : comparar_palavras,
        '2' : estatisticas_forca,
        '3' : menu_inicial
    }
    
    try:
        consultar[escolha_menu_forca]()
    except KeyError:
        print('Opção inválida! Digite uma opção válida!')
        menu_jogo_forca()

## Filtros 

def filtro_quant_letras():
    numero_de_letras = int(input("Digite a quantidade de letras da palavra: "))
    print(f'Você digitou: {numero_de_letras}')
    print()
    
    for palavra in lista_de_palavras:
        if len(palavra) == numero_de_letras:
            print(palavra)
            
    aperte_enter()
    
def filtro_min_letras():
    numero_de_letras = int(input("Mínimo de letras: "))
    print(f'Você digitou: {numero_de_letras}')
    print()

    for palavra in lista_de_palavras:
        if len(palavra) >= numero_de_letras:
            print(palavra)

    aperte_enter()

def filtro_letra():
    letra_escolhida = input('Digite a letra na palavra: ')
    print(f'Você digitou: {letra_escolhida}')
    print()

    for palavra in lista_de_palavras:
        if letra_escolhida in palavra:
            print(palavra)

    aperte_enter()

def ver_todas_palavras():
    for palavra in lista_de_palavras:
        print(palavra)

    aperte_enter()

### Jogo adivinhar

def jogo_adivinhar():
    
    palavra_digitada = input('Qual palavra deseja adivinhar? ').capitalize()

    if palavra_digitada in lista_de_palavras:
        if palavra_digitada not in palavras_acertadas:
            print(f'''
            
            Parabéns! {palavra_digitada} está correto! :)
            
            ''')
            palavras_acertadas.append(palavra_digitada)
            desempenho_jogo_adivinhar()

            input()
            nova_tentativa_jogo()
        else:
            print(f'Ops! Você já adivinhou {palavra_digitada}')
            nova_tentativa_jogo()
    else:
        print(f'''
        
        Poxa vida! {palavra_digitada} não está correta :(
        
        ''') 

        palavras_erradas.append(palavra_digitada)
        nova_tentativa_jogo()

def imprimir_acertos_adivinhar():
    contador = 0
    for palavra in palavras_acertadas:
        print(f'{(contador+1)}: {palavra}')
        contador += 1

def imprimir_erros_adivinhar():
    contador = 0
    for palavra in palavras_erradas:
        print(f'{(contador+1)}: {palavra}')
        contador += 1

def exibir_palavras_acertadas():
    print(f'''Você acertou {len(palavras_acertadas)} / 250 palavras!''')
    
def desempenho_jogo_adivinhar():
    exibir_palavras_acertadas()
    print()
    imprimir_acertos_adivinhar()
    print()
    imprimir_erros_adivinhar()
    print()
    menu_jogo_adivinhar()

def nova_tentativa_jogo():
    escolha_tentativa = input(f'''O que você deseja fazer? 
                              
    1 - Nova tentativa
    2 - Voltar ao menu''')

    consultar = {
        "1" : jogo_adivinhar,
        '2' : menu_jogo_adivinhar,
    }

    try:
        consultar[escolha_tentativa]()
    except KeyError:
        print('Opção inválida! Digite uma opção válida!')

        nova_tentativa_jogo()

###### Sortear palavra

def sortear_palavra():
    palavra_sorteada = random.choice(lista_de_palavras)

    return palavra_sorteada

def jogo_palavra_sorteada():
    palavra_sorteada = sortear_palavra()

    print(f'''
A palavra sorteada tem {len(palavra_sorteada)} letras.

''')
    
    tentativa_palavra_sorteada = input('Qual palavra você acha que é?').capitalize()

    if tentativa_palavra_sorteada in palavra_sorteada:
        print('Parabéns! Você acertou!')    
    else:
        print(f'Poxa, está errado! A palavra correta era {palavra_sorteada}')

def sorteada_tentar_novamente():
    print('''
Deseja tentar novamente?

''')

### Jogo Forca

def estatisticas_forca():
    imprimir_acertos_forca()
    imprimir_erros_forca()
    input()
    menu_jogo_forca()

def imprimir_acertos_forca():
    print(f'Você acertou {len(forca_acertos)}!')

    contador = 1
    for palavra in forca_acertos:
        print(f'{contador}: {palavra}')
        contador += 1
    print()

def imprimir_erros_forca():
    print(f'Você errou {len(forca_erros)}!')

    contador = 1
    for palavra in forca_erros:
        print(f'{contador}: {palavra}')
        contador += 1
    print()

def comparar_palavras():
    palavra_sorteada = sortear_palavra()
    print(f'A palavra sorteada tem {len(palavra_sorteada)} letras.')
    print()
 
    palavra_digitada = input('Faça uma tentativa: ').capitalize()
    print(f'Você digitou: {palavra_digitada}')
    print()

    lista_sorteada = list(palavra_sorteada)
    lista_digitada = list(palavra_digitada)

    comparacao = []

    for letra in lista_sorteada:
        if letra in lista_digitada:
            comparacao.append(letra)
        else:
            comparacao.append('_')

    print(''.join(comparacao))
    
    if lista_digitada == list(palavra_sorteada):
        print(f'''
Parabéns! Você acertou a palavra!
{palavra_sorteada}
''')
        forca_acertos.append(palavra_sorteada)
        menu_jogo_forca()
        
    elif palavra_digitada == 'Sair':
        menu_jogo_forca()
    else:
        print('Não foi dessa vez!')
        forca_erros.append(palavra_digitada)
        menu_jogo_forca()

# comparar_palavras()

import random

lista_de_palavras = [
    'Abhorrent', 'Absence', 'Absorption', 'Accommodating', 'Accomplice', 'Acreage', 'Acrimonious', 'Actuarial', 'Adjournment', 'Adjudicate', 'Adjustment', 'Affiliation', 'Agastache', 'Aggregate', 'Alacrity', 'Algerian', 'Algorithm', 'Allergen', 'Alleviate', 'Allure', 'Altruistic', 'Amnesty', 'Anachronism', 'Anchoring', 'Anglers', 'Anodyne', 'Apartheid', 'Apocalyptic', 'Apprehend', 'Armageddon', 'Arthritis', 'Assumption', 'Asthma', 'Aversion', 'Avoidance', 'Azalea', 'Baccalaureate', 'Backgammon', 'Backstabbing', 'Balderdash', 'Balustrade', 'Banishment', 'Bequeath', 'Berated', 'Bereavement', 'Bewilderment', 'Bingeing', 'Blasphemous', 'Boisterous', 'Bondholder', 'Braggart', 'Breadth', 'Brinkmanship', 'Buddhist', 'Bureaucracy', 'Burglarize', 'Bustling', 'Camaraderie', 'Camouflage', 'Campaign', 'Capacious', 'Capricious', 'Cataclysm', 'Catastrophic', 'Cautioned', 'Chameleon', 'Chastisement', 'Chauvinism', 'Chicory', 'Circuitous', 'Circumstantial', 'Circumvent', 'Clairvoyant', 'Clumsy', 'Collard', 'Committee', 'Compassionate', 'Conceivably', 'Concise', 'Consciousness', 'Consumption', 'Contempt', 'Conversely', 'Corroborate', 'Craveable', 'Daffodil', 'Dalliance', 'Dalmatian', 'Dampened', 'Dastardly', 'Daunting', 'Deadlock', 'Decadence', 'Deceased', 'Decipher', 'Decluttering', 'Deflationary', 'Delphinium', 'Demographic', 'Demoralize', 'Dereliction', 'Desalination', 'Desensitize', 'Deterrence', 'Dichotomy', 'Diligently', 'Diminished', 'Disproportionate', 'Distillation', 'Downstream', 'Eloquently', 'Embodied', 'Emboldened', 'Enrollment', 'Entrepreneur', 'Equitable', 'Ethereal', 'Ethnography', 'Eucalyptus', 'Evacuee', 'Excerpt', 'Exoskeleton', 'Fallacy', 'Fatigued', 'Fattening', 'Fieldwork', 'Fluctuation', 'Forfeiting', 'Fragile', 'Frittered', 'Ghostly', 'Gingivitis', 'Gooseberry', 'Gratitude', 'Guaranteed', 'Hazelnut', 'Heartwarming', 'Heckled', 'Hideous', 'Hindered', 'Hodgepodge', 'Homeowner', 'Hostile', 'Hyacinth', 'Idiosyncrasy', 'Immobilize', 'Inaugural', 'Inducement', 'Inning', 'Inquiry', 'Interviewee', 'Invariably', 'Ironclad', 'Jaundice', 'Kohlrabi', 'Laceration', 'Lawsuit', 'Leisurely', 'Liability', 'Licensing', 'Looting', 'Luminous', 'Malignancy', 'Mammoth', 'Mangosteen', 'Matriarchal', 'Meerkat', 'Meteorologist', 'Moneyed', 'Mulling', 'Newsworthy', 'Niftiest', 'Nightingale', 'Nimble', 'Nonaccrual', 'Nonexistent', 'Oblivious', 'Oddity', 'Osteoporosis', 'Outlining', 'Overarching', 'Passivizing', 'Pathetically', 'Patroller', 'Patronizing', 'Peaceable', 'Peculiar', 'Perception', 'Periphery', 'Perpetrator', 'Philodendron', 'Phylum', 'Pomegranate', 'Posthumous', 'Procedural', 'Readership', 'Reassurance', 'Reinvigorate', 'Reprieve', 'Rescinded', 'Resourcefulness', 'Restitution', 'Rhetorical', 'Rhinoceros', 'Rookie', 'Roulette', 'Rustling', 'Scorching', 'Seasoned', 'Shallots', 'Shepherd', 'Sightings', 'Skepticism', 'Slaughterhouse', 'Sleuthing', 'Solely', 'Soothing', 'Southeast', 'Stalemate', 'Stampede', 'Subsiding', 'Succeeded', 'Successor', 'Succumb', 'Suppress', 'Synthesize', 'Systematicity', 'Tennessee', 'Thoroughness', 'Thriving', 'Toppled', 'Tournament', 'Transcend', 'Transdisciplinary', 'Trespass', 'Unacceptable', 'Unbiased', 'Unbowed', 'Undergraduate', 'Unforeseen', 'Unobtrusive', 'Unprecedented', 'Unpredictable', 'Unsettle', 'Viewership', 'Voracious', 'Weakened', 'Whether', 'Whirring', 'Whisperer'
    ]

palavras_acertadas = []
palavras_erradas = []

forca_acertos = []
forca_erros = []

####################### INICIANDO O PROGRAMA ##########################

inicio_do_programa()

menu_inicial()