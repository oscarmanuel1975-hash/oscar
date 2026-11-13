// Saca fotogramas de una página HTML que expone window.render(t) y window.ready.
// Uso: node render_frames.js --html ruta/reel.html --out carpeta_frames [--fps 30] [--dur 33]
//        [--w 1080] [--h 1920] [--workers 4] [--quality 92]
// Si no se pasa --fps o --dur, se leen de window.REEL = {fps, duration} en la página.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), { pathToFileURL } = require('url');
const a = {}; for (let i = 2; i < process.argv.length; i += 2) a[process.argv[i].replace(/^--/, '')] = process.argv[i + 1];
if (!a.html || !a.out) { console.error('Faltan --html y --out'); process.exit(1); }
const W = +(a.w || 1080), H = +(a.h || 1920), WORKERS = +(a.workers || 4), Q = +(a.quality || 92);
(async () => {
  fs.mkdirSync(a.out, { recursive: true });
  const url = pathToFileURL(path.resolve(a.html)).href;
  const browser = await chromium.launch();
  const probe = await browser.newPage({ viewport: { width: W, height: H } });
  await probe.goto(url); await probe.evaluate(() => window.ready);
  const meta = await probe.evaluate(() => window.REEL || {});
  await probe.close();
  const FPS = +(a.fps || meta.fps || 30), DUR = +(a.dur || meta.duration);
  if (!DUR) { console.error('Falta --dur o window.REEL.duration'); process.exit(1); }
  const total = Math.round(FPS * DUR);
  await Promise.all([...Array(WORKERS)].map(async (_, w) => {
    const pg = await browser.newPage({ viewport: { width: W, height: H } });
    await pg.goto(url); await pg.evaluate(() => window.ready);
    for (let f = w; f < total; f += WORKERS) {
      await pg.evaluate(t => window.render(t), f / FPS);
      await pg.screenshot({ path: `${a.out}/f_${String(f).padStart(5, '0')}.jpg`, type: 'jpeg', quality: Q });
    }
  }));
  await browser.close();
  console.log(JSON.stringify({ frames: total, fps: FPS, duration: DUR, out: a.out }));
})();
