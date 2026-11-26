#Aqui vou desenvolver meu código de teste para a revisão.
# Lista global (array) para armazenar os motores em memória
motores = []
proximo_id = 1


def cadastrar_motor():
    global proximo_id
    print("\n--- CADASTRAR NOVO MOTOR ---")
    modelo = input("Modelo do motor: ").strip()
    fabricante = input("Fabricante: ").strip()
    tipo = input("Tipo (Elétrico, Combustão, Híbrido, etc.): ").strip()
    
    # Validação simples para garantir que potência seja um número
    while True:
        try:
            potencia_cv = float(input("Potência (em CV): "))
            break
        except ValueError:
            print("Erro: Digite um valor numérico válido para a potência.")

    motor = {
        "id": proximo_id,
        "modelo": modelo,
        "fabricante": fabricante,
        "tipo": tipo,
        "potencia_cv": potencia_cv
    }
    
    motores.append(motor)
    proximo_id += 1
    print(f"\n[SUCESSO] Motor '{modelo}' cadastrado com ID {motor['id']}!")


def listar_motores():
    print("\n--- LISTA DE MOTORES CADASTRADOS ---")
    if not motores:
        print("Nenhum motor cadastrado no momento.")
        return

    for m in motores:
        print(
            f"ID: {m['id']} | Modelo: {m['modelo']} | "
            f"Fabricante: {m['fabricante']} | Tipo: {m['tipo']} | "
            f"Potência: {m['potencia_cv']} CV"
        )


def buscar_motor_por_id(id_busca):
    for motor in motores:
        if motor["id"] == id_busca:
            return motor
    return None


def atualizar_motor():
    print("\n--- ATUALIZAR MOTOR ---")
    listar_motores()
    if not motores:
        return

    try:
        id_busca = int(input("\nDigite o ID do motor que deseja atualizar: "))
    except ValueError:
        print("Erro: ID inválido.")
        return

    motor = buscar_motor_por_id(id_busca)
    if not motor:
        print("Motor não encontrado.")
        return

    print(f"\nEditando motor '{motor['modelo']}' (pressione Enter para manter o valor atual):")
    
    novo_modelo = input(f"Modelo [{motor['modelo']}]: ").strip()
    if novo_modelo:
        motor["modelo"] = novo_modelo

    novo_fabricante = input(f"Fabricante [{motor['fabricante']}]: ").strip()
    if novo_fabricante:
        motor["fabricante"] = novo_fabricante

    novo_tipo = input(f"Tipo [{motor['tipo']}]: ").strip()
    if novo_tipo:
        motor["tipo"] = novo_tipo

    nova_potencia = input(f"Potência CV [{motor['potencia_cv']}]: ").strip()
    if nova_potencia:
        try:
            motor["potencia_cv"] = float(nova_potencia)
        except ValueError:
            print("Potência inválida. Mantendo o valor anterior.")

    print("\n[SUCESSO] Dados do motor atualizados!")


def remover_motor():
    print("\n--- REMOVER MOTOR ---")
    listar_motores()
    if not motores:
        return

    try:
        id_busca = int(input("\nDigite o ID do motor que deseja remover: "))
    except ValueError:
        print("Erro: ID inválido.")
        return

    motor = buscar_motor_por_id(id_busca)
    if not motor:
        print("Motor não encontrado.")
        return

    motores.remove(motor)
    print(f"\n[SUCESSO] Motor '{motor['modelo']}' (ID {id_busca}) removido!")


def menu():
    while True:
        print("\n===============================")
        print("   SISTEMA DE CADASTRO DE MOTORES")
        print("===============================")
        print("1. Cadastrar motor")
        print("2. Listar motores")
        print("3. Atualizar motor")
        print("4. Remover motor")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_motor()
        elif opcao == "2":
            listar_motores()
        elif opcao == "3":
            atualizar_motor()
        elif opcao == "4":
            remover_motor()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Ponto de entrada do programa
if __name__ == "__main__":
    menu()