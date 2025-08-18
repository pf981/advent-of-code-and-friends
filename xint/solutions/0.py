import dataclasses
import datetime
import math
import requests
import re


@dataclasses.dataclass
class Contact:
    name: str
    city: str
    birthdate: datetime.date


def xint(path: str) -> str:
    return requests.get(f"https://salza.dk/xint{path}").text


def contacts(name: str) -> Contact | None:
    result = xint(f"/contacts?name={name}")

    if result.strip() == "No match":
        return None

    for line in result.splitlines():
        key, value = line.split(": ")
        key = key.lower()

        if key == "name":
            name = value
        elif key == "city":
            city = value
        elif key == "birthdate":
            birthdate = datetime.datetime.strptime(value, "%Y-%m-%d").date()
        else:
            raise ValueError(f"Unexpected key, {key}, in contacts response: {result}")

    return Contact(name=name, city=city, birthdate=birthdate)


def message(content: str) -> str:
    return xint(f"/secure?message={content}")


def md5(content: str) -> str:
    return xint(f"/md5?content={content}")


# https://salza.dk/xint/case-skills-0
# https://salza.dk/xint/case-skills-1
message("1991-01-15")

suspects = [
    "Liam Foster",
    "Emily Martinez",
    "Emma Richardson",
    "Michael Brown",
    "Samantha Green",
    "Olivia Harris",
    "Laura Johnson",
    "Emma Watson",
    "Sophia Rodriguez",
    "Noah Scott",
    "Chloe Davis",
    "Sabine Wagner",
    "Ava Hill",
    "Isabella Young",
    "Grace Baker",
    "Zoe Phillips",
    "Abigail Barnes",
    "Isaiah Foster",
]

suspect_info: dict[str, Contact | None] = {}
for suspect in suspects:
    suspect_info[suspect] = contacts(suspect)

suspect_info

target = suspect_info["Sabine Wagner"]
assert target

# https://salza.dk/xint/case-german-suspect
print(message(f"{target.name} {target.birthdate}"))
# Yes, Sabine is the person we are looking for!

# https://salza.dk/xint/case-weak-password
password = "sunshine"
assert md5(password) == "0571749e2ac330a7455809c6b0e7af90"
print(message(password))
# Great. Sunshine works. We are now much closer to unraveling the informant network.

# https://salza.dk/xint/case-blueprint-exchange
text = """Spy 1:
  2024-09-02 45.661756731212506, 9.6563905065983
  2024-09-03 45.509343929262556, 10.223344034198696
  2024-09-04 45.16067947531438, 10.03673133673127
  2024-09-05 44.84121575185407, 10.282274359714725
  2024-09-06 44.771531406772446, 10.847023312576667
  2024-09-07 44.715723321080254, 11.274268172567877
  2024-09-08 45.08098054121563, 11.760443358075115
  2024-09-09 45.381864528076036, 11.873393148647503
  2024-09-10 45.51278532034426, 11.544365497849675
  2024-09-11 45.42646590138319, 10.985885474583696
  2024-09-12 45.32596210157767, 10.84106975167043
  2024-09-13 45.14029227074016, 10.778295446830253
  2024-09-14 44.97355895881006, 10.72054308637729

Spy 2:
  2024-09-02 45.861849004734914, 11.496433494201893
  2024-09-03 45.73054797371461, 11.378417801102358
  2024-09-04 45.5180633993797, 11.526565160525179
  2024-09-05 45.43707284390177, 11.855502517887713
  2024-09-06 45.64108654897535, 11.923298767115105
  2024-09-07 45.72879520325385, 11.73748682478818
  2024-09-08 45.858351658830316, 11.514010299557143
  2024-09-09 45.73755850552394, 11.365862940134322
  2024-09-10 45.58663812196578, 10.705477253215644
  2024-09-11 45.422975646827076, 10.959085444769967
  2024-09-12 45.83036497200938, 11.00177197206129
  2024-09-13 45.87059140706045, 10.793361279991895
  2024-09-14 45.62879636359038, 10.51715433869511"""

spies = []
for position_str in text.split("\n\n"):
    positions = []
    for line in position_str.splitlines()[1:]:
        date, lat, lon = re.findall(r"[0-9-.]+", line)
        positions.append((date, float(lat), float(lon)))

    spies.append(positions)


target_date = None
target_d = float("inf")
target_lat_lon = None
for (date1, lat1, lon1), (date2, lat2, lon2) in zip(*spies):
    assert date1 == date2
    d = math.dist((lat1, lon1), (lat2, lon2))

    if d < target_d:
        target_d = d
        target_date = date1
        target_lat_lon = lat1, lon1

target_lat_lon

print(message("2024-09-11 Verona"))
# Thank you. Well done! You have been promoted to security Level 1 with the token:
#
#   zfea6yd5e
#
# Use it to access Level 1: https://salza.dk/xint/level1?token=zfea6yd5e
