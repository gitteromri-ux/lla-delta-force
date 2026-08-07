const { chromium } = require('playwright');
(async () => {
  const url = process.argv[2];
  const b = await chromium.launch();
  for (const [w,h,name] of [[1600,1100,'desktop'],[390,900,'mobile']]) {
    const ctx = await b.newContext({ viewport:{width:w,height:h} });
    const p = await ctx.newPage();
    const errs = [];
    p.on('response', r => { if (r.status()>=400) errs.push(r.status()+' '+r.url()); });
    for (const t of ['leads','infl','golive']) {
      await p.goto(url + '#' + t, { waitUntil:'domcontentloaded', timeout:90000 });
      await p.waitForTimeout(1500);
      await p.screenshot({ path:`shots/v2_${name}_${t}.png` });
      await p.evaluate(()=>window.scrollBy(0,2600));
      await p.waitForTimeout(1200);
      await p.screenshot({ path:`shots/v2_${name}_${t}_2.png` });
      const bad = await p.evaluate(() => {
        const out=[];
        document.querySelectorAll('.tabpane:not([hidden]) *').forEach(el=>{
          if(el.scrollWidth>el.clientWidth+2 && getComputedStyle(el).overflowX==='visible')
            out.push(el.className+' | '+el.tagName+' | sw'+el.scrollWidth+' cw'+el.clientWidth);
        });
        if(document.documentElement.scrollWidth>window.innerWidth+1) out.push('PAGE HSCROLL '+document.documentElement.scrollWidth);
        return [...new Set(out)].slice(0,10);
      });
      if(bad.length) console.log(`[${name}/${t}]`, bad.join('\n   '));
    }
    if(errs.length) console.log(`[${name}] failed:`, [...new Set(errs)].slice(0,10));
    await ctx.close();
  }
  await b.close(); console.log('done');
})();
