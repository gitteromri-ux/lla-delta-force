const { chromium } = require('playwright');
(async () => {
  const url = process.argv[2];
  const tag = process.argv[3] || 'local';
  const b = await chromium.launch();
  const tabs = ['golive','meta','leads','infl','email','ceo'];
  for (const [w,h,name] of [[1600,1200,'desktop'],[390,900,'mobile']]) {
    const ctx = await b.newContext({ viewport:{width:w,height:h}, deviceScaleFactor:1 });
    const p = await ctx.newPage();
    const errs = [];
    p.on('response', r => { if (r.status()>=400) errs.push(r.status()+' '+r.url()); });
    for (const t of tabs) {
      await p.goto(url + '#' + t, { waitUntil:'networkidle', timeout:60000 });
      await p.waitForTimeout(1200);
      await p.screenshot({ path:`shots/${tag}_${name}_${t}.png`, fullPage:true });
      // overflow detection
      const bad = await p.evaluate(() => {
        const out = [];
        document.querySelectorAll('.tabpane:not([hidden]) *').forEach(el => {
          if (el.scrollWidth > el.clientWidth + 2 && getComputedStyle(el).overflowX === 'visible') {
            out.push(el.className + ' | ' + el.tagName + ' | sw' + el.scrollWidth + ' cw' + el.clientWidth);
          }
        });
        const de = document.documentElement;
        if (de.scrollWidth > window.innerWidth + 1) out.push('PAGE HSCROLL ' + de.scrollWidth);
        return out.slice(0,15);
      });
      if (bad.length) console.log(`[${name}/${t}] overflow:`, bad.join('\n   '));
    }
    if (errs.length) console.log(`[${name}] failed requests:`, [...new Set(errs)].slice(0,20));
    await ctx.close();
  }
  await b.close();
  console.log('done');
})();
