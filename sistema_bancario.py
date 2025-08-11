menu = """ 
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
Limite_saques = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Por gentileza, informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nDepósito realizado com sucesso!")
        else:
            print("A operação falhou! O valor informado é inválido.")
            
    elif opcao == "2":
        valor = float(input("Por gentileza, digite o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= Limite_saques
        
        # A lógica para o saque precisa ser um único bloco if/elif/else
        # com todas as condições de erro verificadas na ordem certa.
        # O saque só é realizado se nenhuma das condições for verdadeira.
        if excedeu_saldo:
            print("A operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("A operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("A operação falhou! Número máximo de saques diários atingido.")
        elif valor <= 0:
            # Esta verificação garante que o valor do saque seja positivo.
            print("A operação falhou! O valor informado é inválido.")
        else:
            # Apenas se todas as condições acima forem falsas, o saque é processado.
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
            
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        # Melhoria para exibir o saldo mesmo que não haja movimentações.
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    elif opcao == "4":
        break
        
    else:
        # Este 'else' está no loop 'while', não no bloco 'if' anterior.
        # Ele só é executado se nenhuma das opções válidas for selecionada.
        print("Opção inválida, por gentileza, retorne ao menu e selecione a opção desejada.")
