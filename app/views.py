from django.contrib.sites import requests
from django.http import JsonResponse
from django.core import serializers
import json
import requests
from app.models import Posts
from django.views.decorators.csrf import csrf_exempt


def getPosts(request, request_uid):
    if request.method != "GET":
        return JsonResponse({"message": "Wrong method"}, status=400)
    if not isinstance(request_uid, int):
        return JsonResponse({'message': 'No posts for this user id'}, status=404)

    post = Posts.objects.filter(userId=request_uid)

    js = serializers.serialize('json', post)
    userPosts = json.loads(js)

    if not userPosts:
        return JsonResponse({'message': 'No posts for this user id'}, status=404)

    return JsonResponse(userPosts, safe=False)


@csrf_exempt
def addPost(request):
    if request.method != "POST":
        return JsonResponse({"message": "Wrong method"}, status=400)
    if not request.body:
        return JsonResponse({'message': 'No data'}, status=400)

    data = request.body.decode('utf-8')
    data = json.loads(data)

    if 'id' not in data or 'userId' not in data:
        return JsonResponse({'message': 'Missing data'}, status=400)

    if not isinstance(data['id'], int) or not isinstance(data['userId'], int):
        return JsonResponse({'message': 'Wrong data'}, status=400)

    usersResponse = requests.get('https://jsonplaceholder.typicode.com/users')
    users = usersResponse.json()

    userGood = False
    for i in users:
        if i['id'] == data['userId']:
            userGood = True
            break

    if not userGood:
        return JsonResponse({'message': 'No user with this id'}, status=404)

    existing = Posts.objects.filter(id=data['id'])
    if existing:
        return JsonResponse({'message': 'Post with this ID already exists'}, status=400)

    post = Posts()

    post.id = data['id']
    post.userId = data['userId']
    post.title = data['title']
    post.body = data['body']

    post.save()

    return JsonResponse({"message": "Post created"}, status=201)


@csrf_exempt
def deletePost(request, postID):
    if request.method != "DELETE":
        return JsonResponse({"message": "Wrong method"}, status=400)

    post = Posts.objects.filter(id=postID)
    if not post:
        return JsonResponse({"message": "No post with this id"}, status=404)

    post.delete()
    return JsonResponse({'message': 'Post successfully removed'}, status=200)


@csrf_exempt
def updatePost(request):
    if request.method != "PUT":
        return JsonResponse({"message": "Wrong method"}, status=400)
    if not request.body:
        return JsonResponse({'message': 'No data'}, status=400)

    data = request.body.decode('utf-8')
    data = json.loads(data)

    if 'id' not in data and 'title' not in data and 'body' not in data:
        return JsonResponse({'message': 'Missing data'}, status=400)

    if not isinstance(data['id'], int):
        return JsonResponse({'message': 'Wrong data'}, status=400)

    try:
        post = Posts.objects.get(id=data['id'])
    except:
        return JsonResponse({"message": "No post with this id"}, status=404)

    if data['title'] == "":
        post.body = data['body']
    if data['body'] == "":
        post.title = data['title']
    if data['title'] != "" and data['body'] != "":
        post.title = data['title']
        post.body = data['body']

    post.save()
    return JsonResponse({'message': 'Post successfully edited'}, status=201)
