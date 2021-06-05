t = int(input())
while(t>0):
    cats, dogs, legs = map(int, input().split())
    max_legs = (dogs + cats) * 4

if((2 * dogs) >= cats):
    min_legs = 4 * dogs


else:
    min_legs = (cats - (2*dogs)) * 4 + dogs * 4

# print(min_legs, max_legs)

if(legs < min_legs or legs > max_legs):
    print("no")

else:
    if(legs % 4 == 0):
        print("yes")
    else:
        print("no")
t -= 1
