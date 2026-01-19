# 🛠️ Automation Toolkit

Repositório focado em scripts de automação para resolver problemas reais de infraestrutura, suporte e produtividade.

## 📂 File Organizer Automation

Script Python desenvolvido para sanear diretórios automaticamente. O algoritmo escaneia o caminho alvo, identifica extensões e move os arquivos para pastas semânticas, garantindo a organização sem intervenção manual.

### ⚙️ Funcionalidades:
* **Segurança de Dados:**Detecta se já existe um arquivo com o mesmo nome no destino. Caso exista, o script renomeia o novo arquivo automaticamente (ex: `relatorio_1.pdf`), evitando sobrescrita acidental e perda de dados.
* **Pathlib:** Uso da biblioteca `pathlib` para manipulação de caminhos orientada a objetos, garantindo compatibilidade entre Windows e Linux.
* **Tratamento de Erros:** Validação de inputs do usuário para evitar quebras de execução (Crash) caso o diretório não exista ou seja inválido.
* **Escalabilidade:** Estrutura baseada em dicionário (`hash map`), facilitando a adição de novas regras de extensão sem alterar a lógica principal.

### ⚡ Quick Start (Como usar)

**Pré-requisitos:** Python 3.x instalado.

1. **Clone o repositório:**
   ```bash
   git clone 

2. **Execute o script:**

Bash

python file_organizer/organizer.py