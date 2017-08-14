#e8-2-2 Gmail API寄信
from __future__ import print_function
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import  base64
from  email.mime.text import MIMEText
from  email.mime.multipart import MIMEMultipart
from apiclient import errors
def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,  'gmail-python-quickstart.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
def create_message(sender, to, subject,message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
#    msg.attach(MIMEText(message_text,'plain' ) ) 
#    raw =  base64.urlsafe_b64encode(msg.as_bytes())
#    raw  = raw.decode()
#    body =  { ' raw ':  raw}
#    return  body

def send_message( service,user_id, message):
    try:
        message  =(service.users().messages().send(userId=user_id, body=message).execute())
        print ('Message Id :%s' %message ['id' ] )
        return  message
    except  errors.HttpError  as  error:
        print ( ' An error  occurred : ' , error )
SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'
credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
service = discovery.build('gmail', 'v1', http=http)
message = create_message('','tsy0413@gmail.com','test', 'test')
send_message(service,'me',message)