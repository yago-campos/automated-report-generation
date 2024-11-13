# Selenium Web Automation - Login e Geração de Relatórios Seguros

Este repositório contém um script de automação utilizando o Selenium para realizar o login em um portal web e gerar relatórios de forma automatizada. O código foi desenvolvido com foco em segurança, utilizando criptografia de senha e variáveis de ambiente.

## Funcionalidades

- **Login seguro**: O script realiza o login no portal web com autenticação segura utilizando senha criptografada.
- **Geração de relatórios**: Após o login, o script navega pelo portal e preenche os dados necessários para gerar um relatório.
- **Criptografia de senha**: A senha é armazenada de forma segura utilizando a biblioteca `cryptography.fernet`.
- **Uso de variáveis de ambiente**: Credenciais sensíveis e a chave de criptografia são carregadas a partir de um arquivo `.env`, evitando a exposição de dados diretamente no código.

## Como Usar

### Requisitos

- Python 3.x
- Selenium
- ChromeDriver (ou outro WebDriver compatível)
- Bibliotecas Python:
  - `cryptography`
  - `python-dotenv`
  
### Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure seu arquivo `.env` com as seguintes variáveis de ambiente:
    ```
    usuario=seu_usuario
    ENCRYPTION_KEY=chave_de_criptografia_gerada
    senha=senha_criptografada
    ```

4. Certifique-se de que o ChromeDriver ou o WebDriver que você deseja usar esteja instalado e configurado corretamente.

### Execução

1. Execute o script:
    ```bash
    python seu_script.py
    ```

2. O script abrirá o navegador, realizará o login e gerará o relatório conforme os dados informados no código.

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum erro ou quiser melhorar o código, fique à vontade para abrir uma *issue* ou enviar um *pull request*.

## Disclaimer

Este código foi desenvolvido com o objetivo de automatizar tarefas em sites de forma segura. Certifique-se de estar em conformidade com os Termos de Serviço do site ao utilizá-lo.
