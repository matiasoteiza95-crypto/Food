"""Builds the home-screen (PWA) version of Cauldron into docs/ for GitHub Pages.

index.html is written for Claude artifacts, which add the <!doctype>/<head> shell at
publish time. This wraps the same file in that shell plus the iPhone app tags.
Run from the repo root after editing index.html:  python3 scripts/build-pwa.py
"""
import hashlib, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
app = (root / "index.html").read_text(encoding="utf-8")
version = hashlib.sha1(app.encode()).hexdigest()[:10]

head = """<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Cauldron">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#140f1c">
<meta name="description" content="Daily meal planner: per-person calories, a weekly budget, UK supermarket comparison and a shopping list.">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" type="image/png" href="icon-192.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""
tail = """
<script>
if ("serviceWorker" in navigator) addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
</script>
</body>
</html>
"""
(root / "docs" / "index.html").write_text(head + app + tail, encoding="utf-8")

sw = (root / "scripts" / "sw.template.js").read_text(encoding="utf-8").replace("__VERSION__", version)
(root / "docs" / "sw.js").write_text(sw, encoding="utf-8")
print("built docs/ version", version)
