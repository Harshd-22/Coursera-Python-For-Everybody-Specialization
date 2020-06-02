name = input("Enter file:")
if len(name) < 1 : 
    name = "mbox-short.txt"
handle = open(name)

bigcount = None
bigword = None
counts = dict()
lst = list()

for line in handle:
    if not line.startswith("From "):
        continue
    line = line.rstrip()
    line = line.split()
    lst.append(line[1])

for i in lst:
    counts[i] = counts.get(i, 0) + 1
    
for k,v in counts.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v
        
print(bigword,bigcount)