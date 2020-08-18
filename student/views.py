from django.shortcuts import render,redirect
from project_admin.models import AssignTest
from django.contrib.auth.decorators import login_required
import datetime
from datetime import timedelta,date
from django.http import HttpResponse
from assessment.models import QuestionCategory
# Create your views here.
@login_required
def student_home_view(request):
	
	#check whether user has old test which are not yet cancelled:
	#test = AssignTest.objects.filter(student__user=request.user,test_status='pending',test_datetime__lte=current_date_time)|AssignTest.objects.filter(elearning_stu__user=request.user,test_status='pending',test_datetime__lte=datetime.datetime.now())
	#test.update(test_status ='cancel')

	#current_date_time = date.strftime(datetime.datetime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
	current_date_time = datetime.datetime.now().replace(microsecond=0)
	
	#fetch all upcoming test
	test = AssignTest.objects.filter(student__user=request.user,test_status__in=['pending','started'])|AssignTest.objects.filter(elearning_stu__user=request.user,test_status__in=['pending','started'])
	
	#if there are some upcoming test
	if test.count()>0:
		#check whether any test has already begun
		for t in test:
			#print(current_date_time + timedelta(days=0,minutes=int(t.duration)))
			print(t.test_datetime,type(t.test_datetime))
			print(current_date_time,type(current_date_time))
			
			test_end_time = t.test_datetime + timedelta(days=0,minutes=int(t.duration))
			
			#if test has begun
			if t.test_datetime <= current_date_time and t.test_datetime< test_end_time:
				
				remaining_minutes = (test_end_time -current_date_time ).seconds/60

				print('test duration',t.duration) #40
				print(remaining_minutes) #38
				#if only 10 minutes has passed
				if t.test_status == 'started' and test_end_time <= current_date_time:
					return redirect('start_test')

				if t.duration - remaining_minutes <=10 and remaining_minutes<= t.duration:
					t.test_status = 'started'
					t.save()
					return redirect('start_test')
					

				#if test missed
				else:
					t.test_status='cancel'
					t.save()

					
			if t.test_datetime<current_date_time:
				t.test_status='cancel'
				t.save()
				
		
		test = AssignTest.objects.filter(student__user=request.user,test_status__in=['pending','started'])|AssignTest.objects.filter(elearning_stu__user=request.user,test_status__in=['pending','started'])
		if test.count()>0:
			test1 = test.values('test_datetime').order_by('test_datetime')
			latest_test = test1[0]['test_datetime']
			print('A')
			return render(request,'student/home.html',{'test_date':latest_test,'count_upcoming':test.count()})

	
	return render(request,'student/home.html',{'test_date':'','count_upcoming':0})

@login_required
def start_test_view(request):

	test = AssignTest.objects.filter(student__user=request.user,test_status__in=['pending','started'])|AssignTest.objects.filter(elearning_stu__user=request.user,test_status__in=['pending','started'])
	test.order_by('test_datetime')

	if test.count()>=1:
		t = test.order_by('test_datetime')[0]

	
	else:
		return redirect('student_home')



	print(test)
	return render(request,'student/test.html')

@login_required
def question_display_view(request):
	test = AssignTest.objects.filter(student__user=request.user,test_status='started')|AssignTest.objects.filter(elearning_stu__user=request.user,test_status='started')
	test.order_by('test_datetime')

	if test.count()==1:
		t = test.order_by('test_datetime')[0]
		category = QuestionCategory.objects.filter(test=test[0].test_paper)
		print(category)
		return render(request,'student/english.html',{'category':category})

	
	else:
		return redirect('student_home')

	
@login_required
def past_test_view(request):
	return render(request,'student/past_test.html')

@login_required
def upcoming_test_view(request):
	upcoming_test = AssignTest.objects.filter(student__user=request.user,test_status='pending')|AssignTest.objects.filter(elearning_stu__user=request.user,test_status='pending')
	return render(request,'student/upcoming_test.html',{'upcoming':upcoming_test,'count':upcoming_test.count()})

@login_required
def cancel_test_view(request,id):
	test = AssignTest.objects.get(id=id)
	test.test_status ='cancel'
	test.save()
	return redirect('upcoming_test')