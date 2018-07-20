from django.shortcuts import render
from .models import About, Experience, Education, Project, Skill, Interest


def profile(request):
    AboutMe = About.objects.all()
    MyExperience = Experience.objects.all()
    MyEducation = Education.objects.all()
    ProjectList = Project.objects.order_by('id')
    MySkills = Skill.objects.all()
    MyInterest = Interest.objects.all()

    context = {'ProjectList': ProjectList, 'AboutMe': AboutMe, 'MyExperience': MyExperience,
               'MyEducation': MyEducation, 'MySkills': MySkills, 'MyInterest': MyInterest}
    return render(request, 'myprofile/index.html', context)