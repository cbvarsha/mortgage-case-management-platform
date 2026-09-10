const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs');const html=fs.readFileSync('dist/index.html','utf8'),js=fs.readFileSync('dist/app.js','utf8');
test('all eight enterprise modules have distinct renderers',()=>['casesView','tasksView','documentsView','underwritingView','valuationsView','communicationsView','customersView','reportsView'].forEach(x=>assert.match(js,new RegExp(`function ${x}|${x}:`))));
test('all seven case tabs have dedicated content',()=>['overview','affordability','documents','property','conditions','notes','activity'].forEach(x=>assert.match(js,new RegExp(`${x}`))));
test('critical workflows are implemented',()=>['new-case','open-case','toggle-doc','set-stage','approve','request-info','add-condition','add-note','book-valuation','send-message','export-report'].forEach(x=>assert.match(js,new RegExp(`['\"]${x}['\"]`))));
test('required assets are linked',()=>['styles.css','enterprise.css','model.js','app.js'].forEach(x=>assert.ok(html.includes(x))));
test('no placeholder href controls',()=>assert.ok(!/href=["']#["']/.test(html)));
