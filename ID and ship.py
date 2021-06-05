def ship(id):
  id = id.upper()
  if id == 'B':
    return "BattleShip"
  if id == 'C':
    return "Cruiser"
  if id == 'D':
    return "Destroyer"
  if id == 'F':
    return "Frigate"

T = int(input())
res = []
for i in range(T):
  id = input()
  res.append(ship(id))

for i in res:
  print(i)
