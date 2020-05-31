from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.base import View
from .models import *
from .forms import *



class GoodsList(View):
    def get(self, request):
        goods = Car.objects.all()
        category = Category.objects.all()
        return render(request, 'goods/index.html', {'goods_list': goods, 'category': category})
    #### NEW Class ListView   ##########
    # model = Car
    # queryset = Car.objects.all()
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args,**kwargs)
    #     context["category"] = Category.objects.all()
    #     context["goods_list"] = Car.objects.all()
    #
    #     return context

def addcar(request):
    form = AddCar()
    context = {
        'list_car': Car.objects.all().order_by('id'),
        'form': form
    }

    return render(request, 'goods/add_car.html', context=context)



class AddCar(View):

    def get(self, request):

        template = 'goods/add_car_new.html'
        car = Car.objects.get(id=1)
        form = AddCar()
        print(type(form))
        print(dir(form))
        return render(request, template, context= {'form': form, 'car':car})

class CarDetail(View):
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['star_form'] = RatingForm()
    #     return context

    def get(self, request, slug):
        car = Car.objects.get(slug=slug)
        category = Category.objects.all()
        ############################## Paginanate #####################
        # review = Reviews.objects.all()
        # review = car.get_review()
        review = car.reviews_set.filter(parent__isnull=True)
        paginator = Paginator(review, 5)
        page_num = request.GET.get('page', 1)
        page = paginator.get_page(page_num)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''
        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''
        # print(dir(review))
        context = {
            'posts': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url,
            'car': car,
            # 'rev': rev
            'category': category,

        }

        ############################## Paginanate #####################
        # return render(request, 'goods/product.html', {'car': car})

        return render(request, 'goods/product.html', context= context)


class AddReview(View):
    def post(self,request,pk):
        form = ReviewForm(request.POST)


        car = Car.objects.get(id=pk)
        # print(review)
        if form.is_valid():
            form = form.save(commit=False)

            form.car = car
            form.date_post = timezone.now()
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))

            form.save()

            # return redirect('/')
        return redirect(car.get_absolute_url())

class AddStars(View):
    def post(self,request,pk):
        form = RatingForm(request.POST)


        car = Car.objects.get(id=pk)
        # print(review)
        if form.is_valid():
            Rating.objects.update_or_create(
                # ip=self.get_client_ip(request),
                car_id=int(request.POST.get("car")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
        # context['star_form'] = form
        # return context
        #     # return redirect('/')
        # return redirect(car.get_absolute_url())

class AddStarRating(View):
    """Добавление рейтинга фильму"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)




# Create your views here.
