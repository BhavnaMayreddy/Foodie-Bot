import smtplib
from prompt_toolkit import print_formatted_text, HTML

def sendmail(mail_id,txt_details):
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("zomato.rasatest@gmail.com","Test@2020")
    # message to be sent 
    subject = "Foodie ChatBot Restaurant Result"
    text = "List of restaurants you searched for:\n"
  
    message = 'Subject: {}\n\n{}'.format(subject, txt_details)
    print(message)
    try:
        s.sendmail("zomato.rasatest@gmail.com",str(mail_id),message)
        s.quit()
    except:
        dispatcher.utter_message('email not sent')
    #last_req_res = ""
    return "email sent"
