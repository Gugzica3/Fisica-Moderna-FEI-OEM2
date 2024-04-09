h1 = 6.626e-34  
c = 3e8  
m_eletron = 9.11e-31  
e = 1.602e-19  
epsilon_0 = 8.854e-12  
pi = 3.1416
velocidade = 2.187e6  


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


def calcular_tudo_por_n(n):
    raio_orbita = (n*n) * 5.29e-11
    raio_orbita_nm = raio_orbita * 1e9
    velocidade_eletron = velocidade / n
    energia_cinetica = 13.6 / (n*n)
    energia_potencial = -27.2 / (n*n)
    energia_total = energia_cinetica * (-1)
    comprimento_onda = h1 / (m_eletron * velocidade_eletron)
    comprimento_onda_nm = comprimento_onda * 1e9
    return {
        "raio_orbita": raio_orbita,
        "raio_orbita_nm": raio_orbita_nm,
        "velocidade_eletron": velocidade_eletron,
        "energia_cinetica": energia_cinetica,
        "energia_potencial": energia_potencial,
        "energia_total": energia_total,
        "comprimento_onda": comprimento_onda,
        "comprimento_onda_nm": comprimento_onda_nm
    }
    
            
def propriedades(n_inicial,n_final):
        
        Energia_n1 = -13.6 / n_inicial ** 2
        Energia_n2 = -13.6 / n_final ** 2
        
        Energia_abs = Energia_n2 - Energia_n1
        Energia_abs_J = Energia_abs * 1.60218e-19
        Energia_emt = Energia_n1 - Energia_n2
        Energia_emt_J = Energia_emt * 1.60218e-19
        

        comprimento = ((h1 * c) / Energia_emt_J)
        comprimento_nm = comprimento * 1e9

        frequencia = c / comprimento
        frequencia_THz = frequencia / 1e12
        
        return{
            "energia absorvida":Energia_abs,
            "energia absorvida jaules":Energia_abs_J,
            "energia emitida":Energia_emt,
            "energia emitida jaules":Energia_emt_J,
            "comprimento foton":comprimento,
            "comprimento foton nm":comprimento_nm,
            "frequencia":frequencia,
            "frequencia THZ":frequencia_THz
        }


def executar_programa():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            n = int(input("Digite o valor de n: "))
            resultados = calcular_tudo_por_n(n)
            print("\n***** RESULTADOS *****")
            print(f"[=] Raio da órbita (rn): {resultados['raio_orbita']:.3e} m")
            print(f"[=] Raio da órbita (rn): {resultados['raio_orbita_nm']:.3e} nm")
            print(f"[=] Velocidade (vn): {resultados['velocidade_eletron']:.3e} m/s")
            print(f"[=] Comprimento de onda de De Broglie (λn): {resultados['comprimento_onda']:.3e} m")
            print(f"[=] Comprimento de onda de De Broglie (λn): {resultados['comprimento_onda_nm']:.3e} nm")
            print(f"[=] Energia cinética (Kn): {resultados['energia_cinetica']:.3e} Ev")
            print(f"[=] Energia potencial (Un): {resultados['energia_potencial']:.3e} Ev")
            print(f"[=] Energia total (En): {resultados['energia_total']:.3e} J")

        elif escolha == "2":
            n_inicial = int(input("Digite o valor de n inicial: "))
            n_final = int(input("Digite o valor de n final: "))
            resultados = propriedades(n_inicial,n_final)
            print("\n***** RESULTADOS *****")
            print(f"[=] Energia emitida do fóton: {resultados['energia emitida jaules']:.3e} J ({resultados['energia emitida']:.3e} eV)")
            print(f"[=] Energia absorvida do fóton: {resultados['energia absorvida jaules']:.3e} J ({resultados['energia absorvida']:.3e} eV)")
            print(f"[=] Frequência do fóton: {resultados['frequencia']:.3e} Hz {resultados['frequencia THZ']:.3e} THZ")
            print(f"[=] Comprimento de onda do fóton: {resultados['comprimento foton']:.3e} m {resultados['comprimento foton nm']:.3e} nm")

        elif escolha == "3":
            n_inicial = input("Digite o valor de n inicial (deixe em branco se desconhecido): ").strip()
            n_final = input("Digite o valor de n final (deixe em branco se desconhecido): ").strip()
            ffoton = input("Digite o valor de ffóton (Hz), ou deixe em branco: ").strip()
            lambda_foton = input("Digite o valor de λfóton (m), ou deixe em branco: ").strip()

            n_inicial = int(n_inicial) if n_inicial else None
            n_final = int(n_final) if n_final else None
            ffoton = float(ffoton) if ffoton else None
            lambda_foton = float(lambda_foton) if lambda_foton else None

           
            resultado = calcular_n_transicao_absorvido(n_inicial=n_inicial, n_final=n_final, ffoton=ffoton, lambda_foton=lambda_foton)
            print("\n***** RESULTADOS *****")
            if n_inicial is None:
                print(f"[=] n inicial calculado: {resultado:.2f}")
            else:
                print(f"[=] n final calculado: {resultado:.2f}")

        elif escolha == "4":
            n_inicial = input("Digite o valor de n inicial (deixe em branco se desconhecido): ").strip()
            n_final = input("Digite o valor de n final (deixe em branco se desconhecido): ").strip()
            ffoton = input("Digite o valor de ffóton (Hz), ou deixe em branco: ").strip()
            lambda_foton = input("Digite o valor de λfóton (m), ou deixe em branco: ").strip()

            n_inicial = int(n_inicial) if n_inicial else None
            n_final = int(n_final) if n_final else None
            ffoton = float(ffoton) if ffoton else None
            lambda_foton = float(lambda_foton) if lambda_foton else None

            
            resultado = calcular_n_transicao_emitido(n_inicial=n_inicial, n_final=n_final, ffoton=ffoton, lambda_foton=lambda_foton)
            print("\n***** RESULTADOS *****")
            if n_inicial is None:
                print(f"[=] n inicial calculado: {resultado:.2f}")
            else:
                print(f"[=] n final calculado: {resultado:.2f}")
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
executar_programa()


