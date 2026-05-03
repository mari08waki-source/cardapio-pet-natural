import re

file_path = 'C:/Users/mari0/.gemini/antigravity/scratch/cardapio-pet-natural/calculadora-pet-FINAL.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make the checkmarks grid 1 column (better for mobile reading)
old_grid = 'display:grid; grid-template-columns: 1fr 1fr; gap:16px;'
new_grid = 'display:grid; grid-template-columns: 1fr; gap:14px;'

# Reduce padding on the dark green box slightly for mobile
old_padding = 'padding:32px 24px;'
new_padding = 'padding:24px 16px;'

# Adjust the huge price font size slightly down for narrow screens
old_price = 'font-size:46px;'
new_price = 'font-size:42px;'

# Adjust CTA button font size slightly
old_cta_font = 'font-size:19px;'
new_cta_font = 'font-size:17px;'

content = content.replace(old_grid, new_grid)
content = content.replace(old_padding, new_padding)
content = content.replace(old_price, new_price)
content = content.replace(old_cta_font, new_cta_font)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile adjustments applied successfully.")
