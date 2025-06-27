import random

lista_de_palavras = ['Abhorrent', 'Absence', 'Absorption', 'Accommodating', 'Accomplice', 'Acreage', 'Acrimonious', 'Actuarial', 'Adjournment', 'Adjudicate', 'Adjustment', 'Affiliation', 'Agastache', 'Aggregate', 'Alacrity', 'Algerian', 'Algorithm', 'Allergen', 'Alleviate', 'Allure', 'Altruistic', 'Amnesty', 'Anachronism', 'Anchoring', 'Anglers', 'Anodyne', 'Apartheid', 'Apocalyptic', 'Apprehend', 'Armageddon', 'Arthritis', 'Assumption', 'Asthma', 'Aversion', 'Avoidance', 'Azalea', 'Baccalaureate', 'Backgammon', 'Backstabbing', 'Balderdash', 'Balustrade', 'Banishment', 'Bequeath', 'Berated', 'Bereavement', 'Bewilderment', 'Bingeing', 'Blasphemous', 'Boisterous', 'Bondholder', 'Braggart', 'Breadth', 'Brinkmanship', 'Buddhist', 'Bureaucracy', 'Burglarize', 'Bustling', 'Camaraderie', 'Camouflage', 'Campaign', 'Capacious', 'Capricious', 'Cataclysm', 'Catastrophic', 'Cautioned', 'Chameleon', 'Chastisement', 'Chauvinism', 'Chicory', 'Circuitous', 'Circumstantial', 'Circumvent', 'Clairvoyant', 'Clumsy', 'Collard', 'Committee', 'Compassionate', 'Conceivably', 'Concise', 'Consciousness', 'Consumption', 'Contempt', 'Conversely', 'Corroborate', 'Craveable', 'Daffodil', 'Dalliance', 'Dalmatian', 'Dampened', 'Dastardly', 'Daunting', 'Deadlock', 'Decadence', 'Deceased', 'Decipher', 'Decluttering', 'Deflationary', 'Delphinium', 'Demographic', 'Demoralize', 'Dereliction', 'Desalination', 'Desensitize', 'Deterrence', 'Dichotomy', 'Diligently', 'Diminished', 'Disproportionate', 'Distillation', 'Downstream', 'Eloquently', 'Embodied', 'Emboldened', 'Enrollment', 'Entrepreneur', 'Equitable', 'Ethereal', 'Ethnography', 'Eucalyptus', 'Evacuee', 'Excerpt', 'Exoskeleton', 'Fallacy', 'Fatigued', 'Fattening', 'Fieldwork', 'Fluctuation', 'Forfeiting', 'Fragile', 'Frittered', 'Ghostly', 'Gingivitis', 'Gooseberry', 'Gratitude', 'Guaranteed', 'Hazelnut', 'Heartwarming', 'Heckled', 'Hideous', 'Hindered', 'Hodgepodge', 'Homeowner', 'Hostile', 'Hyacinth', 'Idiosyncrasy', 'Immobilize', 'Inaugural', 'Inducement', 'Inning', 'Inquiry', 'Interviewee', 'Invariably', 'Ironclad', 'Jaundice', 'Kohlrabi', 'Laceration', 'Lawsuit', 'Leisurely', 'Liability', 'Licensing', 'Looting', 'Luminous', 'Malignancy', 'Mammoth', 'Mangosteen', 'Matriarchal', 'Meerkat', 'Meteorologist', 'Moneyed', 'Mulling', 'Newsworthy', 'Niftiest', 'Nightingale', 'Nimble', 'Nonaccrual', 'Nonexistent', 'Oblivious', 'Oddity', 'Osteoporosis', 'Outlining', 'Overarching', 'Passivizing', 'Pathetically', 'Patroller', 'Patronizing', 'Peaceable', 'Peculiar', 'Perception', 'Periphery', 'Perpetrator', 'Philodendron', 'Phylum', 'Pomegranate', 'Posthumous', 'Procedural', 'Readership', 'Reassurance', 'Reinvigorate', 'Reprieve', 'Rescinded', 'Resourcefulness', 'Restitution', 'Rhetorical', 'Rhinoceros', 'Rookie', 'Roulette', 'Rustling', 'Scorching', 'Seasoned', 'Shallots', 'Shepherd', 'Sightings', 'Skepticism', 'Slaughterhouse', 'Sleuthing', 'Solely', 'Soothing', 'Southeast', 'Stalemate', 'Stampede', 'Subsiding', 'Succeeded', 'Successor', 'Succumb', 'Suppress', 'Synthesize', 'Systematicity', 'Tennessee', 'Thoroughness', 'Thriving', 'Toppled', 'Tournament', 'Transcend', 'Transdisciplinary', 'Trespass', 'Unacceptable', 'Unbiased', 'Unbowed', 'Undergraduate', 'Unforeseen', 'Unobtrusive', 'Unprecedented', 'Unpredictable', 'Unsettle', 'Viewership', 'Voracious', 'Weakened', 'Whether', 'Whirring', 'Whisperer']

palavras_acertadas = []
palavras_erradas = []

sorteio_palavras_acertadas = []

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


# sortear_palavra()

### jogo de adivinhar palavra 

### Imprimir quantidade letras forca 


def imprimir_forca(palavra_da_forca): 
    
    print(f'A palavra sorteada tem {len(palavra_da_forca)} letras: {"".join(tentativa)}')

### Digitar palavra para descobrir se é a da forca

def input_forca():
    palavra_digitada = input('Faça uma tentativa: ').capitalize()
    return palavra_digitada

### tentativa da forca

def tentativa_forca():
    
    tentativa = []

    palavra_da_forca = sortear_palavra()

    print(str("".join(palavra_da_forca))) ########## apenas pra eu tentar a palavra

    imprimir_forca(palavra_da_forca)
    input()

    palavra_digitada = input_forca()
    print(palavra_digitada)

    lista_palavra_da_forca = list(palavra_da_forca)
    lista_palavra_digitada = list(palavra_digitada)
    print(lista_palavra_digitada)
    print(lista_palavra_da_forca)

    for letra in lista_palavra_digitada:
        for letra in lista_palavra_da_forca and letra not in tentativa:
            tentativa.append(letra)
    
        for letra in not lista_palavra_da_forca and letra not in tentativa:
            tentativa.append('_ ')

    ########## Conferindo se a palavra está correta

    if palavra_digitada == palavra_da_forca:
        tentativa_acertada = str("".join(palavra_da_forca)).upper()
        print(f'''
Parabéns! Você acertou a palavra!
{tentativa_acertada}
''')
        
#    elif palavra_digitada == '0':
#        print('Poxa que pena!')


    elif palavra_digitada != palavra_da_forca:
            # palavra_digitada != str(tentativa)
                
            print(str(tentativa))
            palavra_digitada = input_forca()
        
tentativa_forca()


