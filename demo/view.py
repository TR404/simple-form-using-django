# kahani kuch isa h isme ek website banaya hua h jo ke msg or check btn leta h or dushre page pr deta h yadi check nhi hua h to error dega or sab kiya hua h to apna msg ko forward kr dega ab isme hum isa bhi kr sakte he ke spacel charecter ko replace kr de to iske liye simple h ke variable bana lete h jisme wo sara charecter ho jo remove karna h or ab ispr loop laga dete h ke yadi mere msg ka jo jo variable me diye h wo sab h to remove kr de bs ab wo sara remove kr ke de dega humko.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return HttpResponse("<h1>This is First Program</h1>")
	
def indexSecond(request):
	print(request.GET.get('text','default'))
	return HttpResponse("sala smgh nhi aa raha h")
	
def indexThird(request):
	return render(request, 'index.html')
	
	
def indexFourth(request):
	djtext = request.GET.get('text', 'default')
	remove = request.GET.get('remove' , 'off')
	capsOn = request.GET.get('capsOn' , 'off')
	#print(remove)
	if remove == 'on':
		removeSymbols = '''!()-[]{}:;'"\,<>./?!@#$%^&*_~'''
		newDj = ''
		for char in djtext:
			if char not in removeSymbols:
				newDj = newDj + char
				#print(djtext)
		#messages = djtext
		parameter = {'purpose' : remove, 'message' : newDj }
		return render(request,'print.html', parameter)
	elif capsOn =='on':
		djNewText = ''
		for char in djtext:
			djNewText = djNewText + char.upper()
		parameter = {'purpose' : capsOn, 'message' : djNewText }
		return render(request,'print.html', parameter)
	else:
		return HttpResponse("Check Again...")
