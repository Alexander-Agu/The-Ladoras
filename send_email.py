from Google import create_service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(massage, to, subject):
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']

    service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    emailMsg = subject
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = to
    mimeMessage['subject'] = massage
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()