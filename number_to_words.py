complete_number = input('Enter a number: ')

cardinal_word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 
              'eleven', 'tweleve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_word = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7 : 'seventy', 8: 'eighty', 9: 'ninety'}

number_arr = []
l = len(complete_number)
for i in range(l // 7 + 1):
    number_arr = [complete_number[-7 * (i + 1) : l if -7 * i == 0 else -7 * i]] + number_arr
    
def number_to_word(number):
    if number == '0':
        return cardinal_word[0]
    length = len(number)
    s = ''
    i = 0
    while i < length:
        digit = int(number[i])
        if digit == 0:
            i += 1
            continue

        if length - i == 7:
            if digit == 1:
                s += cardinal_word[int(number[i : i+2])] + ' lakh '
                i += 1
            else:
                s += tens_word[digit] + ' '
        elif length - i == 6:
            s += cardinal_word[digit] + ' lakh '
        elif length - i == 5:
            if digit == 1:
                s += cardinal_word[int(number[i : i+2])] + ' thousand '
                i += 1
            else:
                s += tens_word[digit] + ' '
        elif length - i == 4:
            s += cardinal_word[digit] + ' thousand '
        elif length - i == 3:
            s += cardinal_word[digit] + ' hundred '
        elif length - i == 2:
            if digit == 1:
                s += cardinal_word[int(number[i : i+2])]
                i += 1
            else:
                s += tens_word[digit] + ' '
        elif length - i == 1:
            s += cardinal_word[digit]
        i += 1

    return s

s = ''
for number in number_arr[:-1]:
    s += number_to_word(number) + ' crore '

s += number_to_word(number_arr[-1])

print(s)