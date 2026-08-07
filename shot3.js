const { chromium } = require('playwright');
(async () => {
  const url = process.argv[2], tab=process.argv[3], scroll=parseInt(process.argv[4]||'0');
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport:{width:1600,height:1100} });
  const p = await ctx.newPage();
  await p.goto(url, { waitUntil:'domcontentloaded', timeout:90000 });
  await p.click(`.tb[data-p="${tab}"]`);
  await p.waitForTimeout(800);
  if(scroll){ await p.evaluate(y=>window.scrollTo(0,y), scroll); await p.waitForTimeout(1500); }
  await p.screenshot({ path:`shots/q_${tab}_${scroll}.png` });
  await b.close(); console.log('ok');
})();
