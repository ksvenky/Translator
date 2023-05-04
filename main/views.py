

from django.shortcuts import render,HttpResponse
from translate import Translator
# Create your views here.

def home(request):
	if request.method == "POST":
		text = request.POST.get("translate")
		language = request.POST.get("language")
		translator= Translator(to_lang=language)
		translation = translator.translate(text)
		return render(request,"index.html", {"translation":translation})
	return render(request,"index.html")


