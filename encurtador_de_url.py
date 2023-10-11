import pyshorteners

# URL que será encurtada
url = "linkedin.com/in/enzo-jurevics-321336209/"

s = pyshorteners.Shortener()

short_url = s.tinyurl.short(url)

print("URL encurtada:", short_url)
