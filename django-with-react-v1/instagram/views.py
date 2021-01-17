from warnings import catch_warnings

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, CreateView, UpdateView, \
    DeleteView

from .forms import PostForm
from .models import Post, Comment


# @login_required
# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)  # 두번째 인자가 존재하지 않으면 그대로 POST만 저장
#         if form.is_valid():
#             post = form.save(commit=False)  # default commit=True 설정, False시 save 호출 작동 안함(저장 안됌)
#             post.author = request.user  # 현재 로그인 유저
#             post.save()
#             messages.success(request, "포스팅을 저장했습니다.")
#             return redirect(post)
#     else:
#         form = PostForm()
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': None,
#     })


# 클래스 create_post
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, '메세지를 등록하였습니다.')
        return super().form_valid(form)


post_new = PostCreateView.as_view()


# @login_required  # 함수형
# def post_list(request):
#     post_set = Post.objects.all()
#     q = request.GET.get('q', '')
#
#     if q:
#         post_set = post_set.filter(message__icontains=q)
#
#     # messages.info(request, "message test")
#     return render(request, 'instagram/post_list.html', {
#         'post_list': post_set,
#         'q': q,
#     })


@method_decorator(login_required, name="dispatch")  # 클래스형
class PostListView(ListView):
    model = Post
    paginate_by = 10


post_list = PostListView.as_view()


# post_list = ListView.as_view(model=Post, paginate_by=10) #ListView 활용 paginate_by-> 페이지별 row 갯수 설정 (search 불가) , login_required()로 감싸기


# generic을 활용한 list, detail
# post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')
# post_list = ListView.as_view(model=Post) #ListView 활용 (search 불가)

# ListView
# class PostListView(ListView):
#     model = Post
# post_list = PostListView.as_view()

# DetailView
# class PostDetailView(DetailView):
#     model = Post
#     pk_url_kwarg = 'id'
# post = PostDetailView.as_view()

# DetailVIew query_set변경 (유저일때 보이기 처리)
class PostDetailView(DetailView):
    model = Post

    # form_class = PostForm #위에 model 선언과 동일 (Form이 없어도 처리가 되는 이유는 View내에서 Form 생성 처리)

    # queryset = Post.objects.filter(is_public=True)

    def get_queryset(self):
        # request 인자는 class기반 View에서 self.request로 접근가능
        qs = super().get_queryset()  # 재정의할때 super 호출
        if not self.request.user.is_authenticated:  # 인증이 되어 있지 않으면
            qs = qs.filter(is_public=True)  # 공개 게시물만 허용
        return qs


post_detail = PostDetailView.as_view()
# post_detail = DetailView.as_view(model=Post, queryset=Post.objects.filter(is_public=True))  # 쿼리셋을 보낼 수도 있다.


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     # request.method
#     # request.META, request.GET, Post, body, FILES등
#     # response = HttpResponse()
#     # response.write("Hello World")
#     # return response
#     # return render(request, 'instagram/post_list.html')
#
#     post = get_object_or_404(Post, id=pk)
#
#     # try:
#     #     post = Post.objects.get(id=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#
#     return render(request, 'instagram/post_detail.html', {
#         'post': post
#         'object': post #가능
#     })


post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)
post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at',
                                            make_object_list=True)  # make_object default false이고 True로 해야 출력됌


# def archives_year(request, year):
#     return HttpResponse(f"{year}년")

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, id=pk)
#
#     # 작성자 체크 팁
#     if request.user != post.author:  # 글쓴이와 현재 로그인 유저가 다를시
#         messages.error(request, '작성자만 수정 가능합니다.')  # 에러메세지 추가
#         return redirect(post)
#
#     # form을 사용시 끝까지 form을 이용해 저장하기 form.cleaned_data['keyName'] / request.POST['keyName'] -> 사용하지 않기
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=post)  # update시 instance= 로 모델 인스턴스 전달
#         if form.is_valid():
#             post = form.save()  # default commit=True 설정, False시 save 호출 작동 안함(저장 안됌)
#             messages.success(request, "포스팅을 저장했습니다.")
#             return redirect(post)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': post,
#     })


# classUpdateView
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, '포스팅을 수정하였습니다.')
        return super().form_valid(form) #html {{form}}


post_edit = PostUpdateView.as_view()


# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, id=pk)  # confirm을 띄울땐 get, 유저가 확인 후 삭제 요청시 post
#     if request.method == 'POST':
#         if request.user != post.author:  # 글쓴이와 현재 로그인 유저가 다를시 (이부분은 데코레이터나 별도의 믹스인 처리로 하기)
#             messages.error(request, '작성자만 삭제 가능합니다.')  # 에러메세지 추가
#             return redirect(post)
#         post.delete()
#         messages.success(request, '포스팅을 삭제하였습니다.')
#         return redirect('instagram:post_list')
#     return render(request, 'instagram/post_confirm_delete.html', {
#         'post': post
#     })
#     # TODO


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/instagram/' #장고가 초기화전 소스코드 읽혀질때 실행됌 -> url improperlyConfigured exception 발생 이는 2가지 방법이 있다. 1. get_success_url 2.reverse_lazy
    # success_url = reverse_lazy('instagram:post_list') #success_url이 사용되어질때 실행

# def get_success_url(self):
#     return reverse('instagram:post_list')


post_delete = PostDeleteView.as_view()
