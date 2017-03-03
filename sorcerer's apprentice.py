import linkbot3 as linkbot
import math
import time

# Change yourt name here
robot = linkbot.CLinkbot("9wl4") 

def play_song(song, tempo):
    beat = 60./tempo
    freq = {"A440":440, 'R': 0, '':0, 'C':440*2**(3/12), 'C#':440*2**(4/12), 'Db':440*2**(4/12), 'D':440*2**(5/12), 'D#':440*2**(6/12), 'Eb':440*2**(6/12), 'E':440*2**(7/12), 'E#':440*2**(8/12), 'F':440*2**(8/12), 'F#':440*2**(9/12), 'Gb':440*2**(9/12), 'G':440*2**(10/12), 'G#':440*2**(11/12), 'Ab':440*2**(11/12), 'A':440*2**(12/12), 'A#':440*2**(13/12), 'Bb':440*2**(13/12), 'B':440*2**(14/12), 'Fb':440*2**(7/12), 'B#':440*2**(3/12)}
    for note in song:
        if not note[0] in freq:
            print("Error: '" + note[0] + "' is not a valid note name.")
            break
        robot.buzzer.set_frequency(freq[note[0]] * 2 ** (note[1] - 5))
        time.sleep(note[2] * beat)
    robot.buzzer.set_frequency(0)

sorcerer = [ 
#1 Stuckey
    ['G', 5, 1],
    ['R', 0, .5],
    
#2 stuckey
    ['D', 6, 1],
    ['R', 0, .5],
#3 stuckey
    ['D', 5, 1],
    ['E', 5, 1],
    ['F#', 5, 1],

#4 Black Matt
    ['G', 5, 1],
    ['R', 0, .5],
    ['Bb', 5, 1],

    
#5 Brooke
    ['G', 5, 1],
    ['R', 0, .5],
    ['Bb', 5, 1],


#6 Ejae
    ['A', 5, 1],
    ['G', 5, 1],
    ['F#', 5, 1],

#7 Qunicy
    ['G', 5, 1],
    ['R', 0, 1],
    ['Bb', 5, 1],

#8 Arianna 
    ['G', 5, 1],
    ['R', 0, 1],
    ['Bb', 5, 1],
#9 Riley
    ['A', 5, 1],
    ['G', 5, 1],
    ['F#', 5, 1],

#10 Arshdeep
    ['G', 5, 1],
    ['R', 0, .5],
    ['Bb', 5, 1],

#11 Ejae 
    ['G', 5, 1],
    ['Bb', 5, 1],
    ['A', 5, 1],

#12 Isaiah
    ['G', 5, 1],
    ['A', 5, 1],
    ['Bb', 5, 1],

#13 Jackson
    ['A', 5, 1],
    ['C', 6, 1],
    ['Bb', 5, 1],
 
#14 Alex
    ['A', 5, 1],
    ['R', 0, .5],
    ['C#', 6, 1],

#15 Kailah
    ['G', 5, 1], 
    ['R', 0, .5], 
    ['Bb', 5, 1],
 
#16 Sarah
    ['A', 5, 1],
    ['C', 6, 1], 
    ['Bb', 5, 1],


#17 Lakia
    ['A', 5, 1],
    ['R', 0, .5],
    ['C#', 6, 1],

#18 Harris 
    ['G', 5, 1],
    ['R', 0, 1],
    ['Bb', 5, 1],

#19 Trinity
    ['A', 5, 1],
    ['Bb', 5, 1],
    ['C', 6, 1],

#20 Amy
    ['D', 6, .7],
    ['R', 0, .1],
    ['D', 6, .7],
    ['R', 0, .1],
    ['D', 6, .7],
    ['R', 0, .1],
    
 #21 DJ
    ['D', 6, .7],
    ['R', 0, .1],
    ['D', 6, .7],
    ['R', 0, .1],
    ['D', 6, .7],
    ['R', 0, .1],


#22 Arianna 
    ['D', 6, 1],
    ['C', 6, 1],
    ['Bb', 5, 1],

#23 Black Matt
    ['A', 5, 1],
    ['C', 6, 1],
    ['Bb', 5, 1],
 
#24
    ['A', 5, 1],
    ['G', 5, 1],
    ['F', 5, 1],


#25
    ['F', 5, 1], 
    ['E', 5, 1],
    ['D', 5, 1],


#26 ejae
    ['C', 5, 1],
    ['Bb', 4, 1],
    ['A', 4, 1],

#27
    ['G', 4, 1],
    ['F', 4, 1],
    ['E', 4, 1],

#28 Black Matt
    ['D', 4, 1],
    ['R', 0, 1],
    ['R', 0, 1],


    ]

play_song(sorcerer, 300)


