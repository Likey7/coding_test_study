from collections import deque

def count_ice(tray):
    n = len(tray)
    m = len(tray[0])
    ice = 0

    queue = deque(tray[0][0])
    while queue:




