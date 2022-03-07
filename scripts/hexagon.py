#!/usr/bin/python3

import sys
import ezdxf
import math

roundingPrecision = 5

if len(sys.argv) > 1:
    edgeLength = sys.argv[1]
else:
    edgeLength = 10
print(f"Output outline for edge length a = {edgeLength}")

# Create new dxf file and new modelspace
doc = ezdxf.new("R12")
msp = doc.modelspace()
# Create coordinates
coords = list()
for i in range(0, 360+60, 60):
    x = math.cos(math.radians(i))
    y = math.sin(math.radians(i))
    coords.append((round(x * edgeLength, ndigits=roundingPrecision), round(y * edgeLength, ndigits=roundingPrecision)))

print(coords)

for i in range(0, len(coords) - 1):
    msp.add_line(coords[i], coords[i + 1])

doc.saveas("hexagon_outline.dxf")
