"""
lista parte 02
"""


kpop = []

bts = ["JK", "Jimin", "Yoongi", "RM", "Tae", "jin", "hobi"]

ateez = [
    "Yunho", "san", "HJ", "jongho", "Woyuong", "seonghwa", "yeosang",
    "mingi"
]

kpop.append(bts[:])
bts[0] = "Jungkook"
bts[4] = "Taehyung"
kpop.append(ateez[:])
print(kpop[0][0], bts[0])
