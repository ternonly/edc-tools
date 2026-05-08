import urllib.request, ssl
url = "https://survival72gear.myshopify.com/"
# Try without password first; if redirected use password page
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=20) as r:
        body = r.read().decode("utf-8", errors="replace")
        print(("URL final:" + r.geturl()).encode())
        print(("LEN:" + str(len(body))).encode())
        # Save full body
        with open("home.html", "w", encoding="utf-8") as f:
            f.write(body)
        print(b"saved home.html")
except Exception as e:
    print(f"ERR: {e}".encode())
