name = input("Enter file:")
if len(name) < 1 : 
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
lst = list()
tmp = list()

for line in handle:
    if not line.startswith("From "):
        continue
    line = line.rstrip()
    line = line.split()
    numbers = line[5].split(':')
    lst.append(numbers[0])

for i in lst:
    counts[i] = counts.get(i, 0) + 1
   
for k,v in counts.items():
    tmp.append((k,v))

tmp = sorted(tmp)

for k,v in tmp:
    print(k,v)