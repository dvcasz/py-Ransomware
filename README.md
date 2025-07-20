# py-Ransomware: Ransomware Simples em Python

Este projeto é uma demonstração de um **ransomware** básico, desenvolvido em Python para fins puramente **educacionais e de pesquisa** 🔬. Ele inclui um script para criptografar arquivos em um diretório e outro para descriptografá-los mediante uma senha.

**🛑 AVISO DE SEGURANÇA E USO RESPONSÁVEL**
Este código foi criado para ajudar a entender como ransomwares funcionam em um nível fundamental.

* **NÃO EXECUTE ESTE SCRIPT EM SUA MÁQUINA PESSOAL** ou em qualquer sistema com dados importantes.
* **USE APENAS EM UM AMBIENTE SEGURO E ISOLADO**, como uma Máquina Virtual (VM) dedicada para testes.
* O uso deste código para atividades maliciosas é ilegal. O autor não se responsabiliza por qualquer dano ou mau uso.

---

## Funcionalidades

O projeto é composto por dois scripts principais que simulam um ataque de ransomware:

1.  **`malware.py` (O Criptografador)**:
    * Varre o diretório atual em busca de todos os arquivos.
    * Ignora a si mesmo, o script de descriptografia (`decrypt.py`) e o arquivo da chave (`key.key`) para não se autodestruir.
    * Gera uma chave de criptografia simétrica forte usando a biblioteca `cryptography.fernet`.
    * Salva essa chave em um arquivo chamado `key.key`.
    * Lê o conteúdo de cada arquivo, o criptografa e sobrescreve o arquivo original com a versão criptografada.

2.  **`decrypt.py` (O Descriptografador)**:
    * Também varre o diretório para encontrar os arquivos criptografados.
    * Lê a chave de criptografia salva no arquivo `key.key`.
    * Solicita ao usuário que digite uma senha.
    * Se a senha corresponder à que está no código (`"pswrd"`), ele prossegue para descriptografar os arquivos, restaurando-os ao seu estado original.
    * Caso a senha esteja incorreta, ele exibe uma mensagem de erro e não faz nada.

---

## Como Usar (Apenas em Ambiente de Teste!)

Siga estes passos **exclusivamente dentro de uma Máquina Virtual**:

1.  **Prepare o Ambiente**:
    * Crie uma pasta de teste (ex: `C:\teste_ransomware`).
    * Crie alguns arquivos de exemplo dentro dela (ex: `documento.txt`, `foto.jpg`, `planilha.xlsx`).

2.  **Coloque os Scripts na Pasta**:
    * Copie os arquivos `malware.py` e `decrypt.py` para dentro da pasta `C:\teste_ransomware`.

3.  **Execute o Criptografador**:
    * Abra o terminal (Prompt de Comando ou PowerShell) na pasta de teste.
    * Execute o script de criptografia:
        ```bash
        python malware.py
        ```
    * Você verá uma mensagem de que os arquivos foram criptografados. Se tentar abri-los, verá que o conteúdo está ilegível. Um novo arquivo, `key.key`, terá sido criado.

4.  **Execute o Descriptografador**:
    * Agora, execute o script de descriptografia:
        ```bash
        python decrypt.py
        ```
    * O script pedirá a senha. Digite `pswrd` e pressione Enter.
    * Seus arquivos de exemplo serão restaurados ao estado original.

---

## Conceitos de Segurança Demonstrados

* **Criptografia Simétrica**: O uso de uma única chave (`Fernet`) tanto para criptografar quanto para descriptografar os dados.
* **Lógica de Ransomware**: A mecânica básica de negação de acesso a arquivos e a exigência de uma condição (neste caso, uma senha) para restaurar o acesso.
* **Gerenciamento de Chaves (Inseguro)**: O script salva a chave localmente. Em um ransomware real, essa chave seria criptografada com a chave pública do atacante ou enviada para um servidor de C2, tornando a recuperação sem o atacante impossível.
