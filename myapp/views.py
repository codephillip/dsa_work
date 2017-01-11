from django.shortcuts import render

from myapp.models import Topic, SubTopic, Member


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