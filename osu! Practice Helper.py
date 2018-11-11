'''
osu! Practice Helper

Very simple script to split beatmap into multiple chunks

Made by M8than (github.com/m8than)
'''

from os import system

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

system("title --- osu! Practice Helper ---")

fileName = input("Filename: ").replace('"','')
parts = int(input("Part count: "))

with open(fileName, 'r') as osuFile:
    beatmap = osuFile.read()

fileBefore = beatmap.split("[HitObjects]")[0]
versionName = beatmap.split("Version:")[1].split('\n')[0]

hitObjects = beatmap.split("[HitObjects]")[1].split("\n\n")[0].split('\n')

hitObjectParts = chunkIt(hitObjects, parts)

for i in range(len(hitObjectParts)):
    partString = " (OPH) Pt. " + str(i+1)
    with open(fileName.replace(".osu", partString + ".osu"), 'w') as newDiff:
        hitObjectString = '\n'.join(hitObjectParts[i])
        fileContent = fileBefore.replace(versionName, versionName + partString) + "[HitObjects]\n" + hitObjectString
        newDiff.write(fileContent)
