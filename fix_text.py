import re

file_path = 'C:/Users/mari0/.gemini/antigravity/scratch/cardapio-pet-natural/calculadora-pet-FINAL.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the long diagnosis text
old_diag = """        <p style="font-size:14px; color:#4B5563; line-height:1.5; margin-bottom:12px;">Com base nas suas respostas, analisamos o padrão atual da alimentação dele.</p>
        <p style="font-size:14px; color:#4B5563; line-height:1.5; margin-bottom:12px;">Hoje, ele segue um modelo mais comum no dia a dia, com pouca variação nos ingredientes ao longo da semana.</p>
        <p style="font-size:14px; color:#4B5563; line-height:1.5; margin-bottom:12px;">Para a fase e o porte dele, já é possível deixar essa alimentação mais ajustada, com combinações mais adequadas e melhor distribuídas.</p>
        <p style="font-size:14px; color:#4B5563; line-height:1.5; margin-bottom:16px;">O ponto principal não está apenas nos alimentos em si, mas na forma como essa rotina é organizada. Com pequenas mudanças, já é possível melhorar a rotina alimentar dele a partir de hoje.</p>"""

new_diag = """        <p style="font-size:15px; color:#4B5563; line-height:1.5; margin-bottom:16px;"><strong>Analisamos o perfil alimentar do seu pet com base nas suas respostas.</strong> Com pequenas mudanças na forma como a rotina é organizada, já é possível melhorar a alimentação dele a partir de hoje.</p>"""

content = content.replace(old_diag, new_diag)

# 2. Replace the PDF texts
content = content.replace('Baixe o PDF na hora', 'Acesso liberado no App')
content = content.replace('tudo em PDF pra baixar agora', 'tudo no aplicativo agora')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Text and PDF references updated successfully.")
