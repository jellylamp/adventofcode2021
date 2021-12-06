class SonarSweeper(object):

    @staticmethod
    def first_scenario(input_list):
        previous = 0
        increase_count = 0

        for index in range(0, len(input_list)):
            # skip first item
            if index == 0:
                continue
            current = input_list[index]
            if current > previous:
                increase_count += 1
            previous = current
        print(f'Scenario 1: Sonar Increased by {increase_count}')

    def second_scenario(self, input_list):
        first = 0
        second = 0
        previous_sum = 0
        increase_count = 0

        for index in range(0, len(input_list)):
            current = input_list[index]
            if index == 0:
                first = current
                continue
            elif index == 1:
                second = current
                continue

            current_sum = first + second + current

            # Don't count the first sum nothing to compare to
            if current_sum > previous_sum and index != 2:
                increase_count += 1

            first = second
            second = current
            previous_sum = current_sum

        print(f'Scenario 2: Sonar Increased by {increase_count}')


if __name__ == '__main__':
    input_string = input('Enter coordinates separated by a space. NOTE for a long list of numbers, put them in a file and < it into the script with "python3 sonar_sweeper.py < file.txt".: \n')
    input_list_temp = input_string.split()

    # convert each item to int type
    for i in range(0, len(input_list_temp)):
        # convert each item to int type
        input_list_temp[i] = int(input_list_temp[i])

    SonarSweeper().first_scenario(input_list_temp)
    SonarSweeper().second_scenario(input_list_temp)