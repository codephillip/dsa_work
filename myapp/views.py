from django.shortcuts import render
import timeit

from myapp.models import Topic, SubTopic, Member

mylist = [88298, 50207, 33162, 96619, 26507, 55409, 29664, 58815, 43325, 58561]


def index(request):
    return render(request, 'index.html')


def dsa_notes(request):
    topics = Topic.objects.all()
    return render(request, 'dsa_notes.html', {
        'topics': topics
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


def sorting(request, pk):
    topic = Topic.objects.get(pk=pk)
    sub_topics = SubTopic.objects.filter(topic=topic)
    return render(request, 'sorting.html', {
        'sub_topics': sub_topics,
    })


def single_sort(request, pk):
    timelist = []
    sub_topic = SubTopic.objects.get(pk=pk)
    t = timeit.Timer(lambda: bubble_sort(mylist))
    timelist.append(t.timeit(number=1))
    t = timeit.Timer(lambda: insertion_sort(mylist))
    timelist.append(t.timeit(number=1))
    t = timeit.Timer(lambda: selection_sort(mylist))
    timelist.append(t.timeit(number=1))
    t = timeit.Timer(lambda: merge_sort(mylist))
    timelist.append(t.timeit(number=1))
    t = timeit.Timer(lambda: quick_sort(mylist))
    timelist.append(t.timeit(number=1))

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
