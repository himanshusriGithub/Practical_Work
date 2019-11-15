import json
filename = 'PracticalWork.txt'
works = {}
with open(filename) as fh:
    for line in fh:
       work, description = line.strip().split(" " , 1)
       works[work] = description.strip()
print(json.dumps(works, indent=1, sort_keys=False))


