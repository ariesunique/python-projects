import csv
import re
from collections import namedtuple
import heapq

def question1():
    print("\n\nQuestion 1. Using vanilla csv reader")
    count = 0
    hw1_sum = 0
    hw2_sum = 0
    test1_sum = 0
    test2_sum = 0
    with open("grades.csv") as f:
        f.readline() # skip header
        data = csv.reader(f)
        for row in data:
            print(row)
            count+= 1
            hw1_sum += int(row[2])
            hw2_sum += int(row[3])
            test1_sum += int(row[5])
            test2_sum += int(row[6])

    print(f"The avg for hw1 is {hw1_sum/count:0.2f}, for hw2 is {hw2_sum/count:0.2f}, for test1 is {test1_sum/count:0.2f}, and for test2 is {test2_sum/count:0.2f}")

    
def question2():
    print("\n\nQuestion 2. Using DictReader")
    hw1_sum = 0
    hw2_sum = 0
    test1_sum = 0
    test2_sum = 0
    count = 0
    with open("grades.csv") as f:
        f.readline() # eliminate header since we're using our own
        reader = csv.DictReader(f, fieldnames = ("last", "first", "hw1", "hw2", "hw3", "test1", "test2"))
        for row in reader:
            print(row)
            count+=1
            hw1_sum += int(row["hw1"])
            hw2_sum += int(row["hw2"])
            test1_sum += int(row["test1"])
            test2_sum += int(row["test2"])
    
    print(f"HW1 avg: {hw1_sum/count:0.2f}, HW2 avg: {hw2_sum/count:0.2f}, Test1 avg: {test1_sum/count:0.2f}, Test2 avg: {test2_sum/count:0.2f}")   
    
    
def question3():
    print("\n\nQuestion 3. Using NamedTuple")
    count = 0
    hw1_sum = 0
    hw2_sum = 0
    test1_sum = 0
    test2_sum = 0
    with open("grades.csv") as f:
        f.readline() # skip headers
        reader = csv.reader(f)
        Row = namedtuple('Row', ("last","first","hw1","hw2","hw3","test1","test2"))
        for r in reader:
            row = Row(*r)
            print(row)
            count+=1
            hw1_sum += int(row.hw1)
            hw2_sum += int(row.hw2)
            test1_sum += int(row.test1)
            test2_sum += int(row.test2)
    print(f"HW1 avg: {hw1_sum/count:0.2f}, HW2 avg: {hw2_sum/count:0.2f}, Test1 avg: {test1_sum/count:0.2f}, Test2 avg: {test2_sum/count:0.2f}")   
    
    
    
def question4():
    print("\n\nQuestion 4. Each student's grades order by last name.")
    data = []
    Result = namedtuple('Result', ["last", "first", "hw_grade", "test_grade"])
    with open("grades.csv") as f:
        f.readline() # skip the header
        reader = csv.reader(f)
        Row = namedtuple('Row', ["last","first","hw1","hw2","hw3","test1","test2"])
        for r in reader:
            row = Row(*r)
            hw_grade = (int(row.hw1) + int(row.hw2)) / 2
            test_grade = (int(row.test1) + int(row.test2))/2
            data.append(Result(row.last.strip(), row.first.strip(), hw_grade, test_grade))
    sorted_data = sorted(data, key=lambda res:res.last)
    print("{:15} {:15} {:10} {:10}".format("Last Name", "First Name", "HW Average", "Test Average" ))
    for result in sorted_data:
        print("{:15} {:15} {:10} {:10}".format(result.last, result.first, result.hw_grade, result.test_grade))
        
    

def question5():
    print("\n\nQuestion 5. Show cumulative grade for each student and print highest student.")
    data = []
    Result = namedtuple("Result", ["last", "first", "cum_grade"])
    with open("grades.csv") as f:
        f.readline() # skip the header
        reader = csv.reader(f)
        Row = namedtuple("Row", ["last","first","hw1","hw2","hw3","test1","test2"])
        for r in reader:
            row = Row(*r)
            hw_avg = (int(row.hw1) + int(row.hw2))/2
            test_avg = (int(row.test1) + int(row.test2))/2
            # Remember to normalize the data; you need to multiply the hw grade by 10 to get both averages out of 100
            cum_grade = .3*hw_avg*10 + .7*test_avg 
            data.append(Result(row.last.strip(), row.first.strip(), cum_grade))
    print("{:15} {:15} {:>10}".format("Last", "First", "Cum Grade"))
    print("="*42)
    for res in data:
        print("{:15} {:15} {:10.2f}".format(res.last, res.first, res.cum_grade))
    highest_student = max(data, key=lambda res: res.cum_grade)
    print("Student with the highest grade is {} {} with a cumulative grade of {:0.2f}".format(highest_student.first, highest_student.last, highest_student.cum_grade))
    
    
    
    
    
    
def question6():
    print("\n\nQuestion 6. Show cumulative grade for each student and determine the top 3 students.")
    data = []
    Result = namedtuple("Result", ["last", "first", "cum_grade"])
    with open("grades.csv") as f:
        f.readline() # skip header
        reader = csv.reader(f)
        Row = namedtuple("Row", ["last", "first", "hw1", "hw2", "hw3", "test1", "test2"])
        for r in reader:
            row = Row(*r)
            hw_avg = (int(row.hw1) + int(row.hw2))/2 * 10
            test_avg = (int(row.test1) + int(row.test2))/2
            cum_grade = .3*hw_avg+ .7*test_avg
            data.append(Result(row.last.strip(), row.first.strip(), cum_grade))
    data.sort(key=lambda res: res.cum_grade, reverse=True)
    #sorted_data = sorted(data, key=lambda res: res.cum_grade, reverse=True)
    print("{:15} {:15} {:>10}".format("Last", "First", "Grade"))
    print("="*42)
    for res in data:
        print(f"{res.last:15} {res.first:15} {res.cum_grade:10.2f}")
        
    top3 = heapq.nlargest(3, data, key=lambda res: res.cum_grade)
    print("\nThe top 3 students are {0.first}, {1.first}, and {2.first}, with cumulative grades of {0.cum_grade:.2f}, {1.cum_grade:.2f}, and {2.cum_grade:.2f}, respectively.".format(top3[0], top3[1], top3[2]))
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    question1()
    question2()
    question3()
    question4()
    question5()
    question6()