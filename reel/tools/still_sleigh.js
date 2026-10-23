const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1080,height:1920}});
await pg.goto('file:///home/user/oscar/reel/reel.html');await pg.evaluate(()=>window.ready);
await pg.evaluate(T=>window.render(T),+process.argv[3]);await pg.screenshot({path:process.argv[2]});await b.close()})();
