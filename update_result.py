import re

file_path = 'C:/Users/mari0/.gemini/antigravity/scratch/cardapio-pet-natural/calculadora-pet-FINAL.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

html_start = "  <!-- RESULTADO -->"
html_end = "      <!-- Botão recomeçar -->"

new_html = """  <!-- RESULTADO -->
  <div class="result" id="resultScreen">

    <div class="result-hero" style="background:#FFF;">
      <img src="imagem-resultado.jpg" alt="Pet saudável e feliz" style="display:block;width:100%;height:100%;object-fit:cover;"/>
      <div class="result-hero-badge" style="background:#F0FDF4; color:#166534; border:1px solid #BBF7D0; padding:10px 24px; position:absolute; bottom:16px; left:50%; transform:translateX(-50%); border-radius:99px; display:flex; align-items:center; gap:8px; font-size:13px; font-weight:700; white-space:nowrap; box-shadow:0 4px 16px rgba(0,0,0,0.12);">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        Cardápio personalizado pronto
      </div>
    </div>

    <div class="result-body" style="padding: 24px 16px 32px;">

      <div class="result-header" style="text-align:center; margin-bottom:28px;">
        <h2 id="resultTitle" style="font-size:24px; font-weight:800; letter-spacing:-0.5px; color:#064E3B;">O cardápio ideal do seu pet está pronto 🐾</h2>
        <p id="resultSubtitle" style="font-size:15px; color:#475569; margin-top:8px; line-height:1.4;">Plano alimentar feito especialmente para o porte, fase e necessidades do seu pet.</p>
        <div style="background:#166534; color:#fff; border-radius:12px; padding:12px 16px; margin-top:20px; display:inline-flex; align-items:center; gap:12px; font-weight:600; text-align:left; box-shadow:0 8px 24px rgba(22,101,52,0.3); width:100%;">
          <div style="background:#FBBF24; width:36px; height:36px; border-radius:50%; display:flex; align-items:center; justify-content:center; color:#111; flex-shrink:0;">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m13 2-2 10h9l-9 10 2-10H4l9-10z"/></svg>
          </div>
          <span style="font-size:14px; line-height:1.3;">Você pode alimentar seu pet a partir de hoje!</span>
        </div>
      </div>

      <div style="display:flex; justify-content:center; gap:8px; margin-bottom:28px;">
        <div style="flex:1; text-align:center; background:#F8FAFC; padding:12px 8px; border-radius:12px; border:1px solid #E2E8F0;">
          <svg style="color:#166534; margin-bottom:4px;" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
          <div style="font-size:11px; font-weight:600; color:#475569; line-height:1.2;">Sem adivinhar<br>o que dar</div>
        </div>
        <div style="flex:1; text-align:center; background:#F8FAFC; padding:12px 8px; border-radius:12px; border:1px solid #E2E8F0;">
          <svg style="color:#166534; margin-bottom:4px;" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          <div style="font-size:11px; font-weight:600; color:#475569; line-height:1.2;">Sem perder<br>tempo</div>
        </div>
        <div style="flex:1; text-align:center; background:#F8FAFC; padding:12px 8px; border-radius:12px; border:1px solid #E2E8F0;">
          <svg style="color:#166534; margin-bottom:4px;" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>
          <div style="font-size:11px; font-weight:600; color:#475569; line-height:1.2;">Tudo pronto<br>e seguro</div>
        </div>
      </div>

      <!-- DIAGNÓSTICO -->
      <div style="background:#FFFBEB; border:1.5px solid #FDE68A; border-radius:16px; padding:24px; margin-bottom:28px; text-align:left;">
        <h3 style="color:#D97706; font-size:17px; margin-bottom:16px; display:flex; align-items:center; gap:8px;">
          <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h4l2-9 5 18 3-9h6"/></svg>
          Análise do perfil alimentar do seu pet 🐾
        </h3>
        <p style="font-size:14px; color:#4B5563; line-height:1.5; margin-bottom:12px;">Com base nas suas respostas, analisamos o padrão atual da alimentação dele.</p>
        <p style="font-size:14px; color:#4B5563; line-height:1.5; margin-bottom:12px;">Hoje, ele segue um modelo mais comum no dia a dia, com pouca variação nos ingredientes ao longo da semana.</p>
        <p style="font-size:14px; color:#4B5563; line-height:1.5; margin-bottom:12px;">Para a fase e o porte dele, já é possível deixar essa alimentação mais ajustada, com combinações mais adequadas e melhor distribuídas.</p>
        <p style="font-size:14px; color:#4B5563; line-height:1.5; margin-bottom:16px;">O ponto principal não está apenas nos alimentos em si, mas na forma como essa rotina é organizada. Com pequenas mudanças, já é possível melhorar a rotina alimentar dele a partir de hoje.</p>
        <div style="background:#FEF3C7; padding:12px; border-radius:8px;">
          <p style="font-size:14px; color:#92400E; font-weight:700; line-height:1.4; text-align:center;">👉 Para facilitar isso, o plano completo já está pronto logo abaixo 👇</p>
        </div>
      </div>

      <!-- BLOQUEIO -->
      <div style="background:#F8FAFC; border:1.5px solid #E2E8F0; border-radius:16px; padding:20px; margin-bottom:32px; text-align:left; position:relative; overflow:hidden;">
        <div style="display:flex; gap:16px; align-items:center; margin-bottom:16px;">
          <div style="background:#0F172A; width:48px; height:48px; border-radius:12px; display:flex; align-items:center; justify-content:center; color:#fff; flex-shrink:0;">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          </div>
          <div>
            <h3 style="color:#0F172A; font-size:17px; margin-bottom:4px; font-weight:800;">Plano completo bloqueado</h3>
            <p style="font-size:13px; color:#475569;">Receitas + porções exatas + rotina alimentar + lista de compras</p>
          </div>
        </div>
        <div style="background:#F1F5F9; padding:12px; border-radius:8px; display:flex; gap:10px; align-items:flex-start;">
          <svg style="color:#166534; flex-shrink:0;" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/></svg>
          <p style="font-size:13px; color:#334155; line-height:1.4;"><strong>Não é uma receita genérica da internet.</strong> É um plano completo, equilibrado e pronto para o dia a dia do seu pet.</p>
        </div>
      </div>

      <div class="upsell-box" style="background:#064E3B; padding:32px 24px; border-radius:24px; color:#fff; box-shadow:0 20px 40px rgba(6,78,59,0.4);">
        <div style="background:#FBBF24; color:#064E3B; display:inline-flex; align-items:center; gap:6px; padding:6px 16px; border-radius:99px; font-weight:800; font-size:12px; text-transform:uppercase; margin-bottom:20px; box-shadow:0 4px 12px rgba(251,191,36,0.3);">
          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/></svg> ACESSO IMEDIATO
        </div>
        
        <h3 id="upsellTitle" style="font-size:26px; font-weight:900; margin-bottom:12px; letter-spacing:-0.5px; line-height:1.1;">CARDÁPIO COMPLETO</h3>
        <p id="upsellDesc" style="font-size:15px; color:#D1FAE5; line-height:1.5; margin-bottom:28px;">Tenha o plano alimentar completo e pare de se preocupar com o que o seu pet pode ou não comer.</p>

        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-bottom:32px; text-align:left;">
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
              <div style="font-size:13px; font-weight:700; margin-bottom:2px;">Lista de compras pronta</div>
              <div style="font-size:11px; color:#A7F3D0;">Nada de esquecer ou comprar errado</div>
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
          </div>
          <div style="display:flex; gap:8px;">
            <svg style="color:#34D399; flex-shrink:0; margin-top:2px;" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
            <div>
              <div style="font-size:13px; font-weight:700; margin-bottom:2px;">Permitidos e proibidos</div>
              <div style="font-size:11px; color:#A7F3D0;">Mais segurança para o pet</div>
            </div>
          </div>
        </div>

        <div style="background:#fff; border-radius:16px; padding:24px; color:#111; margin-bottom:24px; text-align:center;">
          <div style="font-size:15px; color:#64748B; text-decoration:line-through; margin-bottom:4px; font-weight:600;">De R$ 67,00</div>
          <div style="font-size:46px; font-weight:900; color:#064E3B; letter-spacing:-1px; line-height:1;">R$ 29,90</div>
          <div style="font-size:13px; color:#475569; margin-top:8px; margin-bottom:20px; font-weight:600;">Pagamento único • acesso imediato</div>
          
          <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:12px; padding:16px; display:flex; gap:12px; align-items:center; text-align:left;">
            <div style="color:#064E3B; flex-shrink:0;">
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>
            </div>
            <div>
              <div style="font-size:14px; font-weight:800; color:#064E3B; margin-bottom:2px;">7 dias de garantia</div>
              <div style="font-size:12px; color:#475569; line-height:1.4;">Se você ou seu pet não gostarem, devolvemos 100% do valor. Sem perguntas.</div>
            </div>
          </div>
        </div>

        <a class="btn-cta" href="https://saude-78211325.clickmax.space/f/cardapios-natural-pet-ee9891bf-374b-4d57-8beb-8954a9133617" target="_blank" rel="noopener" onclick="if(typeof fbq === 'function') fbq('track', 'InitiateCheckout');" style="text-decoration:none; background:#FBBF24; color:#111; padding:22px; border-radius:14px; display:flex; flex-direction:column; align-items:center; gap:4px; font-size:19px; box-shadow:0 8px 24px rgba(251,191,36,0.4); border:none; width:100%; text-transform:uppercase; font-weight:900; letter-spacing:-0.5px;">
          <div style="display:flex; align-items:center; gap:8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            QUERO MEU CARDÁPIO COMPLETO
          </div>
          <span style="font-size:12px; font-weight:700; opacity:0.8;">ACESSO IMEDIATO</span>
        </a>
      </div>

      <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-top:24px; padding:0 8px;">
        <div style="display:flex; gap:8px; align-items:flex-start; flex:1;">
          <svg style="color:#059669; margin-top:2px;" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>
          <div>
            <div style="font-size:12px; font-weight:700; color:#111;">Compra segura</div>
            <div style="font-size:11px; color:#64748B;">Ambiente 100% protegido</div>
          </div>
        </div>
        <div style="display:flex; gap:8px; align-items:flex-start; flex:1;">
          <svg style="color:#059669; margin-top:2px;" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          <div>
            <div style="font-size:12px; font-weight:700; color:#111;">Acesso imediato</div>
            <div style="font-size:11px; color:#64748B;">Baixe o PDF na hora</div>
          </div>
        </div>
      </div>
"""

js_start = "    // Gera cardápio baseado nas respostas para o usuário anônimo (lead)"
js_end = "    const resultEl = document.getElementById('resultScreen');"

new_js = """    // Mantém o comportamento limpo para a tela nova
    const resultEl = document.getElementById('resultScreen');"""

start_idx = content.find(html_start)
end_idx = content.find(html_end)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_html + content[end_idx:]

j_start_idx = content.find(js_start)
j_end_idx = content.find(js_end)

if j_start_idx != -1 and j_end_idx != -1:
    content = content[:j_start_idx] + new_js + content[j_end_idx + len(js_end):]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Sucesso!")
