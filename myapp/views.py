from django.shortcuts import render

from myapp.models import Topic, SubTopic


def index(request):
    return render(request, 'index.html')


def dsa_notes(request):
    topics = Topic.objects.all()
    return render(request, 'dsa_notes.html', {
        'topics': topics
    })


def about(request):
    return render(request, 'about.html')


def dsa_notes_details(request, pk):
    topic = Topic.objects.get(pk=pk)
    sub_topics = SubTopic.objects.filter(topic=topic)
    return render(request, 'dsa_notes_details.html', {
        'sub_topics': sub_topics,
        'topic': topic,
    })
