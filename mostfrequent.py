def most_frequent(string):
    
    freq_dict = {}

    
    for letter in string:
        freq_dict[letter] = freq_dict.get(letter, 0) + 1

   
    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    
    for letter, frequency in sorted_freq:
        print(f"{letter} = {frequency:02d}")

# for example
user_input = input("Please enter a string: ")
most_frequent(user_input)
