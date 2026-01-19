import shutil
from pathlib import Path

# Funcao que define o mapeamento entre extensoes e pastas de destino
def organize_file(defined_path):  
    rules = {".txt": "Textos",  
             ".pdf": "PDFs",
             ".xlsx": "Planilhas",
             ".docx": "Documentos",
             ".png": "Fotos",
             ".jpg": "Fotos"}  
    
    for file in defined_path.iterdir():  # Loop que varre cada item dentro do diretorio
        if file.is_dir():  # Ignora se for uma pasta, focando apenas em arquivos
            continue
            
        # Verifica se a extensao (convertida para minuscula) esta no mapeamento
        if file.suffix.lower() in rules:  
            folder_name = rules[file.suffix.lower()]
            destination_directory = defined_path / folder_name
            
            # Cria a pasta e protege o script para nao quebrar se ela ja existir
            destination_directory.mkdir(exist_ok=True)  

            new_file = destination_directory / file.name

            counter = 1
            while new_file.exists():  # Loop que garante a integridade dos dados, evitando sobrescrita por nomes duplicados
                new_name = f"{file.stem}_{counter}{file.suffix}"
                new_file = destination_directory / new_name
                counter += 1
            
            shutil.move(str(file), str(new_file))  # Transfere fisicamente o arquivo
            print(f"Movido: {file.name} -> {new_file.name}")
            
    print("--- Organização concluída. ---")       

# Bloco principal de execucao interativa
while True:
    path = input("Digite o caminho: ").strip()
    print("Verificando o caminho...")
    defined_path = Path(path)

    # Tratamento de erro: Verifica se o caminho definido existe
    if not defined_path.exists():
        print("ERRO: Diretório não encontrado.")
        continue
    
    # Tratamento de erro: Garante que o usuario nao passou um arquivo ao inves de pasta
    if not defined_path.is_dir():
        print("ERRO: O caminho especificado é um ARQUIVO. Por favor, indique uma PASTA.")
        continue
    
    else:
        print(f"Diretório encontrado: {defined_path}")
        organize = input("Organizar o diretório (S/N)? ").upper().strip()
        if organize == "S":
            print("\n--- Iniciando organização ---")
            organize_file(defined_path)
            break
        else:
            continue
