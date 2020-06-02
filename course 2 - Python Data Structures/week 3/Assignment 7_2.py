count = 0
value = 0

fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    pos = line.find("0")
    value = value + float(line[pos:])
    count = count + 1

avg = value/count
print("Average spam confidence:",avg)