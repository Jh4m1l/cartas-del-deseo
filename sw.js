self.addEventListener('install', e => {
  e.waitUntil(
    caches.open('cartas-cache').then(cache => {
      return cache.addAll([
        '/cartas-del-deseo/',
        '/cartas-del-deseo/index.html',
        '/cartas-del-deseo/cartas.json',
        '/cartas-del-deseo/icono.png'
      ]);
    })
  );
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request))
  );
});