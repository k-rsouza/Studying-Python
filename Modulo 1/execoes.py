try:
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
   # print(f"O resultado é: {resultado}")
except ValueError as e:
    print(f"Erro: Tipo de dado inserido inválido. {e}")
    raise ValueError("Por favor, insira um número válido.")      # Lança uma exceção e interrompe a execução!!!
except Exception as e:
    print(f"Erro: {e}")
else:
     print(f"O resultado é: {resultado}")
finally:
    print("Execução finalizada.")  # O bloco finally é sempre executado, independentemente de ocorrer uma exceção ou não.