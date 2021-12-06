class Dive(object):

    @staticmethod
    def first_scenario(self):
        depth = 0
        horizontal_pos = 0

        # convert each item to int type
        for index in range(0, len(input_list_temp)):
            current_direction, current_direction_count_str = input_list_temp[index].split()
            current_direction_count = int(current_direction_count_str)

            if current_direction == 'forward':
                horizontal_pos += current_direction_count
            elif current_direction == 'down':
                depth += current_direction_count
            elif current_direction == 'up':
                depth -= current_direction_count

        multiplied = depth * horizontal_pos
        print(f'Scenario 1 output is {multiplied}')


if __name__ == '__main__':
    input_string = input('Enter coordinates separated by a comma. NOTE for a long list of numbers, put them in a file and < it into the script with "python3 dive.py < file.txt".: \n')
    input_list_temp = input_string.split(',')
    Dive().first_scenario(input_list_temp)