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
    # numbers to consider set here just for initial if.
    numbers_to_consider = input_list
    bit_count = str(input_list[0])

    for index, character in enumerate(bit_count):
        # for oxygen rating, get higher first number count from the count arrays. Higher number goes to oxygen.

        if len(numbers_to_consider) > 1:
            if one_count_array.get(index) >= zero_count_array.get(index):
                # more 1s in the bit count
                numbers_to_consider = get_numbers_with_starting_num_from_list_at_index(numbers_to_consider, 1, index)
            else:
                # more zeros
                numbers_to_consider = get_numbers_with_starting_num_from_list_at_index(numbers_to_consider, 0, index)

            zero_count_array, one_count_array = get_count_arrays_from_list(numbers_to_consider)

    final_oxygen = numbers_to_consider[0]

    # just set it to one of them at first
    zero_count_array, one_count_array = get_count_arrays_from_list(input_list)
    # numbers to consider set here just for initial if.
    numbers_to_consider = input_list

    for index, character in enumerate(bit_count):
        # for co2 rating, get lower first number count from the count arrays.
        if len(numbers_to_consider) > 1:
            if zero_count_array.get(index) <= one_count_array.get(index):
                # more 1s in the bit count
                numbers_to_consider = get_numbers_with_starting_num_from_list_at_index(numbers_to_consider, 0, index)
            else:
                # more zeros
                numbers_to_consider = get_numbers_with_starting_num_from_list_at_index(numbers_to_consider, 1, index)
            zero_count_array, one_count_array = get_count_arrays_from_list(numbers_to_consider)
    final_co2 = numbers_to_consider[0]

    oxygen_decimal = int(final_oxygen, 2)
    co2_decimal = int(final_co2, 2)
    life_support_rating = oxygen_decimal * co2_decimal
    print(f'Life support rating: {life_support_rating}')


def get_numbers_with_starting_num_from_list_at_index(list_to_search, num_to_match, index_to_observe):
    match_list = []

    for item in list_to_search:
        for char_index, character in enumerate(item):
            if char_index == index_to_observe:
                if int(item[index_to_observe]) == int(num_to_match):
                    match_list.append(item)
            elif char_index > index_to_observe:
                continue

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
