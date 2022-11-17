from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from PyPDF2 import PdfFileMerger
import datetime

def index(request):
	return render(request, 'index.html')

def merge(request):
	if request.method == 'POST':
		pdfs = request.FILES.getlist('myfiles')
		
		merger = PdfFileMerger()

		for pdf in pdfs:
		    merger.append(pdf)

		ct = datetime.datetime.now()
		file_name = "mergedpdfs/" + str(ct.timestamp()) + ".pdf"

		merger.write(file_name)

		return FileResponse(open(file_name, 'rb'), content_type='application/pdf')

	return HttpResponse("Bad Gateway")