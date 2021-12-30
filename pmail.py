import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('sender_email@gmail.com', 'sender_password')
server.sendmail('sender_email@gmail.com', 'receiver_email@gmail.com', 'Mail sent using python code(MESSAGE/BODY)')
print('Mail sent')
