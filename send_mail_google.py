import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

recipient_email = 'mohamedzahi33@gmail.com'
html_content = """<p style="color:red">Hello World! 2d99</p>"""

try:
    msg = MIMEMultipart()
    msg['From'] = f'Miramar General Maintenance <miramar.general.maintenance@gmail.com>'
    msg["To"] = recipient_email
    msg["Subject"] = 'Hello from Python!!!'
    msg['cc'] = reply_to_cc
    msg['Reply-To'] = reply_to_cc

    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login('miramar.general.maintenance@gmail.com', 'vtodbphbjhywskex')
        server.sendmail('miramar.general.maintenance@gmail.com', recipient_email, msg.as_string())

except Exception as e:
    print(f"An error occurred: {str(e)}")
