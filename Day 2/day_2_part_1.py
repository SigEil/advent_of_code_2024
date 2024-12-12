correct_reports = 0
min_difference = 1
max_difference = 3
with open('day_2_input.txt') as file:
    report_list = (list(map(int, line.split())) for line in file if line.strip())

    for report in report_list:
        if report == sorted(report) or report == sorted(report, reverse=True):
            for i in range(len(report) - 1):
                difference = abs(report[i] - report[i + 1])
                if not (min_difference <= difference <= max_difference):
                    break
            else:
                correct_reports += 1

print('Correct Report:', correct_reports)