from django.shortcuts import render
import datetime

# Create your views here.
# def index(request):
#     now = datetime.datetime.now()
#     if now.month == 1 and now.day == 1:
#         return render(request, "newyear/index.html", {
#             "answer" : "yes".capitalize()
#         })
#     else:
#         return render(request, "newyear/index.html", {
#             "answer" : "no".capitalize()
#         })
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "answer": now.month == 1 and now.day == 1
        # "answer": True
    })