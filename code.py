input_str = input()

vowels = 'aeiouAEIOU'  # حروف صدادار
output_str = ''

for i in input_str:
    if i not in vowels:
        output_str += '.' + i.lower()

print(output_str)