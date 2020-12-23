raw_data = open('input.txt', 'r')

freqs = raw_data.readlines()
freq_list = [0]
current_freq = 0
found = False

while found is not True:
    for freq in freqs:
        sign = freq[:1]
        if sign == '+':
            value = freq[1:]
            current_freq = current_freq + int(value)
            print(current_freq)
            if current_freq in freq_list:
                print("Second Freq: " + str(current_freq))
                found = True
                break
            else:
                freq_list.append(current_freq)
        elif sign == '-':
            value = freq[1:]
            current_freq = current_freq - int(value)
            print(current_freq)
            if current_freq in freq_list:
                print("Second Freq: " + str(current_freq))
                found = True
                break
            else:
                freq_list.append(current_freq)
