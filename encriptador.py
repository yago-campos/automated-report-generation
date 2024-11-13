from cryptography.fernet import Fernet

# Gera uma chave de criptografia
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Exemplo de senha
password = "".encode()  # Insira sua senha entre ""
encrypted_password = cipher_suite.encrypt(password)

# Exibe a chave e a senha criptografada para armazená-las no .env
print(f"Chave de criptografia: {key.decode()}")
print(f"Senha criptografada: {encrypted_password.decode()}")