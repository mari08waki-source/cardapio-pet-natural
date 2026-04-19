/* Cardápio Pet Natural — Service Worker
 * Estratégia: network-first para navegação HTML, cache-first para ícones/assets estáticos.
 * NÃO intercepta: POST, requests cross-origin, APIs dinâmicas, checkout, wa.me.
 */

const CACHE_VERSION = 'cardapio-pet-v1';
const APP_SHELL = [
  '/',
  '/index.html',
  '/calculadora-pet-FINAL.html',
  '/cardapio.html',
  '/login.html',
  '/obrigado.html',
  '/admin.html',
  '/favicon.png',
  '/manifest.json',
  '/icons/icon-192.png',
  '/icons/icon-512.png',
  '/icons/icon-512-maskable.png'
];

// Instala e pré-cacheia o app shell
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_VERSION).then((cache) => {
      // addAll falha tudo se um item falhar; usamos add individual com catch
      return Promise.all(
        APP_SHELL.map((url) =>
          cache.add(url).catch((err) => {
            console.warn('[SW] falhou ao cachear', url, err);
          })
        )
      );
    })
  );
  self.skipWaiting();
});

// Limpa caches antigos
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys
          .filter((k) => k !== CACHE_VERSION)
          .map((k) => caches.delete(k))
      )
    )
  );
  self.clients.claim();
});

// Fetch handler: só intercepta GET same-origin
self.addEventListener('fetch', (event) => {
  const req = event.request;

  // Ignora requisições não-GET (POST de checkout, login, etc)
  if (req.method !== 'GET') return;

  const url = new URL(req.url);

  // Ignora requisições cross-origin (IA externa, WhatsApp, checkout, CDNs)
  if (url.origin !== self.location.origin) return;

  // Navegação HTML: network-first, fallback cache
  if (req.mode === 'navigate' || req.destination === 'document') {
    event.respondWith(
      fetch(req)
        .then((resp) => {
          // Atualiza cache com versão nova
          const copy = resp.clone();
          caches.open(CACHE_VERSION).then((cache) => cache.put(req, copy));
          return resp;
        })
        .catch(() =>
          caches.match(req).then((cached) => cached || caches.match('/index.html'))
        )
    );
    return;
  }

  // Assets estáticos (ícones, imagens, manifest): cache-first
  if (
    req.destination === 'image' ||
    req.destination === 'manifest' ||
    req.destination === 'style' ||
    req.destination === 'script' ||
    req.destination === 'font'
  ) {
    event.respondWith(
      caches.match(req).then((cached) => {
        if (cached) return cached;
        return fetch(req).then((resp) => {
          if (resp && resp.status === 200 && resp.type === 'basic') {
            const copy = resp.clone();
            caches.open(CACHE_VERSION).then((cache) => cache.put(req, copy));
          }
          return resp;
        });
      })
    );
    return;
  }

  // Qualquer outro caso: deixa passar direto (não intercepta APIs dinâmicas)
});
