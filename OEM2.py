h = 6.626e-34  
c = 3e8  
me = 9.109e-31  
e = 1.602e-19  
epsilon_0 = 8.854e-12  
pi = 3.1416  


print("***** ATOMO DE BOHR E QUANTIZAÇÃO COM PYTHON *****")
print("\nIntegrantes do grupo: Gustavo Bertoluzzi Cardoso e Isabella Vieira Silva Rosseto")
print("\nEste programa estuda o modelo de Bohr para o átomo de hidrogênio. Os cálculos incluem raio da órbita, velocidade, comprimento de onda de De Broglie do elétron, energia cinética, potencial e total. Todas as entradas e saídas são tratadas com precisão de quatro algarismos significativos, e os resultados são apresentados com notação científica quando apropriado.")

def mostrar_menu():
    print("\n***** MENU *****")
    print("1. Calcular propriedades para um número quântico específico (n)")
    print("2. Calcular a diferença de energia, frequência e comprimento de onda do fóton entre dois níveis quânticos")
    print("3. Calcular n final ou inicial dado (n inicial ou n final) e (frequência ou comprimento de onda do fóton absorvido)")
    print("4. Calcular n final ou inicial dado (n inicial ou n final) e (frequência ou comprimento de onda do fóton emitido)")
    print("5. Calcular Efóton, ffóton, e λfóton dado Efóton em [J] ou [eV], ou vice-versa")
    print("0. Sair")


mostrar_menu()

def calcular_tudo_por_n(n):
    rn = calcular_raio(n)
    vn = calcular_velocidade(n)
    lambda_n = calcular_comprimento_onda(n, vn)
    kn = calcular_energia_cinetica(vn)
    un = calcular_energia_potencial(rn)
    en = calcular_energia_total(kn, un)
    return rn, vn, lambda_n, kn, un, en

def calcular_efoton_por_ffoton_lambda(ffoton=None, lambda_foton=None):
    if ffoton is not None:
        Efoton = calcular_Efóton_dado_foton(ffóton=ffoton)
    elif lambda_foton is not None:
        Efoton = calcular_Efóton_dado_foton(λfóton=lambda_foton)
    Efoton_ev = energia_joules_para_ev(Efoton)
    return Efoton, Efoton_ev


def calcular_ffoton_lambdafoton_por_efoton(Efoton_j=None, Efoton_ev=None):
    if Efoton_ev is not None:
        Efoton_j = Efoton_ev * e
    ffoton = calcular_frequencia_foton(Efoton_j)
    lambda_foton = calcular_comprimento_onda_foton(Efoton_j)
    return ffoton, lambda_foton


rn, vn, lambda_n, kn, un, en = calcular_tudo_por_n(2)


Efoton, Efoton_ev = calcular_efoton_por_ffoton_lambda(ffoton=5e14)


ffoton_test, lambda_foton_test = calcular_ffoton_lambdafoton_por_efoton(Efoton_j=3.027e-19)

print("\n***** RESULTADOS DOS TESTES *****")
print(f"\nFunção 1 - n=2: rn={rn:.3e} m, vn={vn:.3e} m/s, λn={lambda_n:.3e} m, Kn={kn:.3e} J, Un={un:.3e} J, En={en:.3e} J")
print(f"Função 5A - Efóton: {Efoton:.3e} J ({Efoton_ev:.3e} eV)")
print(f"Função 5B - ffóton: {ffoton_test:.3e} Hz, λfóton: {lambda_foton_test:.3e} m")

def executar_programa():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            n = int(input("Digite o valor de n: "))
            resultados = calcular_tudo_por_n(n)
            print("\n***** RESULTADOS *****")
            print(f"\n[=] Raio da órbita (rn): {resultados[0]:.3e} m")
            print(f"[=] Velocidade (vn): {resultados[1]:.3e} m/s")
            print(f"[=] Comprimento de onda de De Broglie (λn): {resultados[2]:.3e} m")
            print(f"[=] Energia cinética (Kn): {resultados[3]:.3e} J")
            print(f"[=] Energia potencial (Un): {resultados[4]:.3e} J")
            print(f"[=] Energia total (En): {resultados[5]:.3e} J")

        elif escolha == "2":
            n_inicial = int(input("Digite o valor de n inicial: "))
            n_final = int(input("Digite o valor de n final: "))
            Efóton, Efóton_ev, ffóton, λfóton = calcular_diferenca_energia_frequencia_comprimento(n_inicial, n_final)
            print("\n***** RESULTADOS *****")
            print(f"\n[=] Energia do fóton: {Efóton:.3e} J ({Efóton_ev:.3e} eV)")
            print(f"[=] Frequência do fóton: {ffóton:.3e} Hz")
            print(f"[=] Comprimento de onda do fóton: {λfóton:.3e} m")

        elif escolha == "3":
            # Esta opção requer uma implementação mais detalhada para lidar com os diferentes casos de entrada
            pass

        elif escolha == "4":
            # Similar à opção 3, requer detalhamento adicional
            pass

        elif escolha == "5":
            escolha_5 = input("Digite 'A' para calcular Efóton por ffóton ou λfóton, ou 'B' para calcular ffóton e λfóton por Efóton: ").upper()
            if escolha_5 == "A":
                ffoton = float(input("Digite o valor de ffóton (Hz), ou deixe em branco se não souber: ") or "0")
                lambda_foton = float(input("Digite o valor de λfóton (m), ou deixe em branco se não souber: ") or "0")
                Efoton, Efoton_ev = calcular_efoton_por_ffoton_lambda(ffoton or None, lambda_foton or None)
                print("\n***** RESULTADOS *****")
                print(f"\n[=] Efóton: {Efoton:.3e} J ({Efoton_ev:.3e} eV)")
            elif escolha_5 == "B":
                Efoton_j = float(input("Digite o valor de Efóton em [J], ou deixe em branco se não souber: ") or "0")
                Efoton_ev = float(input("Digite o valor de Efóton em [eV], ou deixe em branco se não souber: ") or "0")
                ffoton, lambda_foton = calcular_ffoton_lambdafoton_por_efoton(Efoton_j or None, Efoton_ev or None)
                print("\n***** RESULTADOS *****")
                print(f"\n[=] ffóton: {ffoton:.3e} Hz")
                print(f"[=] λfóton: {lambda_foton:.3e} m")

        elif escolha == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida, por favor escolha novamente.")

