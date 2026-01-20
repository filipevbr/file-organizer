## 📂 File Organizer

Script Python desenvolvido para sanear diretórios automaticamente. O algoritmo escaneia o caminho alvo, identifica extensões e move os arquivos para pastas semânticas, garantindo a organização sem intervenção manual.

### ⚙️ Funcionalidades:
* **Segurança de Dados:** Detecta se já existe um arquivo com o mesmo nome no destino. Caso exista, o script renomeia o novo arquivo automaticamente (ex: `relatorio_1.pdf`), evitando sobrescrita acidental e perda de dados.
* **Pathlib:** Uso da biblioteca `pathlib` para manipulação de caminhos orientada a objetos, garantindo compatibilidade entre Windows e Linux.
* **Tratamento de Erros:** Validação de inputs do usuário para evitar quebras de execução (Crash) caso o diretório não exista ou seja inválido.
* **Escalabilidade:** Estrutura baseada em dicionário (`hash map`), facilitando a adição de novas regras de extensão sem alterar a lógica principal.

## 🚀 Quick Start

Você pode rodar este projeto de duas formas: usando o executável standalone (sem necessidade de instalar nada) ou rodando o código fonte Python diretamente.

### Opção A: Executável (Windows) - Recomendado
Ideal para rodar em máquinas de clientes ou ambientes bloqueados onde não é possível instalar o Python.

1. Acesse a aba **[Releases](../../releases)** deste repositório.
2. Baixe o arquivo: `FileOrganizer.exe`.
3. Coloque o arquivo na pasta que deseja organizar (ou execute-o e cole o caminho quando solicitado).

---

### Opção B: Código Fonte
Requer Python 3.x instalado.

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/filipevbr/file-organizer.git
    ```

2. **Acesse a pasta:**
    ```bash
    cd file-organizer
    ```

3. **Execute o script**
    ```bash
    python organizer.py
    ```