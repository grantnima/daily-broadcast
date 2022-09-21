import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from util.configuration import config

class sender:

    def __init__(self):
        self.account = config.mail_account
        self.password = config.mail_password
        self.toList = config.mail_to_list
        self.signature = config.mail_signature
        self.subject = config.mail_subject

    def doSend(self,rawContent):
        try:
            msg = MIMEText(rawContent,"html","utf-8")
            msg["From"] = formataddr([self.signature,self.account])
            msg["To"] = formataddr(["",self.account])
            msg["Subject"] = self.subject
            server = smtplib.SMTP_SSL("smtp.qq.com",465)
            server.login(self.account, self.password)
            server.sendmail(self.account, self.toList, msg.as_string())
            server.quit()
        except Exception as ex:
            raise Exception("邮件发送失败, err: {}".format(ex))

if __name__ == '__main__':
    s = sender()
    s.doSend("testingtesting")
        

