import math

x1, y1, r1, x2, y2, r2 = map(float, input().split())

d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

if r1 > r2:
    r1, r2 = r2, r1

ans = 0
if d < r1 + r2:
    if d < r2 - r1:
        ans = math.pi * r1**2
    else:
        rad1 = math.acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
        rad2 = math.acos((d**2 + r2**2 - r1**2) / (2 * d * r2))

        sector1 = r1**2 * rad1
        sector2 = r2**2 * rad2
        triangle1 = r1**2 * math.cos(rad1) * math.sin(rad1)
        triangle2 = r2**2 * math.cos(rad2) * math.sin(rad2)

        ans = sector1 + sector2 - triangle1 - triangle2

print('{:0.3f}'.format(ans))
