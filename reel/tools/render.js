const { chromium } = require('playwright'); const fs=require('fs');
const FPS=30, DUR=31.5, OUT=process.argv[2], WORKERS=4;
(async()=>{
  fs.mkdirSync(OUT,{recursive:true});
  const b=await chromium.launch(); const total=FPS*DUR;
  await Promise.all([...Array(WORKERS)].map(async(_,w)=>{
    const pg=await b.newPage({viewport:{width:1080,height:1920}});
    await pg.goto('file:///home/user/oscar/reel/reel.html'); await pg.evaluate(()=>window.ready);
    for(let f=w; f<total; f+=WORKERS){
      await pg.evaluate(t=>window.render(t), f/FPS);
      await pg.screenshot({path:`${OUT}/f_${String(f).padStart(4,'0')}.jpg`,type:'jpeg',quality:92});
    }
  }));
  await b.close(); console.log('done',total);
})();
