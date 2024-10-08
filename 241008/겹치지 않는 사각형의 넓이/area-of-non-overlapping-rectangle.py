def area(x1, y1, x2, y2):
    return (x2 - x1) * (y2 - y1)

def overlap(x1, y1, x2, y2, x3, y3, x4, y4):
    overlap_x = max(0, min(x2, x4) - max(x1, x3))
    overlap_y = max(0, min(y2, y4) - max(y1, y3))
    return overlap_x * overlap_y

ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
mx1, my1, mx2, my2 = map(int, input().split())

area_A = area(ax1, ay1, ax2, ay2)
area_B = area(bx1, by1, bx2, by2)

overlap_A = overlap(ax1, ay1, ax2, ay2, mx1, my1, mx2, my2)
overlap_B = overlap(bx1, by1, bx2, by2, mx1, my1, mx2, my2)

remaining_area = (area_A - overlap_A) + (area_B - overlap_B)
print(remaining_area)