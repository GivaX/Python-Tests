def load():
    filename = "input.txt"
    openfile = open(filename, 'r')
    results = []

    for line in openfile:
        line = line.strip()
        line = line.split(' ')
        results.append(line)

    openfile.close()
    return results

def save(data):
    filename = "output.txt"
    openfile = open(filename, 'w')

    for line in data:
        for l in line:
            openfile.write(str(l))
            openfile.write(' ')
        openfile.write('\n')
    openfile.close()

save(load())
