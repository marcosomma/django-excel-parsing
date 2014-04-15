from django.shortcuts import render
from django.http import HttpResponse

from models import *

import xlrd

def getfiles(request):
	workbook = xlrd.open_workbook('test.xlsx')
	worksheet = workbook.sheet_by_name('test')

	num_rows = worksheet.nrows - 1

	for r_ind in range(1,num_rows):
		row = worksheet.row(r_ind)

		for c_ind,c in enumerate(row):
			cell_type = worksheet.cell_type(r_ind, c_ind)

			if cell_type != 0 :
				cell_value = worksheet.cell_value(r_ind, c_ind)

				if c_ind == 0:
					course = Course(title=cell_value)
					actual_course = course
					course.save()

				elif c_ind == 1:
					lesson = Lesson(title=cell_value , course=actual_course)
					actual_lesson = lesson
					lesson.save()

				elif c_ind == 2:
					topic = Topic(title=cell_value , lesson=actual_lesson)
					topic.save()

	return HttpResponse(workbook)