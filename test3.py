def load():
    filename = "input.txt"
    openfile = open(filename, 'r')
    results = {}

    for line in openfile:
        line = line.strip()
        line = line.split(' ')
        results[line[1]] = line[0]

    openfile.close()
    return results

def save(data):
    filename = "output.txt"
    openfile = open(filename, 'w')

    for key in data.keys():
        openfile.write(data[key])
        openfile.write(' ')
        openfile.write(key)
        openfile.write('\n')
    openfile.close()

save(load())
