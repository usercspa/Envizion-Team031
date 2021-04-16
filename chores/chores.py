from chores import Chores

chores = Chores('John Mary'.split())

for c in chores:
    status = 'name' if c.istitle() else 'other'
    chores.mark(c, status)

print chores.count('name'), "names,", \
      chores.count('^name'), "others"