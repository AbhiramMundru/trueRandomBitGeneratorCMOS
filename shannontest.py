import math
binString = "10101010001010010000101010101010101010101010101010000101000101010101000010101000001010101010101010"
print("Output: " + str(binString))
ones=binString.count('1')
zeros=binString.count('0')
print("Number.of ones: " + str(ones))
print("Number of zeros: " + str(zeros))
p=ones/(ones+zeros)
ent=(-p*math.log2(p)) - ((1-p)*math.log2(1-p))
print("Entropy: " + str(ent))