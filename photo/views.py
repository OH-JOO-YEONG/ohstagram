from django.shortcuts import render
from .models import Photo
from django.views.generic import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {
        'photos': photos
    })

class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid(): #입력된 값 검증
            form.instance.save()
            return redirect('/') #이상이 없다면 데이터베이스에 저장하고 redirect로 메인페이지 이동
        else:
            return self.render_to_response({'form': form}) #만약 이상이 있다면 작성된 내용을 그대로 작성 페이지에 표시합니다.

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'