"""Use Shopify Section Rendering API to bypass page cache."""
import urllib.request, time
url = f"https://survival72gear.myshopify.com/?sections=header-announcements&_={int(time.time()*1000)}"
req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Cache-Control": "no-cache, no-store, must-revalidate",
    "Pragma": "no-cache"
})
try:
    with urllib.request.urlopen(req, timeout=20) as r:
        body = r.read().decode("utf-8", errors="replace")
        print(("status: " + str(r.status)).encode())
        print(("len: " + str(len(body))).encode())
        with open("section-snippet.html", "w", encoding="utf-8") as f:
            f.write(body)
except Exception as e:
    print(f"ERR: {e}".encode())
