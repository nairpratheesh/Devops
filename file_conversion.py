import pandas as pd
try:
    from urllib.request import Request, urlopen  # Python 3
except ImportError:
    from urllib2 import Request, urlopen  # Python 2

req = Request('https://coderbyte.com/api/challenges/logs/user-info-csv')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0')
content = urlopen(req)

df = pd.read_csv(content)
print("before sorting",df)
df.sort_values(["Name"],axis=0,ascending=[True],inplace=True)

print("After converting",df)
print(df.to_json())

