#/usr/bin/python
import sys


with open(sys.argv[1]) as f:
    msgss = [a.split('\n') for a in f.read().split('\n\n\n')]
    for n, msgs in enumerate(msgss):
        with open('test/' + str(n) + '.csv', 'w') as g:
            g.write('0, 0, Header, 0, 1, ' + msgs[0] + '\n')
            g.write('1, 0, Start_track' + '\n')
            g.write('1, 0, Tempo, ' + msgs[1] + '\n')

            last = []
            current = []
            for i, x in enumerate(msgs[2]):
                if x == " ":
                    for note in last:
                        g.write('1, ' + str(i) + ', Note_off_c, 1, ' + str(note) + ', 96\n')
                    for note in current:
                        g.write('1, ' + str(i) + ', Note_on_c, 1, ' + str(note) + ', 96\n')
                    last = current
                    current = []
                else:
                    current.append(ord(x) - 33)
            g.write('1, ' + str(len(msgs[2])) + ', End_track\n')
            g.write('0, 0, End_of_file')

                
