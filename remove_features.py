import re

file_path = 'C:/Users/mari0/.gemini/antigravity/scratch/cardapio-pet-natural/calculadora-pet-FINAL.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the start and end of the grid block
grid_start = '<div style="display:grid; grid-template-columns: 1fr; gap:14px; margin-bottom:32px; text-align:left;">'
grid_end = '        </div>\n\n        <div style="background:#fff;'

# We want to replace everything in between with only the 4 valid items
new_grid = """<div style="display:grid; grid-template-columns: 1fr; gap:14px; margin-bottom:32px; text-align:left;">
          <div style="display:flex; gap:8px;">
            <svg style="color:#34D399; flex-shrink:0; margin-top:2px;" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
            <div>
              <div style="font-size:13px; font-weight:700; margin-bottom:2px;">Plano alimentar pronto</div>
              <div style="font-size:11px; color:#A7F3D0;">Tudo organizado para o dia a dia</div>
            </div>
          </div>
          <div style="display:flex; gap:8px;">
            <svg style="color:#34D399; flex-shrink:0; margin-top:2px;" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
            <div>
              <div style="font-size:13px; font-weight:700; margin-bottom:2px;">Porções exatas por peso</div>
              <div style="font-size:11px; color:#A7F3D0;">De acordo com porte e fase</div>
            </div>
          </div>
          <div style="display:flex; gap:8px;">
            <svg style="color:#34D399; flex-shrink:0; margin-top:2px;" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
            <div>
              <div style="font-size:13px; font-weight:700; margin-bottom:2px;">Sem precisar pesquisar</div>
              <div style="font-size:11px; color:#A7F3D0;">É só seguir o plano e ver resultados</div>
            </div>
          </div>
          <div style="display:flex; gap:8px;">
            <svg style="color:#34D399; flex-shrink:0; margin-top:2px;" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
            <div>
              <div style="font-size:13px; font-weight:700; margin-bottom:2px;">Rotina semanal organizada</div>
              <div style="font-size:11px; color:#A7F3D0;">Variedade + equilíbrio</div>
            </div>
          </div>"""

start_idx = content.find(grid_start)
end_idx = content.find(grid_end)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_grid + content[end_idx:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Items removed successfully.")
else:
    print("Markers not found.")
