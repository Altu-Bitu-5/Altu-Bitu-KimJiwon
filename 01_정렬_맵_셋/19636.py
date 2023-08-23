w, basic, t = map(int, input().split())
day, d_input, d_output = map(int, input().split())

w1 = w
w2 = w
basic2 = basic

for _ in range(day):
    w1 += d_input - (basic + d_output)
    w2 += d_input - (basic2 + d_output)
    
    if abs(d_input - (basic2 + d_output)) > t:
        basic2 += (d_input - (basic2 + d_output)) // 2

if w1 <= 0:
    print("Danger Diet")
else:
    print(w1, basic)

if w2 <= 0 or basic2 <= 0:
    print("Danger Diet")
else:
    print(w2, basic2, "YOYO" if basic - basic2 > 0 else "NO")