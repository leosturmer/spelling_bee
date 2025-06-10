lista_de_palavras = ['Abhorrent', 'Absence', 'Absorption', 'Accommodating', 'Accomplice', 'Acreage', 'Acrimonious', 'Actuarial', 'Adjournment', 'Adjudicate', 'Adjustment', 'Affiliation', 'Agastache', 'Aggregate', 'Alacrity', 'Algerian', 'Algorithm', 'Allergen', 'Alleviate', 'Allure', 'Altruistic', 'Amnesty', 'Anachronism', 'Anchoring', 'Anglers', 'Anodyne', 'Apartheid', 'Apocalyptic', 'Apprehend', 'Armageddon', 'Arthritis', 'Assumption', 'Asthma', 'Aversion', 'Avoidance', 'Azalea', 'Baccalaureate', 'Backgammon', 'Backstabbing', 'Balderdash', 'Balustrade', 'Banishment', 'Bequeath', 'Berated', 'Bereavement', 'Bewilderment', 'Bingeing', 'Blasphemous', 'Boisterous', 'Bondholder', 'Braggart', 'Breadth', 'Brinkmanship', 'Buddhist', 'Bureaucracy', 'Burglarize', 'Bustling', 'Camaraderie', 'Camouflage', 'Campaign', 'Capacious', 'Capricious', 'Cataclysm', 'Catastrophic', 'Cautioned', 'Chameleon', 'Chastisement', 'Chauvinism', 'Chicory', 'Circuitous', 'Circumstantial', 'Circumvent', 'Clairvoyant', 'Clumsy', 'Collard', 'Committee', 'Compassionate', 'Conceivably', 'Concise', 'Consciousness', 'Consumption', 'Contempt', 'Conversely', 'Corroborate', 'Craveable', 'Daffodil', 'Dalliance', 'Dalmatian', 'Dampened', 'Dastardly', 'Daunting', 'Deadlock', 'Decadence', 'Deceased', 'Decipher', 'Decluttering', 'Deflationary', 'Delphinium', 'Demographic', 'Demoralize', 'Dereliction', 'Desalination', 'Desensitize', 'Deterrence', 'Dichotomy', 'Diligently', 'Diminished', 'Disproportionate', 'Distillation', 'Downstream', 'Eloquently', 'Embodied', 'Emboldened', 'Enrollment', 'Entrepreneur', 'Equitable', 'Ethereal', 'Ethnography', 'Eucalyptus', 'Evacuee', 'Excerpt', 'Exoskeleton', 'Fallacy', 'Fatigued', 'Fattening', 'Fieldwork', 'Fluctuation', 'Forfeiting', 'Fragile', 'Frittered', 'Ghostly', 'Gingivitis', 'Gooseberry', 'Gratitude', 'Guaranteed', 'Hazelnut', 'Heartwarming', 'Heckled', 'Hideous', 'Hindered', 'Hodgepodge', 'Homeowner', 'Hostile', 'Hyacinth', 'Idiosyncrasy', 'Immobilize', 'Inaugural', 'Inducement', 'Inning', 'Inquiry', 'Interviewee', 'Invariably', 'Ironclad', 'Jaundice', 'Kohlrabi', 'Laceration', 'Lawsuit', 'Leisurely', 'Liability', 'Licensing', 'Looting', 'Luminous', 'Malignancy', 'Mammoth', 'Mangosteen', 'Matriarchal', 'Meerkat', 'Meteorologist', 'Moneyed', 'Mulling', 'Newsworthy', 'Niftiest', 'Nightingale', 'Nimble', 'Nonaccrual', 'Nonexistent', 'Oblivious', 'Oddity', 'Osteoporosis', 'Outlining', 'Overarching', 'Passivizing', 'Pathetically', 'Patroller', 'Patronizing', 'Peaceable', 'Peculiar', 'Perception', 'Periphery', 'Perpetrator', 'Philodendron', 'Phylum', 'Pomegranate', 'Posthumous', 'Procedural', 'Readership', 'Reassurance', 'Reinvigorate', 'Reprieve', 'Rescinded', 'Resourcefulness', 'Restitution', 'Rhetorical', 'Rhinoceros', 'Rookie', 'Roulette', 'Rustling', 'Scorching', 'Seasoned', 'Shallots', 'Shepherd', 'Sightings', 'Skepticism', 'Slaughterhouse', 'Sleuthing', 'Solely', 'Soothing', 'Southeast', 'Stalemate', 'Stampede', 'Subsiding', 'Succeeded', 'Successor', 'Succumb', 'Suppress', 'Synthesize', 'Systematicity', 'Tennessee', 'Thoroughness', 'Thriving', 'Toppled', 'Tournament', 'Transcend', 'Transdisciplinary', 'Trespass', 'Unacceptable', 'Unbiased', 'Unbowed', 'Undergraduate', 'Unforeseen', 'Unobtrusive', 'Unprecedented', 'Unpredictable', 'Unsettle', 'Viewership', 'Voracious', 'Weakened', 'Whether', 'Whirring', 'Whisperer']

palavras_acertadas = []
palavras_erradas = []

quantidade_acertada = 0
quantidade_erradas = 0

def menu_inicial():
    imprimir_menu_inicial()
        
    opcao_menu_inicial = input('Digite a opção desejada: ')

    consultar = {
        "1" : menu,
        '2' : jogo,
        '3' : encerrar_programa
    }

    consultar[opcao_menu_inicial]()

def menu_jogo():
    print('''
------- Jogo Spelling Bee --------

Como funciona:
    - Digite uma palavra
    - Se a palavra constar na lista, você acerta
    - Se não estiver, você pode tentar novamente
    - Ao final, você pode conferir quantas palavras acertou
          e quais foram as palavras que errou.

-----------------------------------------

          ''')


def jogo():
    palavra_digitada = input('Qual palavra deseja adivinhar? ')

    if palavra_digitada in lista_de_palavras:
        print(f'Parabéns! {palavra_digitada} está correto! :)')
        palavras_acertadas.append(palavra_digitada)
        quantidade_acertada +=1
    else: 
        print(f'Poxa vida! {palavra_digitada} não está correta :(')
        palavras_erradas.append(palavra_digitada)
        quantidade_erradas += 1


# Controller

def menu():
    imprimir_menu()    
    item_menu = int(input("Digite a opção escolhida: "))

    while item_menu != 5:
        match item_menu:
            case 1:
                filtro_quant_letras()
            case 2:
                filtro_min_letras()
            case 3:
                filtro_letra()
            case 4:
                menu_inicial()
        break

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

def imprimir_menu():
    print(f'''          
------------ Menu de opções -------------
          
       1 - Filtrar palavras pela quantidade total de letras
       2 - Filtrar palavras pela quantidade mínima de letras
       3 - Filtrar palavras por alguma letra ou conjunto de letras
       4 - Voltar ao menu inicial
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





####################### INICIANDO O PROGRAMA

inicio_do_programa()

menu_inicial()
