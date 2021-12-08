def first_scenario(self):
    gamma_rate = ''
    epsilon_rate = ''

    zero_count_array, one_count_array = get_count_arrays_from_list(input_list)

    # gamma rate is most used item per index
    for index in range(0, len(zero_count_array)):
        # find out which is higher or lower per index
        zero_num = zero_count_array[index]
        one_num = one_count_array[index]

        if zero_num > one_num:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'

    # convert numbers to binary
    print(f'Gamma Rate: {gamma_rate}')
    print(f'Epsilon Rate: {epsilon_rate}')

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    power_conversion_rate = gamma_rate * epsilon_rate

    print(f'Scenario One Power Conversion Rate is {power_conversion_rate}')


def second_scenario(self):
    zero_count_array, one_count_array = get_count_arrays_from_list(input_list)
    numbers_to_consider = []

    # TODO make this a recursey boi

    # for oxygen rating, get higher first number count from the count arrays. Higher number goes to oxygen.
    # Lower number goes to CO2 scrubber rating
    if one_count_array.get(0) >= zero_count_array.get(0):
        # go with 1 count array
        numbers_to_consider = get_numbers_with_starting_num_from_list_at_index(one_count_array, 1, 0)
    else:
        # go with 0 count array
        numbers_to_consider = get_numbers_with_starting_num_from_list_at_index(zero_count_array, 0, 0)


def get_numbers_with_starting_num_from_list_at_index(list_to_search, num_to_match, index_to_observe):
    match_list = []

    for index in range(0, len(list_to_search)):
        if list_to_search[index][index_to_observe] == num_to_match:
            match_list.append(list_to_search[index])

    return match_list


def get_count_arrays_from_list(list_to_search):
    zero_count_array = {}
    one_count_array = {}

    for index in range(0, len(list_to_search)):
        for char_index, character in enumerate(list_to_search[index]):
            # initialize dictionaries dynamically
            if not zero_count_array.get(char_index, None):
                zero_count_array[char_index] = 0
            if not one_count_array.get(char_index, None):
                one_count_array[char_index] = 0

            char_index = int(char_index)
            character = int(character)

            if character == 0:
                zero_count_array[char_index] += 1
            if character is 1:
                one_count_array[char_index] += 1
    return zero_count_array, one_count_array


if __name__ == '__main__':
    input_string = input('Enter coordinates separated by a comma. NOTE for a long list of numbers, put them in a file and < it into the script with "python3 dive.py < file.txt".: \n')
    input_list = input_string.split(',')
    first_scenario(input_list)
    second_scenario(input_list)