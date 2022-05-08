from string import ascii_letters

#extraido de dracula.txt pois é um dos classicos da lingua inglesa
freq = {'a': 0.09506781179805297,
        'b': 0.005289345777622818,
        'c': 0.01055936208367327,
        'd': 0.03333677373613521,
        'e': 0.21600720952818947,
        'f': 0.01101743408923724,
        'g': 0.009051663301028802,
        'h': 0.06612138105792022,
        'i': 0.05488402864117097,
        'j': 0.00018709469654006107,
        'k': 0.003369528072775096,
        'l': 0.030770330501140256,
        'm': 0.014662315955165837,
        'n': 0.07023564084674756,
        'o': 0.09388141989192272,
        'p': 0.0061132189150185255,
        'q': 0.00021408301533921216,
        'r': 0.049202258119928066,
        's': 0.058431169028205346,
        't': 0.11749546942715834,
        'u': 0.016109838081028414,
        'v': 0.0029544914944854474,
        'w': 0.01494824625163252,
        'x': 0.0003183892204278232,
        'y': 0.00933358182037669,
        'z': 0.00013238864492016016,
        'A': 0.0006269313515640643,
        'B': 0.00019548295778844585,
        'C': 0.0002625890477755243,
        'D': 0.0002976009208122609,
        'E': 0.00040993068013845735,
        'F': 0.00010685915416420641,
        'G': 0.00023341248691157715,
        'H': 0.000714825741166705,
        'I': 0.0032768924920320635,
        'J': 0.00017980055632407427,
        'K': 2.698831879915111e-05,
        'L': 0.00032495394662221134,
        'M': 0.0005171545413134632,
        'N': 0.00024362428321395864,
        'O': 0.00023523602196557386,
        'P': 0.0002155418433824095,
        'Q': 3.537658004753591e-05,
        'R': 0.00031145978722263575,
        'S': 0.0004340013428512138,
        'T': 0.0008326261056548916,
        'U': 7.950612835425597e-05,
        'V': 0.0001615652057841073,
        'W': 0.00040300124693326995,
        'X': 3.4647166025937236e-05,
        'Y': 0.0001436945622549397,
        'Z': 1.8235350539966965e-06
}

#funçao intermediária para conseguir os scores de plaintext armazenados acima na variável "freq" obtidos a partir do livro dracula (dracula.txt)
def frequency(txt: str):
    with open(txt, 'r', encoding='utf-8') as book:
        new_lines = list(filter(lambda x: (x != '\n'), book.readlines()))
        results = {}
        for letter in ascii_letters:
            results[letter] = 0

        for line in new_lines:
            for letter in line:
                if letter in ascii_letters:                
                    old_value = results[letter]
                    results[letter] = line.count(letter) + old_value
        n = sum(results.values())
    return {l: results[l] / n for l in results}

#dada uma string, retorna o seu score a partir dos dados de score plain text da variavel "freq" (quando menor, melhor)
def score(text: str):
    error = 0.0
    for letter, f in freq.items():        
        letter_f_str = text.count(bytes(letter, 'utf-8'))/len(text)
        error +=  abs(f - letter_f_str)

    return error
    


