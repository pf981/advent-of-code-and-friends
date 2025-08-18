import dataclasses
import datetime
import requests


@dataclasses.dataclass
class Plate:
    plate: str
    name: str
    buydate: datetime.date
    car: str


def xint(path: str) -> str:
    return requests.get(f"https://salza.dk/xint{path}").text


def get_plate_info(plate: str) -> Plate | None:
    result = xint(f"/cars?plate={plate}")

    if result.strip() == "No match":
        return None

    for line in result.splitlines():
        key, value = line.split(": ")
        key = key.lower()

        if key == "plate":
            plate = value
        elif key == "name":
            name = value
        elif key == "buydate":
            buydate = datetime.datetime.strptime(value, "%Y-%m-%d").date()
        elif key == "car":
            car = value
        else:
            raise ValueError(f"Unexpected key, {key}, in plate response: {result}")

    return Plate(plate=plate, name=name, buydate=buydate, car=car)


def message(content: str) -> str:
    return xint(f"/secure?message={content}")


def field(record, name):
    for line in record.splitlines():
        if line.startswith(f"{name}: "):
            return line[len(f"{name}: ") :]


def time_to_minutes(time: str) -> int:
    hours, minutes = time.split(":")
    return 60 * int(hours) + int(minutes)


# https://salza.dk/xint/level1?token=zfea6yd5e

# https://salza.dk/xint/case-blueprint-exchange-2
cars = xint("/attachments/car-list.txt")
checkins = xint("/attachments/check-in-list.txt")

name_to_checkin = {}
for line in checkins.splitlines():
    time, name = line.split(" ", 1)
    name_to_checkin[name] = time_to_minutes(time)


target_name = None
target_plate = None
for line in cars.splitlines():
    time, plate = line.split(" ", 1)
    plate_info = get_plate_info(plate)

    if not plate_info or plate_info.name not in name_to_checkin:
        continue

    t1 = time_to_minutes(time)
    t2 = name_to_checkin[plate_info.name]

    if t1 + 10 <= t2 <= t1 + 20:
        target_name = plate_info.name
        target_plate = plate
        break
else:
    raise ValueError("Unable to locate suspect")

print(message(f"{target_name} {target_plate}"))
# Perfect. This is exactly what we are looking for! Token part 1 = fu2

token1 = "fu2"

# https://salza.dk/xint/case-hawkeye-backup-exploit
for _ in range(100):
    hawkeye_token = xint("/token?appid=hawkeye")
    hawkeye = xint(f"/entities/hawkeye.php?token={hawkeye_token}")
    if hawkeye.strip() != "Access Denied":
        break
else:
    raise ValueError("Unable to access hawkeye in 100 attempts")

# print(hawkeye)
key = field(hawkeye, "KEY")
print(message(key))
# Thank you. This is all we need to take over the system. Token part 2 = a56

token2 = "a56"

# https://salza.dk/xint/case-seastar-signal
for x in range(300):
    text = xint("/entities/seastar.php")
    print(text, end="", flush=True)

# _/"""\___/"""\_/"""\_/"""\_/\_/\_________/\_/"""\_/"""\___/\_/"""\___/\_/"""\_/\___/\___/\_/\_/\_/\___/"""\_/"""\_/"""\___/\_/\_/"""\___/\_/\_/\___/\_________/\_/\_/\_/"""\_/"""\___/"""\_/"""\_/"""\_/\_/\_________/\_/"""\_/"""\___/\_/"""\___/\_/"""\_/\___/\___/\_/\_/\_/\___/"""\_/"""\_/"""\___/\_/\_
# Morse code
print(message("WAREHOUSE 38"))
# Excellent. You deciphered the communication. We will send in the team. Token part 3 = 49h

token3 = "49h"

# Bonus Adventure: https://salza.dk/xint/case-livingstone

# https://salza.dk/xint/attachments/livingstone-01.png contains letters "NTA" on a brick wall. This is part of a word.
# https://maps.co/gis/
# https://www.google.com/maps/place/Montafon+Self+Catering+Simons+Town/@-34.1973372,18.4477341,3a,30.2y,-20.23h,79.98t/data=!3m7!1e1!3m5!1sal58atYlVFCVH-3M8XnQmw!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D10.021956104850702%26panoid%3Dal58atYlVFCVH-3M8XnQmw%26yaw%3D-20.22932313158054!7i16384!8i8192!4m6!3m5!1s0x1dcc3e369c65a4ad:0x92e38f35f6a9cc8a!8m2!3d-34.1970699!4d18.44741!16s%2Fg%2F11c38h983v?hl=en-AU&entry=ttu&g_ep=EgoyMDI1MDgwNi4wIKXMDSoASAFQAw%3D%3D

print(message("montafon"))
# Awesome! Here is your reward:
# https://salza.dk/xint/attachments/reward-livingstone.png

print(f"https://salza.dk/xint/level2?token={token1}{token2}{token3}")
# https://salza.dk/xint/level2?token=fu2a5649h

#                                   Level 2
#                                  Qualified
#
# --------------------------------------------------------------------------------
#
# Great. I see you have uptained the Level 2 token.
#
# You have reached the end so far. If you had fun, let me known you reached this
# point. It will motivate me to accelerate an update with more cases.
#
# You can reach me at: salza(at)salza.dk
#
# Cases:
#   - No cases yet
#
# Bonus Adventure:
#   - No cases yet
