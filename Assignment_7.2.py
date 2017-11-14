# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0
avg = 0
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:"):
		continue
	count += 1
	num = float(line[21:])
	tot += num
avg = tot / count
print('Average spam confidence:', avg)
