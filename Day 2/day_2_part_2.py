min_difference = 1
max_difference = 3

def is_sorted(report):
    return all(report[i] <= report[i + 1] for i in range(len(report) - 1)) or \
           all(report[i] >= report[i + 1] for i in range(len(report) - 1))

def is_valid_report(report):
    return is_sorted(report) and all(
        min_difference <= abs(report[i + 1] - report[i]) <= max_difference for i in range(len(report) - 1)
    )

def check_with_fail_tolerance(report):
    if is_valid_report(report):
        return True

    for i in range(len(report)):
        original = report[i]
        report[i] = None
        reduced_report = [element for element in report if element is not None]

        if is_valid_report(reduced_report):
            report[i] = original
            return True

        report[i] = original

    return False

with open('day_2_input.txt') as file:
    report_list = (list(map(int, line.split())) for line in file if line.strip())
    correct_reports = sum(1 for report in report_list if check_with_fail_tolerance(report))

print('Correct Reports:', correct_reports)
