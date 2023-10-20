import smtplib
from email.mime.text import MIMEText
from email.header import Header

class QQEmailSender:
    def __init__(self, sender, auth_code, smtp_server='smtp.qq.com', smtp_port=587):
        self.sender = sender
        self.auth_code = auth_code
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, receiver, subject, content):
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = Header(self.sender, 'utf-8')
        message['To'] = Header(receiver, 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtp_obj = smtplib.SMTP(self.smtp_server, self.smtp_port)
            smtp_obj.starttls()
            smtp_obj.login(self.sender, self.auth_code)
            smtp_obj.sendmail(self.sender, receiver, message.as_string())
            smtp_obj.quit()
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print("邮件发送失败:", str(e))

# 示例用法
if __name__ == '__main__':
    sender = '279284832@qq.com'
    auth_code = 'osyznijomuimbhfj'
    receiver = 'comedyyou@163.com'
    subject = '测试邮件'
    content = '这是一封测试邮件。'

    email_sender = QQEmailSender(sender, auth_code)
    email_sender.send_email(receiver, subject, content)
