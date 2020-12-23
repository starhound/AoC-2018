raw_data = open('input.txt', 'r')

freqs = raw_data.readlines()
current_freq = 0
freq_list = []

for freq in freqs:
    sign = freq[:1]
    if sign == '+':
        value = freq[1:]
        current_freq += int(value)
    elif sign == '-':
        value = freq[1:]
        current_freq -= int(value)

print(current_freq)
