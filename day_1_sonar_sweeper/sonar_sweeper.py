class SonarSweeper(object):
    def run(self, input_list):
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
        print(f'Sonar Increased by {increase_count}')


if __name__ == '__main__':
    input_string = input('Enter coordinates separated by a space. NOTE for a long list of numbers, put them in a file and < it into the script with "python3 sonar_sweeper.py < file.txt".: \n')
    input_list_temp = input_string.split()

    # convert each item to int type
    for i in range(0, len(input_list_temp)):
        # convert each item to int type
        input_list_temp[i] = int(input_list_temp[i])

    SonarSweeper().run(input_list_temp)