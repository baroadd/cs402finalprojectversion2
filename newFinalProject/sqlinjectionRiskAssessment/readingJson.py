import json
import urllib.parse
from pprint import pprint
def read(jsonfile,hostname):
    
    with open(jsonfile) as f:
        data = json.load(f)
    hostnameParsed = urllib.parse.urlparse(hostname)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=hostnameParsed)
    listurl=[]
    for each in data["log"]["entries"]:
        url = each["request"]["url"]
        parsed = urllib.parse.urlparse(url)
        parsedDomain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed)
        parameterList = urllib.parse.parse_qs(parsed.query)
        if parameterList and domain == parsedDomain:
            listurl.append(url)
    return listurl