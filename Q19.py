# "99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips,
# as it has a very repetitive format which is easy to memorize, and can take a long time to sing. The song's
# simple lyrics are as follows:
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down, pass it around, 98 bottles of beer on the wall.

i=99
while i>0:
    print(f"""{i} bottles of beer on the wall, {i} bottles of beer.
    Take one down, pass it around, {i-1} bottles of beer on the wall.""")
    i=i-1