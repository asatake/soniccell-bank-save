import sqlite3
import xml.etree.ElementTree as ET


def create_tables(dbname):
    with sqlite3.connect(dbname) as conn:
        c = conn.cursor()
        create_group_table = "CREATE TABLE IF NOT EXISTS bank_group (id INTEGER PRIMARY KEY, name VARCHAR(64))"
        create_bank_table = "CREATE TABLE IF NOT EXISTS bank (id INTEGER PRYMARY KEY, name VARCHAR(64), lsb INTEGER, msb INTEGER, pc INTEGER, group_num INTEGER)"
        c.execute(create_group_table)
        c.execute(create_bank_table)


filename = "banks.xml"

data = open(filename).read()
data = data.encode('utf-8')
data = data.decode()
roots = ET.fromstring(data)

dbname = "soniccell.db"
create_tables(dbname)

group_num = 1
tone_num = 1

with sqlite3.connect(dbname) as conn:
    c = conn.cursor()
    for root in roots:
        for group in root:
            gname = group_name = group.get("Name")
            if (gname == "USER PATCH"):
                continue
            c.execute(
                f'insert into bank_group (id, name) values("{group_num}", "{gname}")'
            )
            group_num += 1
            for pc in group:
                p = pc.get("PC")
                for tone in pc:
                    name = tone.get("Name")
                    lsb = tone.get("LSB")
                    msb = tone.get("MSB")
                    print(name, lsb, msb, p)
                    c.execute(
                        f'insert into bank (id, name, lsb, msb, pc, group_num) values("{tone_num}", "{name}", "{lsb}", "{msb}", "{p}", "{group_num}")'
                    )
                    tone_num += 1