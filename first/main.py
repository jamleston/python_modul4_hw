from pathlib import Path

def summary (arr):
    sum = 0
    for num in arr:
        sum = sum + num
    return sum

def median (arr):
    sum = summary(arr)
    num_of_workers = len(arr)
    median = sum/num_of_workers
    return median

def total_salary(path):
    try:
        with open(path, "r") as file:
            workers = [el.strip() for el in file.readlines()]
            salaries = []
            for worker in workers:
                worker_data = worker.split(',')
                salaries.append(int(worker_data[1]))
            sum = summary(salaries)
            med = int(median(salaries))
            result_tuple = (sum, med)
        return result_tuple
    except (TypeError, FileNotFoundError):
        answer = 'path is not correct'
        print(answer)
        return False, False

relative_path = Path("first\\data.txt")

result = total_salary(relative_path)
print(f'total: {result[0]}, average: {result[1]}')