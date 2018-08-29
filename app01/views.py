from django.shortcuts import render,HttpResponse,redirect


from app01 import models
# Create your views here.


#展示出版社列表列表
def publisher_list(request):
    #去数据库查询所有的数据
    ret = models.Publisher.objects.all().order_by("id")
    return render(request, "publisher_list2.html", {"publisher_list":ret})



#添加出版社列表
def add_publisher(request):
    erro_msg = ""
    if request.method == "POST":
        new_name = request.POST.get("publisher_name")
        if new_name:
            #通过ORM在数据库中建立一条新的数据
            models.Publisher.objects.create(name=new_name)
        else:
            erro_msg = "出版社名字不能为空"
            return render(request,"add_publisher.html",{"error":erro_msg})
        #添加完成后引导用户出版社列表页面
        return redirect("/publisher_list/")
    #第一次添加一个用来填写信息的HTML页面
    return render(request,"add_publisher.html")


#删除出版社的函数
def delete_publisher(request):
    #删除指定的数据
    #从get请求的参数里边拿到将要删除数据的ID
    del_id = request.GET.get("id",None)  #字典取值，取不到的话，默认显示None
    #如果能取到id值
    if del_id:
        #去数据库删除当前id值的数据
        #根据id值查找到数据
        del_obj = models.Publisher.objects.get(id=del_id).delete()
        #删除

        #返回删除后的页面，跳转到出版社列表页，查看删除是否成功
        return redirect("/publisher_list/")
    else:
        return HttpResponse("要删除的数据不存在")
    pass

#编辑出版社

def edit_publisher(request):
    #用户修改完信息，点击提交，给我发来新的名字
    if request.method == "POST":
        edit_id = request.POST.get("id")
        new_name = request.POST.get("publisher_name")
        #更新数据库
        #更具id取到编辑的是出版社
        edit_publisher = models.Publisher.objects.get(id=edit_id)
        edit_publisher.name = new_name
        edit_publisher.save()
        #跳转到出版社列表页，查看是否修改成功
        return redirect("/publisher_list/")
    #从GET请求的URL中获取到id的参数
    edit_id = request.GET.get("id")
    if edit_id:
        #获取到当前编辑的出版社对象
        publisher_obj = models.Publisher.objects.get(id=edit_id)
        return render(request,"edit_publisher.html",{"publisher":publisher_obj})

    else:
        return HttpResponse("编辑的出版社不存在")

#登陆
def Login(request):
    error_msg = ""
    if request.method == "POST":  # 这里必须是大写的
        # 如果你是POST请求,我就取出提交的数据,做登录判断
        #print(request.POST["email"])
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        #print(email, pwd)
        # 做是否登陆成功的判断
        if email == "alex@oldboyedu.com" and pwd == "alexdsb":
            # 登录成功
            # 回复一个特殊的响应,这个响应会让用户的浏览器请求指定的URL
            return redirect("http://www.luffycity.com")
        else:
            # 登录失败
            error_msg = "邮箱或密码错误"
    # 不是POST请求就走下面这一句
    return render(request, "Login.html", {"error": error_msg})



#展示书的列表

def book_list(request):
    #去数据库中查询所有数据
    all_book = models.Book.objects.all()
    #在HTML完成熏染数据
    return render(request,"book_List2.html",{"all_book":all_book})

#添加书籍
def add_book(request):
    if request.method == "POST":
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        #创建新书对象，自动提交
        models.Book.objects.create(title=new_title,publisher_id=new_publisher_id)
        #返回到书籍列表页面
        return redirect("/book_list/")

    #取到所有的出版社
    ret = models.Publisher.objects.all()
    return render(request,"add_book.html",{"publisher_list":ret})


#删除书籍
def delete_book(request):
    #从url里边获取要删除书籍的ID
    delete_id = request.GET.get("id")      #从url里边取数据
    #去数据库中删除指定id的数据
    models.Book.objects.get(id=delete_id).delete()
    #返回书籍别表页，查看是否删除成功
    return redirect("/book_list/")


#编辑书籍
def edit_book(request):
    if request.method == "POST":
        #从提交的数据里边去，书名和书关联的出版社
        edit_id = request.POST.get("id")
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        #更新
        edit_book_obj = models.Book.objects.get(id=edit_id)
        edit_book_obj.title = new_title                     #更新书名
        edit_book_obj.publisher_id = new_publisher_id       #更新出版社
        #将修改的数据提交到数据库
        edit_book_obj.save()
        #返回书籍列表页，查看是否修改成功
        return redirect("/book_list/")


    #取到编辑的书的id值
    edit_id = request.GET.get("id")
    #根据id在数据库中找到具体的书籍
    edit_book_obj = models.Book.objects.get(id=edit_id)
    ret = models.Publisher.objects.all()
    #返回一个页面，让用户编辑书籍信息
    return render(
        request,
        "edit_book.html",
        {"publisher_list":ret,"book_obj":edit_book_obj}
    )


#作者列表
def author_list(request):
    #查询所有的作者
    all_author = models.Author.objects.all()
    return render(request,"author_list2.html",{"author_list":all_author})



#添加作者
def add_author(request):
    if request.method == "POST":
        #取到提交的数据
        new_author_name = request.POST.get("author_name")
        books = request.POST.getlist("books")      #当前端传的数据是多个的时候要用gitlist

        #创建作者
        new_author_obj = models.Author.objects.create(name=new_author_name)
        #把新作者和书籍建立对应关系,自动提交

        new_author_obj.book.set(books)
        #返回到作者列表页面
        return redirect("/author_list/")
    #查询所有的书籍
    ret = models.Book.objects.all()
    return render(request,"add_author.html",{"book_list":ret})


#删除作者
def delete_author(request):
    #从url里边取到要删除作者的id
    delete_id = request.GET.get("id")
    #1.去作者表把作者删了
    #2。去作者和书的关联表，把对应的关联记录删除
    #根据id值找到对应的要删除的作者对象,直接删除
    models.Author.objects.get(id=delete_id).delete()
    return redirect("/author_list/")



#编辑 作者
def edit_author(request):
    #如果编辑完提交数据过来
    if request.method == "POST":

        #拿到提交过来编辑的数据
        edit_author_id = request.POST.get("author_id")

        new_author_name = request.POST.get("author_name")
        #拿到作者关联的书籍信息
        new_books = request.POST.getlist("books")

        #根据id找到当前编辑作者的对象
        edit_author_obj = models.Author.objects.get(id=edit_author_id)
        #更新作者名字
        edit_author_name = new_author_name
        #更新作者与书的对应关系
        edit_author_obj.book.set(new_books)

        #将修改的数据提交到数据库
        edit_author_obj.save()
        #返回作者列表页，查看是否编辑成功
        return redirect("/author_list/")

    #从url中取到要编辑作者的id信息
    edit_id = request.GET.get("id")
    #找到要编辑的作者对象
    edit_author_obj = models.Author.objects.get(id=edit_id)
    #查询所有的书籍
    ret = models.Book.objects.all()
    return render(request,"edit_author.html",{"book_list":ret,"author":edit_author_obj})