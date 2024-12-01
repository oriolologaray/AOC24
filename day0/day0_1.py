misco = jones = []

with open('input.txt') as file:
    while line := file.readline():
        miscoj, ones = line.rstrip().split('   ')
        misco, jones = [*misco, int(miscoj)], [*jones, int(ones)]

misco_jones = sum([misc * jones.count(misc) for misc in misco])

print(misco_jones)