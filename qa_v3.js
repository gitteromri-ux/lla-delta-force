const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport:{width:1600,height:1100}, permissions:['clipboard-read','clipboard-write'] });
  const p = await ctx.newPage();
  const errs=[]; p.on('pageerror',e=>errs.push(String(e)));
  await p.goto('http://localhost:8099/index.html',{waitUntil:'domcontentloaded'});
  for (const t of ['golive','meta','leads','infl','email','ceo']) {
    await p.click(`.tb[data-p="${t}"]`); await p.waitForTimeout(300);
    const vis = await p.$eval(`#p-${t}`, el=>!el.hidden && el.getBoundingClientRect().height>200);
    const h = await p.$eval(`#p-${t}`, el=>el.scrollHeight);
    console.log(t, 'visible:'+vis, 'height:'+h);
  }
  await p.click('.tb[data-p="leads"]'); await p.waitForTimeout(300);
  const nb = await p.$$eval('#p-leads .cpy', b=>b.length);
  console.log('copy buttons in leads:', nb);
  await p.$eval('#p-leads .cpy', b=>b.scrollIntoView());
  await p.click('#p-leads .cpy');
  await p.waitForTimeout(500);
  const label = await p.$eval('#p-leads .cpy', b=>b.textContent);
  const clip = await p.evaluate(()=>navigator.clipboard.readText());
  console.log('button label after click:', label, '| clipboard chars:', clip.length, '| starts:', JSON.stringify(clip.slice(0,60)));
  // link count and overflow
  const stats = await p.evaluate(()=>{
    const pane=document.getElementById('p-leads');
    const links=[...pane.querySelectorAll('a[href^="http"]')].map(a=>a.href);
    const over=[...pane.querySelectorAll('*')].filter(e=>e.scrollWidth>e.clientWidth+8 && !e.classList.contains('twrap') && !e.classList.contains('cbx-b')).length;
    return {links:links.length, uniq:new Set(links).size, over};
  });
  console.log('links', JSON.stringify(stats));
  // mobile
  const p2 = await ctx.newPage();
  await p2.setViewportSize({width:390,height:844});
  await p2.goto('http://localhost:8099/index.html#leads',{waitUntil:'domcontentloaded'});
  await p2.waitForTimeout(600);
  const ov = await p2.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
  console.log('mobile horizontal overflow px:', ov);
  await p2.screenshot({path:'shots/v3_mobile.png'});
  console.log('pageerrors:', errs.length, errs.slice(0,3));
  await b.close();
})();
