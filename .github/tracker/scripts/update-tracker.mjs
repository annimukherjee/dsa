import fs from "fs";
import { execSync } from "child_process";
import { formatISO, subDays } from "date-fns";
import Heatmap from "github-contribution-graph";   // tiny zero-dep heat-map helper
import { ChartJSNodeCanvas } from "chartjs-node-canvas";

const [,, TO, FROM] = process.argv;           // commit range

// 1. Collect commit messages that match the DSA pattern
const raw = execSync(`git log ${FROM}..${TO} --pretty=%H:::%s:::%ci:::%an`)
  .toString()
  .trim()
  .split("\n");

const pattern = /^[0-9]{4}-[0-9]{2}-[0-9]{2}\s+(LeetCode|HackerRank|Codeforces|CodeChef|AtCoder)\s+.+/;

let data = { generated: formatISO(new Date()), entries: [] };
try { data = JSON.parse(fs.readFileSync(".github/tracker/data.json")); } catch {}

raw.forEach(line => {
  const [hash, msg, isoDate, author] = line.split(":::");
  if (!pattern.test(msg)) return;

  const [dateStr,, platform] = msg.match(/^([0-9\-]+)\s+(LeetCode|HackerRank|Codeforces|CodeChef|AtCoder)/);
  const existing = data.entries.find(e => e.date === dateStr);
  if (existing) {
    existing.count += 1;
    existing.messages.push({ msg, author, hash });
  } else {
    data.entries.push({
      date: dateStr,
      platform,
      count: 1,
      messages: [{ msg, author, hash }],
    });
  }
});

// keep newest first
data.entries.sort((a, b) => new Date(b.date) - new Date(a.date));
fs.mkdirSync(".github/tracker", { recursive: true });
fs.writeFileSync(".github/tracker/data.json", JSON.stringify(data, null, 2));

// 2. Pre-generate PNG bar-chart for platform stats
const width = 700, height = 300;
const chart = new ChartJSNodeCanvas({ width, height });
const platforms = [...new Set(data.entries.map(e => e.platform))];
const counts = platforms.map(p => data.entries.filter(e => e.platform === p).length);

const cfg = {
  type: "bar",
  data: { labels: platforms, datasets: [{ data: counts }] },
  options: { plugins: { legend: { display: false } } }
};
fs.writeFileSync(".github/tracker/platform.png", await chart.renderToBuffer(cfg));

// 3. Build index.html (static, JS loads the data+PNG)
const heat = new Heatmap({
  entries: data.entries.map(e => ({ date: e.date, count: e.count })),
  until: formatISO(new Date(), { representation: "date" }),
  transform(count) { return Math.min(4, count); },  // bucket 0-4
});

const html = /*html*/ `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>DSA Tracker</title>
  <link href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css" rel="stylesheet" />
  <style>
    .heatmap rect[data-level="0"] { fill: #161b22 }
    .heatmap rect[data-level="1"] { fill: #0e4429 }
    .heatmap rect[data-level="2"] { fill: #006d32 }
    .heatmap rect[data-level="3"] { fill: #26a641 }
    .heatmap rect[data-level="4"] { fill: #39d353 }
    canvas { max-width: 100%;}
  </style>
</head>
<body>
<main class="container">
  <hgroup>
    <h1>🚀 DSA Problem Tracker</h1>
    <h2>Last updated ${new Date().toLocaleString()}</h2>
  </hgroup>

  <section id="heatmap">${heat.svg}</section>

  <section>
    <h3>Platform Split</h3>
    <img src="platform.png" alt="platform bar chart" />
  </section>

  <details>
    <summary>Raw entries JSON</summary>
    <pre id="json"></pre>
  </details>
</main>
<script type="module">
  fetch('data.json').then(r=>r.json()).then(d=>{
    document.getElementById('json').textContent = JSON.stringify(d, null, 2);
  });
</script>
</body>
</html>`;
fs.writeFileSync(".github/tracker/index.html", html);
console.info("🎉 tracker updated");