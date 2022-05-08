import single_xor

def getCipherEachLine(txt:str):
    with open(txt, 'r', encoding='utf-8') as file:
        counter = 0     
        for line in file.readlines():
            counter += 1
            #listar apenas o "chunk" escondido
            if counter == 171:
                single_xor.crack_cipher(line.replace('\n',''))