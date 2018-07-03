import os
import subprocess

folder = 'rag'
midis = os.listdir(folder)
training = open('training', 'w')

# for midi in ['mapleaf2.mid']:
for midi in midis:
    data = [x.split(', ') for x in subprocess.run(['midicsv', folder + '/' + midi], stdout=subprocess.PIPE).stdout.decode(errors='ignore').split('\n')]
    # print(data[0])

    out = ""
    for entry in data:
        if entry[2] == 'Header':
            out += entry[5] + '\n'
        elif entry[2] == 'Tempo':
            out += entry[3] + '\n'
            break
    notes = ['' for x in range(int(data[-3][1]))]
    for entry in data:
        if entry[2] == 'End_of_file':
            break
        elif entry[2] == 'Note_on_c' and entry[5] != '0':
            notes[int(entry[1])] += chr(33+int(entry[4]))
            # current += chr(33+int(entry[4]))
        # elif entry[2] == 'Note_off_c' or (len(entry) > 5 and entry[2] == 'Note_on_c' and entry[5] == '0'):
            # current = current.replace(chr(33+int(entry[4])), '')
        # out += current + " "
    out += " ".join(notes)
    training.write(out + '\n\n\n')
