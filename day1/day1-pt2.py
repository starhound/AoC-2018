raw_data = open('input.txt', 'r')

freqs = raw_data.readlines()
freq_list = [0]
has_second = False


def calculate():
    current_freq = 0
    for freq in freqs:
        sign = freq[:1]
        if sign == '+':
            value = freq[1:]
            current_freq += int(value)
            if current_freq in freq_list:
                print("Second Freq: " + str(current_freq))
                return True
            else:
                freq_list.append(current_freq)
        elif sign == '-':
            value = freq[1:]
            current_freq -= int(value)
            if current_freq in freq_list:
                print("Second Freq: " + str(current_freq))
                return True
            else:
                freq_list.append(current_freq)
    return False


while True:
    found = calculate()
    if found:
        break
