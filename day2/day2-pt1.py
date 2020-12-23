import collections

# prepare data
raw_data = open("input.txt", 'r')
codes = raw_data.readlines()
# remove all newlines per code
codes = list(map(lambda s: s.strip(), codes))

two_letter_count = 0
three_letter_count = 0

for code in codes:
    d = collections.Counter(code)
    for item in d.items():
        if item[1] == 2:
            two_letter_count += 1
            break

for code in codes:
    d = collections.Counter(code)
    for item in d.items():
        if item[1] == 3:
            three_letter_count += 1
            break

print("Two Letters: " + str(two_letter_count))
print("Three Letters: " + str(three_letter_count))

print("Checksum: " + str(two_letter_count * three_letter_count))
