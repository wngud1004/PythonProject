import smtplib
from email.mime.text import MIMEText

sendEmail = "보내는 사람 이메일"
recvEmail = "받는 사람 이메일"
password = "계정 비밀번호"

smtpName = "smtp.naver.com"  # smtp 서버 주소 gmail.com, Live.com 다 가능
smtpPort = 587  # smtp 포트 번호

text = "매일 내용"
msg = MIMEText(text)  # MIMEText(text , _charset = "utf8")

msg['Subject'] = "이것은 메일 제목"
msg['From'] = sendEmail
msg['To'] = recvEmail
print(msg.as_string())

s = smtplib.SMTP(smtpName, smtpPort)  # 메일 서버 연결
s.starttls()  # TLS 보안 처리
s.login(sendEmail, password)  # 로그인
s.sendmail(sendEmail, recvEmail, msg.as_string())  # 메일 전송, 문자열로 변환하여 보냅니다.
s.close()  # smtp 서버 연결을 종료합니다.
