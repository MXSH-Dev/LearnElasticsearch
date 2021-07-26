from datetime import datetime
from elasticsearch import Elasticsearch
import json
import pprint

import string
import random

from faker import Faker

pp = pprint.PrettyPrinter(indent=2)
es = Elasticsearch(["http://localhost:9200/"])

# sample = {
#     "reqest_id": "3dd7116dd5244e1ebc9b40f2ae641e20",
#     "operation_id": "2caa755ac6fb31aab8024b0b1f0d1fa5fc889e46cb430ca9894e2f6474c4d94c",
#     "parent_operation_id": "2caa755ac6fb31aab8024b0b1f0d1fa5fc889e46cb430ca9894e2f6474c4d94c",
#     "user_name": "Michael Xing",
#     "user_id": "x214074",
#     "start_timestamp": "1607514901",
#     "completion_timestamp": "1607514901",
#     "type": "onboard | dry_run | execute",
#     "device_hostname": "EDTNABTFSE54",
# }

# print(sample["reqest_id"])
# pp.pprint(es.cluster.health())

# res = es.index(index="sdn-cache", id=sample["reqest_id"], body=sample)
# print(res["result"])

# res = es.get(
#     index="sdn-cache",
#     id=sample["reqest_id"],
# )
# pp.pprint(res["_source"])

# for i in range(30000):
#     r = "".join(random.choices(string.ascii_lowercase + string.digits, k=32))
#     sample["reqest_id"] = r
#     res = es.index(index="sdn-cache", id=sample["reqest_id"], body=sample)

fake = Faker()
dt = fake.date_time_between(start_date="-1y", end_date="now")
print(dt)

record = {
    "source": "day0_portal",
    "event": "login",
    "user_id": "",
    "name": "",
    "fingerprint": "",
}

# people = [
#     {"name": fake.first_name(), "id": fake.bothify(text="?######", letters="xt")}
#     for i in range(30)
# ]
# person = {"name": "", "id": ""}
# print(fake.first_name())
# print(fake.bothify(text="?######", letters="xt"))

# for i in range(5):
#     person["id"] = fake.bothify(text="?######", letters="xt")
#     person["name"] = fake.first_name()
#     print(person)
#     people[i] = person
people = [
    {"name": "Patrick", "id": "x065610"},
    {"name": "John", "id": "x148849"},
    {"name": "Tracy", "id": "x740885"},
    {"name": "Valerie", "id": "x953680"},
    {"name": "Sara", "id": "t698634"},
    {"name": "Elizabeth", "id": "t692805"},
    {"name": "Jose", "id": "t248551"},
    {"name": "Shawn", "id": "t554423"},
    {"name": "Joel", "id": "t679898"},
    {"name": "Victoria", "id": "x954995"},
    {"name": "Jennifer", "id": "t081893"},
    {"name": "Cindy", "id": "t301473"},
    {"name": "Patrick", "id": "x685372"},
    {"name": "Christopher", "id": "x389660"},
    {"name": "Sean", "id": "x916331"},
    {"name": "Brenda", "id": "t633171"},
    {"name": "Gary", "id": "x108152"},
    {"name": "Jeremy", "id": "t111032"},
    {"name": "Mary", "id": "x243906"},
    {"name": "Justin", "id": "t474588"},
    {"name": "David", "id": "x683471"},
    {"name": "Benjamin", "id": "t083629"},
    {"name": "Xavier", "id": "x411527"},
    {"name": "Robert", "id": "t421626"},
    {"name": "Justin", "id": "t987151"},
    {"name": "Samantha", "id": "t056125"},
    {"name": "Robert", "id": "x359127"},
    {"name": "Alexander", "id": "t579392"},
    {"name": "Crystal", "id": "x904147"},
    {"name": "Melanie", "id": "x355094"},
]
# print(people)

for _ in range(1000):
    people_index = random.randrange(30)
    rec = {
        "source": "day0_portal",
        "event": "login",
        "user_id": people[people_index]["id"],
        "name": people[people_index]["name"],
        "timestamp": fake.date_time_between(start_date="-1y", end_date="now"),
        "fingerprint": "",
    }
    # print(rec)
    res = es.index(index="ztn-event-records", body=rec)
