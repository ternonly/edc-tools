import urllib.request, time
# preview_theme_id forces theme without cache
url = f"https://survival72gear.myshopify.com/?preview_theme_id=151511040045&_={int(time.time())}"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=20) as r:
    body = r.read().decode("utf-8", errors="replace")
    with open("home_preview.html", "w", encoding="utf-8") as f:
        f.write(body)
print(b"saved, len=" + str(len(body)).encode())
