from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from main.models import student1
from main.models import staff2
from main.models import parent1
from django.core.mail import send_mail
import random
import string
def generate_otp(length=6):
    otp = ''.join(random.choices(string.digits, k=length))
    
    return otp
def process_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = "sriram5066@gmail.com"
        print(name, password)

        if name == 'admin':
            # Generate a random OTP
            otp = generate_otp()

            # Send an email to the provided email address with OTP in the subject
            subject = f'Admin Login OTP: {otp}'
            message = 'You have logged in as admin.'
            from_email = 'ssri47856@gmail.com'  # Replace with your email
            recipient_list = [email]

            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                return JsonResponse({'message': 'Email sent successfully.'})
            except Exception as e:
                return JsonResponse({'message': f'Failed to send email: {str(e)}'}, status=500)

        # Handle non-admin user login logic here

        return JsonResponse({'message': 'Logged in successfully.'})

    return JsonResponse({'message': 'Invalid request method'}, status=400)
def disp(request):
    return render(request,'disp.html')
def inde(request):
    if(request.method=="POST"):
        return render(request,'2nd.html')
    return render(request,'index.html')
def home(request):
    return render(request, 'index.html')
def student_group(request):
    return render(request, '2nd.html')
def index(request):
    return render(request,'index1.html')
def gets(request):
    if request.method == "POST":
        stakeholder = request.POST.get('stakeholder')
        request.session['stakeholder'] = stakeholder

        if stakeholder == 'student':
            name = request.POST.get('name_student')
            batch = request.POST.get('batch_stu')
            email = request.POST.get('email_stu')
            request.session['email']=email
            request.session['name']=name
            saves=student1(name=name,email=email,batch=batch)
            saves.save()
            response_data = {"message": "Student data received and processed successfully"}
        elif stakeholder == 'staff':
            staff_name=request.POST.get('staff_name')
            staff_email=request.POST.get('staff_email')
            request.session['staff_name']=staff_name
            request.session['staff_email']=staff_email
            saves=staff2(staff_name=staff_name,staff_email=staff_email)
            saves.save()
            response_data = {"message": " data received and processed successfully"}
        elif stakeholder == 'parent':
            parent_name=request.POST.get('parent_name')
            sd=request.POST.get('sd')
            batch=request.POST.get('batch')
            ocu=request.POST.get('occupation')
            request.session['parent_name']=parent_name
            request.session['sd']=sd
            saves=parent1(parent_name=parent_name,sd=sd,batch=batch,occupation=ocu)
            saves.save()
            response_data = {"message": " data received and processed successfully"}
        elif stakeholder == 'industry':
            sd=request.POST.get('idus_name')
            batch=request.POST.get('working_in')
            ocu=request.POST.get('designation')
            sd=request.POST.get('email_ind')
            idproof=request.POST.get('uploads')
            response_data = {"message": " data received and processed successfully"}
        elif stakeholder == 'academician':
            name_c=request.POST.get('name_c')
            coll_ame=request.POST.get('name_coll')
            desig=request.POST.get('desig')
            id=request.POST.get('id')
            response_data = {"message": " data received and processed successfully"}
        elif stakeholder == 'alumni':
            name_al=request.POST.get('name_alumni')
            batch_al=request.POST.get('batchs')
            current=request.POST.get('curret')
            desigs=request.POST.get('desigs')
            response_data = {"message": " data received and processed successfully"}
        else:
            response_data = {"message": "Invalid stakeholder selected"}

        return JsonResponse(response_data)
    
    return render(request, '2nd.html')
def third(request):
    return render(request,'third.html')
def thirs(request):
    stake = request.session.get('stakeholder')
    if stake == 'student':
        if request.method == "POST":
            email = request.session.get('email')
            name = request.session.get('name')
            vision_option = request.POST.get('vision_option')
            if vision_option == 'current_vision':
                vision="The Department should continue with the current vision statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('vision_goal'))
            entry=student1.objects.get(name=name,email=email)
            entry.vision=vision
            entry.save()
    if stake=="staff":
        if request.method == "POST":
            staff_name=request.session.get('staff_name')
            staff_email=request.session.get('staff_email')
            vision_option = request.POST.get('vision_option')
            if vision_option == 'current_vision':
                vision="The Department should continue with the current vision statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('vision_goal'))
            entry=staff2.objects.get(staff_name=staff_name,staff_email=staff_email)
            entry.vision=vision
            entry.save()
    if stake=="parent":
        if request.method == "POST":
            parent_name=request.session.get('parent_name')
            sd=request.session.get('sd')
            vision_option = request.POST.get('vision_option')
            if vision_option == 'current_vision':
                vision="The Department should continue with the current vision statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('vision_goal'))
            entry=parent1.objects.get(parent_name=parent_name,sd=sd)
            entry.vision=vision
            entry.save()
    if stake=="industry":
        if request.method == "POST":
            vision_option = request.POST.get('vision_option')
            if vision_option == 'current_vision':
                vision="The Department should continue with the current vision statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('vision_goal'))
    if stake=="academician":
        if request.method == "POST":
            vision_option = request.POST.get('vision_option')
            if vision_option == 'current_vision':
                vision="The Department should continue with the current vision statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('vision_goal'))
    if stake=="alumni":
        if request.method == "POST":
            vision_option = request.POST.get('vision_option')
            if vision_option == 'current_vision':
                vision="The Department should continue with the current vision statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('vision_goal'))
    return render(request, 'fouth.html')
