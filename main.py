improt json
import urllib
from pkg_resources import parse_version

url = 'https://upload.almworks.com/tasks/jira-core.json'

def parse_url(url: str) -> list:
    data = urllib.request.urlopen(url).read()
    return json.load(data.decode("utf-8").lstrip('downloads(').rstrip(')'))

def get_product(url: str) -> str:
    return url.lstrip('https://upload.almworks.com/tasks/').rstrip('.json')

def versionCompare(payload: list) -> str:
    # extract versions
    versions = [x['version'] for x in payload]

    highest_ver = '0.0.0'

    # compare versions and store the highest one
    for i in versions:
        if parse_version(i) >= parse_version(highest_ver):
            highest_ver = i

    return highest_ver
    
