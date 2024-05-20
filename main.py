import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from blog.models import Post, Comment


# Post(
#     name="Name for post",
#     content="Hihihiha"
# ).save()

# post = Post.objects.get(id=1)
# Comment(
#     content="BIMBIMBABAM",
#     author="Sasha",
#     post=post
# ).save()

while True:
    option = input("\n1. Додати коментар\n2. Редагувати пост\n3. Закрити програму\n>>>")

    if option == "1":
        id = int(input("ID поста: "))
        content = input("Зміст коментаря: ")
        author = input("Автор: ")

        post = Post.objects.get(id=id)
        if post:
            Comment(
                content=content,
                author=author,
                post=post
            ).save()

    elif option == "2":
        id = int(input("ID поста: "))
        new_content = input("Новий зміст поста: ")

        post = Post.objects.get(id=id)
        if post:
            post.content = new_content
            post.save()

    elif option == "3":
        break