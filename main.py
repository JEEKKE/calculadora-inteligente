import time
def somar(numero_a, numero_b):
    return numero_a + numero_b

def subtrair(numero_a, numero_b): 
    return numero_a - numero_b

def multiplicar(numero_a, numero_b):
    return numero_a * numero_b

def dividir(numero_a, numero_b):
  try:
      return numero_a / numero_b
  except ZeroDivisionError:
      return "Não é possivel dividir por zero"

def menu_inicial():
    historico = []
    while True:
        time.sleep(1.5)
        operacoes = ["somar", "subtrair", "multiplicar", "dividir"]
        print(operacoes, "--Sair--", "--Historico--")
        esc = input("Escolha a opição que vc deseja fazer:").strip().lower()
        if esc == "sair":
            break
        elif esc == "historico":
            print(historico)
        elif esc in operacoes: 
            
                while True:
                    try:
                        numero_a = float(input(f"Qual vai ser o primeiro numero ?").strip())  
                        numero_b = float(input(f"Qual vai ser o segundo numero ?").strip())  
                        if esc == "somar":
                            soma_feita= somar(numero_a, numero_b)
                            print(f"A soma do numero {numero_a} + {numero_b} = {soma_feita}")
                            hist = esc, numero_a,numero_b, soma_feita
                            historico.append(hist)
                        elif esc == "subtrair":
                            subtrair_feito = subtrair(numero_a, numero_b)
                            print(f"A subtração do numero {numero_a} - {numero_b} = {subtrair_feito}")
                            hist = esc, numero_a,numero_b, subtrair_feito
                            historico.append(hist)
                        elif esc == "multiplicar":
                            multiplicar_feito = multiplicar(numero_a, numero_b)
                            print(f"A multiplicação do numero {numero_a} * {numero_b} = {multiplicar_feito}")
                            hist = esc, numero_a,numero_b, multiplicar_feito
                            historico.append(hist)
                        elif esc == "dividir":
                            dividir_feito = dividir(numero_a, numero_b)
                            if type(dividir_feito) != str:
                                print(f"A divisão do numero {numero_a} / {numero_b} = {dividir_feito}")
                                hist = esc, numero_a,numero_b, dividir_feito
                                historico.append(hist)
                            else:
                                print(dividir_feito)
                        break        
                    except ValueError:
                        print("Vc digitou um valor invalido")
                        continue
        else:
            print(f"Descupe a opição {esc} não é valida")
        
menu_inicial()





 
