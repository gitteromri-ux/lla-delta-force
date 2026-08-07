const { chromium } = require('playwright');
(async () => {
  const url = process.argv[2], tab = process.argv[3], y = +process.argv[4], w = +(process.argv[5]||1600), out = process.argv[6];
  const b = await chromium.launch();
  const p = await b.newPage({ viewport:{width:w,height:1000} });
  await p.goto(url + '#' + tab, { waitUntil:'networkidle', timeout:60000 });
  await p.waitForTimeout(1000);
  await p.evaluate(yy => window.scrollTo(0, yy), y);
  await p.waitForTimeout(600);
  await p.screenshot({ path: out });
  await b.close();
})();
