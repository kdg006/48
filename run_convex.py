#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void
from straight import Straight

f = Void()
Straight.set_straight()
try:
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}\n")
        print(f"Number = {f.count}\n")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
