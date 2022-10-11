import json
import urllib.request
from pkg_resources import parse_version
from app.db import db_ops


def parse_url(url: str) -> list:
    try:
        data = urllib.request.urlopen(url).read()
        return json.loads(
            data.decode("utf-8").lstrip('downloads(').rstrip(')'))
    except:
        raise


def version_compare(payload: list) -> str:
    # extract versions
    versions = [x['version'] for x in payload]

    highest_ver = '0.0.0'

    # compare versions and store the highest one
    for i in versions:
        if parse_version(i) >= parse_version(highest_ver):
            highest_ver = i
    print(highest_ver)
    return highest_ver


def check_version(name: str, version: str, database: str) -> str:
    with db_ops(database) as cur:
        cur.execute('INSERT OR IGNORE INTO Application VALUES(?, ?)',
                    (name, "0.0.0"))
    with db_ops(database) as cur:
        current_ver = cur.execute(
            f'SELECT version from Application where name="{name}"').fetchone(
            )[0]
        if parse_version(current_ver) > parse_version(version):
            cur.execute('UPDATE Application SET version=? WHERE name=?',
                        (version, name))
            return {
                "status":
                f"The release {current_ver} is revoked! Current version is {version}"
            }
        elif parse_version(current_ver) < parse_version(version):
            cur.execute('UPDATE Application SET version=? WHERE name=?',
                        (version, name))
            return {"status": f"The new version {version} is available!"}
        else:
            return {
                "status": f"Nothing changed current version is {current_ver}"
            }
