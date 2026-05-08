import urllib.request, time
# correct section ID is from the JSON: header_announcements_9jGBFp
url = f"https://survival72gear.myshopify.com/?sections=header_announcements_9jGBFp&_={int(time.time()*1000)}"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
with urllib.request.urlopen(req, timeout=20) as r:
    body = r.read().decode("utf-8", errors="replace")
    print(("len: " + str(len(body))).encode())
    with open("section2.html", "w", encoding="utf-8") as f:
        f.write(body)
