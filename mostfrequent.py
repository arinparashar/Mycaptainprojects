def most_frequent(string):
    # letter frequencies will be stored here
    freq_dict = {}

    # frequency of each letter is counted
    for letter in string:
        freq_dict[letter] = freq_dict.get(letter, 0) + 1

    # dictionary is sorted in descneding order
    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    # finally the letter adn their frequencies are printed
    for letter, frequency in sorted_freq:
        print(f"{letter} = {frequency:02d}")

# for example
user_input = input("Please enter a string: ")
most_frequent(user_input)
