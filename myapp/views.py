import time
from django.shortcuts import render
import timeit
import uuid

from myapp.models import Topic, SubTopic, Member, Student, Receipt, SortedReceipt


def index(request):
    students = Student.objects.all()
    receipts_list = []
    for x in range(students.count()):
        receipts_list.append(', '.join(map(str, Receipt.objects.filter(student_id=students[x].id))))
    print("receipts#")
    print(receipts_list)
    data = zip(students, receipts_list)
    # testing binary search
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(linear_search(testlist, 3))
    print(linear_search(testlist, 13))
    return render(request, 'index.html', {
        'data': data,
    })


def insert_students_and_receipts():
    for x in range(5):
        student = Student(name=str(uuid.uuid4().time)[0:8])
        student.save()
        for y in range(10):
            print(student)
            Receipt(student=student, number=str(uuid.uuid4().time)[0:5]).save()


def sorting(request):
    insert_students_and_receipts()
    students = Student.objects.all()
    receipts_list = []
    for x in range(students.count()):
        receipts_list.append(', '.join(map(str, Receipt.objects.filter(student_id=students[x].id))))
    data = zip(students, receipts_list)
    return render(request, 'sorting.html', {
        'data': data,
    })


def about(request):
    members = Member.objects.all()
    return render(request, 'about.html', {
        'members': members
    })


def dsa_notes_details(request, pk):
    topic = Topic.objects.get(pk=pk)
    sub_topics = SubTopic.objects.filter(topic=topic)
    return render(request, 'dsa_notes_details.html', {
        'sub_topics': sub_topics,
        'topic': topic,
    })


def single_sort(request, pk):
    timelist = []
    sub_topic = SubTopic.objects.get(pk=pk)

    return render(request, 'single_sort.html', {
        'sub_topic': sub_topic,
        'timelist': timelist
    })


def bubble_sort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


def insertion_sort(alist):
    for index in range(1, len(alist)):

        current_value = alist[index]
        position = index

        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = current_value


def selection_sort(alist):
    for fill_slot in range(len(alist) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if alist[location] > alist[position_of_max]:
                position_of_max = location

        temp = alist[fill_slot]
        alist[fill_slot] = alist[position_of_max]
        alist[position_of_max] = temp


def merge_sort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
    print("Merging ", alist)


def quick_sort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark


def sorted_receipt(request, pk):
    # 1 for select_all, 2 for select 10
    if int(pk) == 1:
        print("value" + pk)
        students = Student.objects.all()
        timelist = select_all(students)
    else:
        print("value" + pk)
        students = Student.objects.all()[:10]
        timelist = select_ten(students)
    receipts_list = []
    for x in range(students.count()):
        receipts_list.append(', '.join(map(str, SortedReceipt.objects.filter(student_id=students[x].id))))
    title = ['bubble sort', 'insertion sort', 'selection sort', 'merge sort', 'quick sort']
    data = zip(students, receipts_list)
    graph_data = zip(title, timelist)
    print("sortedreceipt")
    print(receipts_list)
    return render(request, 'sorted.html', {
        'data': data,
        'timelist': timelist,
        'title': title,
        'graph_data': graph_data
    })


def select_all(student):
    print("started")
    bubble_sort_time = 0
    insertion_sort_time = 0
    selection_sort_time = 0
    merge_sort_time = 0
    quick_sort_time = 0
    for stn in student:
        mylist = Receipt.objects.filter(student_id=stn.id)
        receipt_list = []
        for x in mylist:
            receipt_list.append(x.number)
        print("receipt_select")
        print(mylist)
        t = timeit.Timer(lambda: bubble_sort(receipt_list))
        bubble_sort_time += t.timeit(number=1)

        # todo implement deletion of old data

        # inserts sorted receipts
        for y in receipt_list:
            SortedReceipt(number=y, student=stn).save()

        t = timeit.Timer(lambda: insertion_sort(receipt_list))
        insertion_sort_time += t.timeit(number=1)
        t = timeit.Timer(lambda: selection_sort(receipt_list))
        selection_sort_time += t.timeit(number=1)
        t = timeit.Timer(lambda: merge_sort(receipt_list))
        merge_sort_time += t.timeit(number=1)
        t = timeit.Timer(lambda: quick_sort(receipt_list))
        quick_sort_time += t.timeit(number=1)
        print("insertion_sort# " + str(insertion_sort_time))
    timelist = [bubble_sort_time, insertion_sort_time, selection_sort_time, merge_sort_time, quick_sort_time]
    return timelist


def select_ten(student):
    print("started")
    print("count student# " + str(student.count()))
    bubble_sort_time = 0
    insertion_sort_time = 0
    selection_sort_time = 0
    merge_sort_time = 0
    quick_sort_time = 0
    for x in student:
        mylist = Receipt.objects.filter(student_id=x.id)
        receipt_list = []
        for x in mylist:
            receipt_list.append(x.number)
        print("receipt_select")
        print(mylist)
        t = timeit.Timer(lambda: bubble_sort(receipt_list))
        bubble_sort_time += t.timeit(number=1)
        t = timeit.Timer(lambda: insertion_sort(receipt_list))
        insertion_sort_time += t.timeit(number=1)
        t = timeit.Timer(lambda: selection_sort(receipt_list))
        selection_sort_time += t.timeit(number=1)
        t = timeit.Timer(lambda: merge_sort(receipt_list))
        merge_sort_time += t.timeit(number=1)
        t = timeit.Timer(lambda: quick_sort(receipt_list))
        quick_sort_time += t.timeit(number=1)
        print("insertion_sort# " + str(insertion_sort_time))
    timelist = [bubble_sort_time, insertion_sort_time, selection_sort_time, merge_sort_time, quick_sort_time]
    return timelist


def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    item = int(item)
    print(type(item))

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            print("IF")
            found = True
        else:
            print("ELSE")
            print(alist[midpoint])
            print(item)
            print(type(alist[midpoint]))
            print(type(item))

            if item < alist[midpoint]:
                last = midpoint - 1
                print("LAST")

            else:
                first = midpoint + 1
                print("FIRST")

    return found


def linear_search(receipts, item):
    print("started linear search")
    for x in receipts:
        print("seaching#" + str(x))
        if str(x) == str(item):
            print("found item")
            return True
    return False


def searching(request, item):
    receipts = Receipt.objects.all()
    found = False

    receipt_list = []
    for x in receipts:
        receipt_list.append(x.number)

    print("receipt#")
    print(receipt_list)

    start = time.time()
    found = linear_search(receipt_list, item)
    stop = time.time()
    l_time = stop - start
    print(found)

    start = time.time()
    found = binary_search(receipt_list, item)
    stop = time.time()
    b_time = stop - start
    timelist = [l_time, b_time]
    print(found)

    graph_data = zip(['Linear Search', 'Binary Search'], timelist)

    return render(request, 'searched.html', {
        'found': found,
        'graph_data': graph_data
    })
