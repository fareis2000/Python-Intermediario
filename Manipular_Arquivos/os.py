import os

os.remove('aula116.txt')
os.rename('aula116.txt', 'aula116_renomeado.txt')
os.unlink('aula116_renomeado.txt')
os.symlink('aula116.txt', 'aula116_link.txt')
os.makedirs('nova_pasta/nova_subpasta', exist_ok=True)
os.rmdir('nova_pasta/nova_subpasta')