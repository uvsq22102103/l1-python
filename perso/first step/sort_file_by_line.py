bands = []

request_filename = r"C:\Users\Aymeric Goudout\Documents\repository info\l1-python\perso\first step\bands.txt"
with open(request_filename) as fin:
    for line in fin :
        bands.append(line.strip())

bands.sort()
print(bands)

output_filename = r"C:\Users\Aymeric Goudout\Documents\repository info\l1-python\perso\first step\test.txt"
with open(output_filename, 'w')as fout:
    for band in bands:
        fout.write(band+ '\n')