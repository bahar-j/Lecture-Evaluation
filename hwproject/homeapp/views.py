from django.shortcuts import render, redirect
from .models import *
from django.db.models.query_utils import Q
import requests

# post의 id와 lecture의 id 구분

def db(request):
    url = "http://18.214.131.153:5000/course"
    response = requests.get(url)
    data = response.json()['data']

    for i in data :
        lecture = Lecture()
        lecture.rq_year = i['rq_year']
        lecture.rq_semester = i['rq_semester']
        lecture.department = i['dept']
        lecture.area = i['area']
        lecture.instruction_number = i['instruction_number']
        lecture.title = i['subject']
        lecture.credit = i['credit']
        lecture.time = i['time']
        lecture.professor = i['professor']
        lecture.save()

    return redirect('/') #다 저장하고 나면 login.html로

def home(request):
    lectures = Lecture.objects.all()
    deptList = list()
    for lecture in lectures:
        deptList.append(lecture.department)
    deptList = list(set(deptList)) # 중복 제거
    deptList.sort()
    isTable = False # default는 테이블이 안보이는 상태로 설정

    return render(request,'home.html',{'lectures': lectures, 'deptList': deptList, 'isTable': isTable})

def search(request):
    lectures = Lecture.objects.all()
    deptList = list()
    for lecture in lectures:
        deptList.append(lecture.department)
    deptList = list(set(deptList))
    deptList.sort()
    isTable = True

    year = int(request.POST['year'][2:]) # db에 20, 19,.. 형식으로 저장되어 있어서
    semester = int(request.POST['semester'])
    dept = request.POST['dept']
    # 조건에 맞는 애들만 걸러서 queryset list로 반환
    searchList = Lecture.objects.filter(rq_year=year, rq_semester = semester, department=dept)
    # print(searchList)

    return render(request, 'home.html', {'lectures': lectures, 'deptList': deptList, 'isTable' : isTable, 'searchList' :searchList})

def detail(request, id):
    selected_lecture = Lecture.objects.get(id=id)
    posts = Post.objects.all()
    postsList = []

    for post in posts:
        if(post.lecture.title == selected_lecture.title):
            postsList.append(post)
            
    return render(request, 'detail.html', {'selected_lecture' : selected_lecture, 'postsList' : postsList})

def new(request, id):
    selected_lecture = Lecture.objects.get(id=id)
    return render(request, 'new.html', {'selected_lecture' : selected_lecture})

def create(request, id):
    post = Post()
    post.writer = request.user
    post.lecture = Lecture.objects.get(id=id)
    post.body = request.GET['body']
    post.rating = request.GET['rating']
    post.save()
    return redirect('detail' , id)

def update(request, id):
    post = Post.objects.get(id=id)
    if ( request.method == "POST" ):
        post.writer = request.user
        post.lecture = Lecture.objects.get(id=post.lecture.id)
        post.body = request.POST['body']
        post.rating = request.POST['rating']
        post.save()
        return redirect('detail' , post.lecture.id)

    return render(request, 'update.html', {'post' : post})

def delete (request, id):
    post = Post.objects.get(id=id)
    #lecture_id= post.lecture.id
    post.delete()
    return redirect('detail' , post.lecture.id)
