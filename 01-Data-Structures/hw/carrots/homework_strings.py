""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""

# read the file dna.fasta
dna = open("./files/dna.fasta")
dna_dict = {}
rna_dict = {}
lines = dna.read().splitlines()
dna.close()
dna_name = "1"
fasta_seq = ""
for line in lines:
    if line[0] == ">":
        dna_dict.update({dna_name: fasta_seq})
        dna_name = line[1:]
        fasta_seq = ""
    else:
        fasta_seq += line
dna_dict.update({dna_name: fasta_seq})
dna_dict.pop("1")

def translate_from_dna_to_rna(dna):
    for key in dna:
        rna_seq = dna[key].replace('T', 'U')
        rna_dict.update({key: rna_seq})
    rna = ""
    for key in rna_dict:
        rna += str(key) + ":" + str(rna_dict[key]) + "\n"
    return rna

with open('translate_from_dna_to_rna.txt', 'tw') as out:
    print(translate_from_dna_to_rna(dna_dict), file = out)   

def count_nucleotides(dna):
    a = 0
    c = 0
    g = 0
    t = 0
    for key in dna:
       c += dna[key].count("C")
       a += dna[key].count("A")
       g += dna[key].count("G")
       t += dna[key].count("T")
    num_of_nucleotides = "A: " + str(a) + "\nC: " + str(c) + "\nG: " + str(g) + "\nT: " + str(t)
    return num_of_nucleotides
   
with open('count_nucleotides.txt', 'tw') as out:
    print(count_nucleotides(dna_dict), file = out)


def translate_rna_to_protein(rna):
    codon_table = {}
    a = []
    rna_seq = "1"
    codon = ""
    with open("./files/rna_codon_table.txt") as codons:
        lines = codons.read().splitlines()
        for line in lines:
            a += line.split()
        for item in a:
            if (a.index(item) % 2 == 0): 
                codon_table.update({rna_seq: codon})
                rna_seq = item
            else:
                codon_table.update({rna_seq: codon})
                codon = item
    codon_table.pop("1")
    protein = ""
    for key in rna:
        if len(rna[key])%3 == 0:
            protein += key + ": "
            for i in range(0, len(rna[key]), 3): 
                codon = rna[key][i:i + 3] 
                protein += codon_table[codon]
            protein += "\n"
        else: 
            protein = key + ": "
            for i in range(0, len(rna[key]) - len(rna[key])%3, 3): 
                codon = rna[key][i:i + 3] 
                protein += codon_table[codon]
            protein += "\n"
    return protein

with open('translate_rna_to_protein.txt', 'tw') as out:
    print(translate_rna_to_protein(rna_dict), file = out)
