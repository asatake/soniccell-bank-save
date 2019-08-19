import sqlite3
from contextlib import closing
import xml.etree.ElementTree as ET

filename = "banks.xml"

data = open(filename).read()
data = data.encode('utf-8')
data = data.decode()

roots = ET.fromstring(data)

tree = {"banks": []}

group_num = 1
tone_num = 1

for root in roots:
    # print(root.tag)
    for group in root:
        if (group.get("Name") == "USER PATCH"):
            continue
        group_num += 1
        # print(group.get("Name"))
        for tone in group:
            # print(tone.get("Name"))
            tone_num += 1

# dbname = "banks"

# with closing(sqlite3.connect(dbname)) as conn:
#     c = conn.cursor()
#     create_table = "create table if not exists bank (id int, name varchar(64), lsb int, msb int, pc int)"
#     c.execute(create_table)
