with open('file.txt', 'r') as info:
    for line in info:
        name, weight, height = line.strip().split(", ")

        bmi = int(weight) / ((int(height) / 100) ** 2)
        result = ""

        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print('\n'.join([name, str(bmi), result]))
        print()