import csv
import timeit

name_of_file = {1000:"data_to_sort/one_thousand.csv",
                10000:"data_to_sort/ten_thousand.csv",
                50000:"data_to_sort/fifty_thousand.csv",
                100000:"data_to_sort/one_hundred_thousand.csv",
                500000:"data_to_sort/five_hundred_thousand.csv",
                1000000:"data_to_sort/one_million.csv",
                3000000:"data_to_sort/three_millions.csv"}

def read_data(amount_data=name_of_file[1000]):
    numbers = []
    with open(amount_data, "r") as f:
        csv_reader = csv.reader(f, delimiter=' ')
        for amount in csv_reader:
            for one_amount in amount:
                numbers.append(int(one_amount))
    return numbers
    # takes data from csv file to list and gives us unsorted list


def bubble_sort(numbers=read_data()):
    last_item = len(numbers) - 1
    for i in range(0, last_item):
        for y in range(0, last_item - i):
            if numbers[y] > numbers[y+1]:
                numbers[y], numbers[y+1] = numbers[y+1], numbers[y]
    return numbers
    #sorts our list with bubble sort and gives us sorted list 

def insertion_sort(numbers=read_data()):
    for i in range(1, len(numbers)):
        while i > 0 and numbers[i] < numbers[i - 1]:
            numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
            i -= 1
    return numbers
    #sorts our list with insertion sort and gives us sorted list


def save_data(numbers=bubble_sort()):
    with open("python-4th-si-week-sorting-algorithms-Val1706/sorted_data/sorted_.csv", "w") as f:
        csv_writer = csv.writer(f, delimiter=' ')
        for number in numbers:
            csv_writer.writerow(str(number))
        print("Done")
    #saves data with appropriate type of sorting ("bubble or insertion") to csv file in "sorted data" folder


def sort_data(amount_data=read_data(name_of_file[1000]), sort_type='insertion'):
    if sort_type == "bubble":
        bubble_sort(amount_data)
    elif sort_type == "insertion":
        insertion_sort(amount_data)
    return amount_data
    # sorts appropriate data with appropriate type of sort("bubble" or "insertion")

def get_computing_time(amount_data=name_of_file[1000], computing_type='bubble sort'):
    start = timeit.default_timer()
    if computing_type == "bubble sort":
        bubble_sort(numbers=read_data(amount_data))
    elif computing_type == "insertion sort":
        insertion_sort(numbers=read_data(amount_data))
    elif computing_type == "export data":
        save_data(numbers=bubble_sort(numbers=read_data(amount_data)))
    elif computing_type == "import data":
        read_data(amount_data)
    stop = timeit.default_timer()
    return str(int(stop - start) * 1000) + " ms"
    #shows us the time of operation depending on chosen file and chosen operation







#print(read_data())
#print(bubble_sort())
#print(insertion_sort())
#save_data()
#sort_data(amount_data=read_data(name_of_file[1000]), sort_type='insertion')
#print(get_computing_time()

