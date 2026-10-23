const { chromium } = require('playwright');
(async()=>{
  const times=process.argv.slice(3).map(Number), out=process.argv[2];
  const b=await chromium.launch(); const pg=await b.newPage({viewport:{width:1080,height:1920}});
  await pg.goto('file:///home/user/oscar/reel/reel.html'); await pg.evaluate(()=>window.ready);
  for(const t of times){ await pg.evaluate(t=>window.render(t),t); await pg.screenshot({path:`${out}/still_${t}.png`}); }
  await b.close();
})();
