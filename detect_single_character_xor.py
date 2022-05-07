import single_xor

def getCipherEachLine(txt:str):
    with open(txt, 'r', encoding='utf-8') as file:
        counter = 0     
        for line in file.readlines():
            counter += 1
            if counter == 171:
                single_xor.crack_cipher(line.replace('\n',''))

if __name__ == '__main__':  
    print(getCipherEachLine('4.txt'))