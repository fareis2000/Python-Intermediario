import os
import re
import subprocess

# Caminho do seu projeto
project_path = os.getcwd()

# Expressão regular para capturar imports
pattern = re.compile(r'^\s*(?:import|from)\s+([a-zA-Z0-9_]+)')

found_libs = set()

# Percorrer todos os .py do projeto
for root, dirs, files in os.walk(project_path):
    for file in files:
        if file.endswith(".py"):
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                for line in f:
                    match = pattern.match(line)
                    if match:
                        found_libs.add(match.group(1))

# Remover módulos padrão do Python (básicos)
ignore = {
    'os', 'sys', 'time', 're', 'math', 'random', 'subprocess',
    'datetime', 'json', 'pathlib', 'typing', 'itertools',
    'collections', 'functools', 'threading', 'asyncio', 'logging',
    'shutil', 'argparse', 'http', 'urllib', 'base64', 'csv', 'io'
}
libs_to_install = [lib for lib in found_libs if lib not in ignore]

print(f"\n🔍 Bibliotecas encontradas: {libs_to_install}\n")

# Instalar cada lib
for lib in libs_to_install:
    try:
        print(f"📦 Instalando {lib}...")
        subprocess.run(["pip", "install", lib])
    except Exception as e:
        print(f"❌ Erro ao instalar {lib}: {e}")
