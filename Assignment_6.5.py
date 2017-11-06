text = "X-DSPAM-Confidence:    0.8475";
x = text.find(':')

piece = text[x+1:]

num = float(piece)
print(num)