def fourth(request):
    stake = request.session.get('stakeholder')
    if stake == 'student':
        if request.method == "POST":
            email = request.session.get('email')
            name = request.session.get('name')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current mission statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=student1.objects.get(name=name,email=email)
            entry.mission=vision
            entry.save()
    if stake=="staff":
        if request.method == "POST":
            staff_name=request.session.get('staff_name')
            staff_email=request.session.get('staff_email')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current mission statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=staff2.objects.get(staff_name=staff_name,staff_email=staff_email)
            entry.mission=vision
            entry.save()
    if stake=="parent":
        if request.method == "POST":
            parent_name=request.session.get('parent_name')
            sd=request.session.get('sd')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current mission statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('mission_goal'))
            entry=parent1.objects.get(parent_name=parent_name,sd=sd)
            entry.mission=vision
            entry.save()
    if stake=="industry":
        if request.method == "POST":
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current mission statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            
    if stake=="academician":
        if request.method == "POST":
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current mission statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
    if stake=="alumni":
        if request.method == "POST":
            vision_option = request.POST.get('mission_option')
            if vision_option == 'mission_vision':
                vision="The Department should continue with the current mission statement as written."
            elif vision_option == 'mission_vision': 
                vision=(request.POST.get('mission_goal'))
    return render(request, 'fifth.html')
def fifth(request):
    stake = request.session.get('stakeholder')
    if stake == 'student':
        if request.method == "POST":
            email = request.session.get('email')
            name = request.session.get('name')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PEOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=student1.objects.get(name=name,email=email)
            entry.peo=vision
            entry.save()
    if stake=="staff":
        if request.method == "POST":
            staff_name=request.session.get('staff_name')
            staff_email=request.session.get('staff_email')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PEOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=staff2.objects.get(staff_name=staff_name,staff_email=staff_email)
            entry.peo=vision
            entry.save()
    if stake=="parent":
        if request.method == "POST":
            parent_name=request.session.get('parent_name')
            sd=request.session.get('sd')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PEOs statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('mission_goal'))
            entry=parent1.objects.get(parent_name=parent_name,sd=sd)
            entry.peo=vision
            entry.save()
    if stake=="industry":
        if request.method == "POST":
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PEOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            
    if stake=="academician":
        if request.method == "POST":
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PEOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
    if stake=="alumni":
        if request.method == "POST":
            vision_option = request.POST.get('mission_option')
            if vision_option == 'mission_vision':
                vision="The Department should continue with the current PEOS statement as written."
            elif vision_option == 'mission_vision': 
                vision=(request.POST.get('mission_goal'))
    return render(request, 'sixth.html')
def sixth(request):
    stake = request.session.get('stakeholder')
    if stake == 'student':
        if request.method == "POST":
            email = request.session.get('email')
            name = request.session.get('name')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PSOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=student1.objects.get(name=name,email=email)
            entry.pos=vision
            entry.save()
    if stake=="staff":
        if request.method == "POST":
            staff_name=request.session.get('staff_name')
            staff_email=request.session.get('staff_email')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PSOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=staff2.objects.get(staff_name=staff_name,staff_email=staff_email)
            entry.pos=vision
            entry.save()
    if stake=="parent":
        if request.method == "POST":
            parent_name=request.session.get('parent_name')
            sd=request.session.get('sd')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PSOs statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('mission_goal'))
            entry=parent1.objects.get(parent_name=parent_name,sd=sd)
            entry.pos=vision
            entry.save()
    if stake=="industry":
        if request.method == "POST":
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PSOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            
    if stake=="academician":
        if request.method == "POST":
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PSOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
    if stake=="alumni":
        if request.method == "POST":
            vision_option = request.POST.get('mission_option')
            if vision_option == 'mission_vision':
                vision="The Department should continue with the current PSOs statement as written."
            elif vision_option == 'mission_vision': 
                vision=(request.POST.get('mission_goal'))
    return render(request, 'seventh.html')