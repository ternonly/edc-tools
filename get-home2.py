import urllib.request, time
url = f"https://survival72gear.myshopify.com/?_={int(time.time())}"
req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache"
})
with urllib.request.urlopen(req, timeout=20) as r:
    body = r.read().decode("utf-8", errors="replace")
    with open("home2.html", "w", encoding="utf-8") as f:
        f.write(body)
print(b"saved home2.html, len=" + str(len(body)).encode())
