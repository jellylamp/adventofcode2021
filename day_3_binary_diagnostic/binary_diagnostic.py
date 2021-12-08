class BinaryDiagnostic(object):

    @staticmethod
    def first_scenario(self):
        zero_count_array = {}
        one_count_array = {}
        gamma_rate = ''
        epsilon_rate = ''

        for index in range(0, len(input_list)):
            for char_index, character in enumerate(input_list[index]):
                # initialize dictionaries dynamically
                if not zero_count_array.get(char_index, None):
                    zero_count_array[char_index] = 0
                if not one_count_array.get(char_index, None):
                    one_count_array[char_index] = 0

                char_index = int(char_index)
                character = int(character)

                print(f'char_index {char_index}')
                print(f'character {character}')
                if character == 0:
                    zero_count_array[char_index] += 1
                if character is 1:
                    one_count_array[char_index] += 1

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


if __name__ == '__main__':
    input_string = input('Enter coordinates separated by a comma. NOTE for a long list of numbers, put them in a file and < it into the script with "python3 dive.py < file.txt".: \n')
    input_list = input_string.split(',')
    BinaryDiagnostic().first_scenario(input_list)
    # BinaryDiagnostic().second_scenario(input_list_temp)