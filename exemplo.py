while True:
    nota = input("Informe uma nota entre 0 e 10: ")
    try:
        nota = float(nota)
        if nota >= 0 and nota <= 10:
            print("Nota válida!")
            break
        else:
            print("Nota inválida, informe um valor entre 0 e 10.")
    except ValueError:
        print("Nota inválida, informe um valor numérico.")