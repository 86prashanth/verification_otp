from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings 
import time,threading

# send email
def send_email_to_user(email,subject,message):
    try:
        email_from=settings.EMAIL_HOST
        send_mail(subject,message,email_from,[email])
    except Exception as e:
        print(e)

# send email through attachement 
def send_email_to_attachment(email,subject,message):
    try:
        email_from=settings.EMAIL_HOST
        email_message=EmailMessage(subject,message,email_from,[email])
        email_message.attach_file('django.pdf')
        email_message.send()
    except Exception as e:
        print(e)
        
        
class SendEmail(threading.Thread):
    def __init__(self,email,subject,message):
        self.email=email
        self.subject=subject 
        self.message=message 
        threading.Thread.__init__(self)
    def run(self):
        time.sleep(20)
        try:
            email_from=settings.EMAIL_HOST
            email_message=EmailMessage(self.subject,self.message,email_from,[self.email])
            email_message.attach_file('django.pdf')
            email_message.send()
        except Exception as e:
            print(e)