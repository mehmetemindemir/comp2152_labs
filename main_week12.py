from mammal import Mammal
from person import Person
from puma import Puma
from tick import Tick

# Mammal instance
m = Mammal(10)
m.speak()
print(m)

# Person instance
p = Person("Mehmet", 30, 165)
p.speak()
print(p)
p.heart.beat()
print(p)

# Tick instance
t = Tick()
t.suck_blood()
print(t)

# Puma instance with Tick (aggregation)
pm = Puma(4, t)
pm.tick.suck_blood()
print(pm)
pm.claw()

pm2= Puma(4)
pm2.claw()
print(pm2)