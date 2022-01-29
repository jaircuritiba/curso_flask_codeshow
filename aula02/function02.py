def imprimirNotaAluno(nome, turma, nota, materia, verificarMedia=False):
    print(f"O aluno {nome}, da turma {turma}, obteve a nota {nota} na matéria de {materia}")
    if verificarMedia:
        if(nota >= 7):
            print("Nota acima da média. Continue assim!")
        else:
            print("Nota inferior a média escolar. Estude um pouco mais!")


# primeira opção
boletim = ['João', '5ºA', 8.0, 'História']

name, team, note, discipline = boletim
imprimirNotaAluno(name, team, note, discipline)
imprimirNotaAluno(name, team, note, discipline, True)

# segunda opção
boletim = ['Pedro', '6ºB', 6.8, 'Português']

imprimirNotaAluno(*boletim, True)

# terceira opção
boletim = {
    "nome" : "Francisco",
    "turma" : "7ºD",
    "nota":"100",
    "materia" : "Matemática"
}

imprimirNotaAluno(**boletim)


