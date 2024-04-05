class Candidato:
    def __init__(self, nome, nota_e, nota_t, nota_p, nota_s):
        self.nome = nome
        self.nota_e = nota_e
        self.nota_t = nota_t
        self.nota_p = nota_p
        self.nota_s = nota_s

def buscar_candidatos(lista_candidatos, nota_minima_e, nota_minima_t, nota_minima_p, nota_minima_s):
    candidatos_selecionados = []
    for candidato in lista_candidatos:
        if (candidato.nota_e >= nota_minima_e and
            candidato.nota_t >= nota_minima_t and
            candidato.nota_p >= nota_minima_p and
            candidato.nota_s >= nota_minima_s):
            candidatos_selecionados.append(candidato)
    return candidatos_selecionados

candidatos = [
    Candidato("Candidato 1", 5, 10, 8, 8),
    Candidato("Candidato 2", 10, 7, 7, 9),
    Candidato("Candidato 3", 8, 5, 4, 9),
    Candidato("Candidato 4", 2, 2, 2, 1),
    Candidato("Candidato 5", 10, 10, 8, 9)
]
nota_minima_e = int(input("Digite a nota mínima em Entrevista: "))
nota_minima_t = int(input("Digite a nota mínima em Teste Teórico: "))
nota_minima_p = int(input("Digite a nota mínima em Teste Prático: "))
nota_minima_s = int(input("Digite a nota mínima em Soft Skills: "))

candidatos_selecionados = buscar_candidatos(candidatos, nota_minima_e, nota_minima_t, nota_minima_p, nota_minima_s)

if len(candidatos_selecionados) > 0:
    print("Candidatos que atendem aos critérios:")
    for candidato in candidatos_selecionados:
        print(candidato.nome)

else:
    print(f'''
          Nenhum candidato atende aos critérios especificados.
           ''')
  
