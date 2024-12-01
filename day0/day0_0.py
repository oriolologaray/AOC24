misco = jones = []

with open('input.txt') as file:
    while line := file.readline():
        miscoj, ones = line.rstrip().split('   ')
        misco, jones = [*misco, int(miscoj)], [*jones, int(ones)]

misco, jones = sorted(misco), sorted(jones)

misco_jones = sum([abs(misc - ojones) for misc, ojones in zip(misco, jones)])

print(misco_jones)