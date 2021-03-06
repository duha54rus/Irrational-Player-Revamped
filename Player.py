from decimal import getcontext, Decimal
from miditime.miditime import MIDITime
from pathlib import Path
from os import system

getcontext().prec = 60
midifile = Path.home().joinpath('Desktop', 'irrational_music.mid')

number = abs(Decimal(input('Enter a positive number that doesn\`t have an integer square root: ')))
bpm = abs(int(input('Enter rhythm (speed) in BPM (beats per minute) 0-600: ')))
velocity = abs(int(input('Enter note velocity (loudness) 0-127: ')))
if velocity > 127: velocity = 127

playstring = str(number.sqrt()).replace('.', '', 1)
midiout = MIDITime(bpm, midifile)
notes = (68, 69, 71, 72, 74, 76, 77, 80, 81, 83)

midinotes = []
for time in range(len(playstring)):
    midinotes.append([
        time,
        notes[int(playstring[time])],
        velocity,
        1
    ])
midinotes[len(playstring) - 1][2] = velocity//2
midinotes[len(playstring) - 1][3] = 4

midiout.add_track(midinotes)
midiout.save_midi()
print('You can find the resulting "irrational_music.mid" file at your desktop')

system(str(midifile))

print('Thank you for listening!')