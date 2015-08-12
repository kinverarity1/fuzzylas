from __future__ import print_function

import codecs
import csv


def load_curves(fn):
    fieldnames = ["company", "type", "method", "mnemonic",
                  "model", "units", "unittype", "description"]
    with codecs.open(fn, mode="r", encoding="utf8") as datafile:
        reader = csv.DictReader(datafile, fieldnames=fieldnames)
        curves = {}
        for row in reader:
            record = {
                "company": row[0].decode('latin-1'),
                "type": row[1].decode('latin-1'),
                "method": row[2].decode('latin-1'),
                # redundant but useful in result lists
                "mnemonic": row[3].decode('latin-1'),
                "model": row[4].decode('latin-1'),
                "units": row[5].decode('latin-1'),
                "unittype": row[6].decode('latin-1'),
                "description": row[7].decode('latin-1')
            }
            curves.setdefault(str(row["mnemonic"]), []).append(record)
    return curves

_fn = os.path.join(os.path.dirname(__file__), "curves.csv")
curves = load_curves(_fn)
