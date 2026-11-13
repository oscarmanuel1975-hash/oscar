// Captura imágenes fijas en instantes concretos para revisar escenas sin renderizar todo el vídeo.
// Uso: node still.js ruta/reel.html carpeta_salida 1.5 8 14.2 [--w 1080 --h 1920 al final no; usa variables W y H]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), { pathToFileURL } = require('url');
const [html, out, ...times] = process.argv.slice(2);
const W = +(process.env.W || 1080), H = +(process.env.H || 1920);
(async () => {
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: W, height: H } });
  await pg.goto(pathToFileURL(path.resolve(html)).href); await pg.evaluate(() => window.ready);
  for (const t of times) { await pg.evaluate(t => window.render(t), +t); await pg.screenshot({ path: `${out}/still_${t}.png` }); }
  await b.close(); console.log('listo', times.join(' '));
})();
