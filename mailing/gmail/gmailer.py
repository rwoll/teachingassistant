from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from apiclient import errors
import oauth2client
from oauth2client import client
from oauth2client import tools

from email.mime.text import MIMEText
import base64


class GoogleMailer(object):
    """Basic mailer class to take advantage of Google's Python API"""

    def __init__(self):
        # builds the Gmail service object
        # Note that we are passing it None, so any API docs about
        # regarding run flags will be useless!
        # It would be good to fix this, but due to clashes with other script
        # parsers, I have not.
        self._service = self._build_gmail_service(None)

    def send_email(self, sender, to, subject, message):
        """Builds and sends an email.

        :param sender: sender's address
        :param to: recipient's address
        :param subject: subject line of email
        :param message: text to appear in the body of the email
        :return: google message dictionary if successful, None otherwise
        """
        return self._send_message(
            self._create_message(sender, to, subject, message))

    def _build_gmail_service(self, flags):
        """Build a basic service for use with Gmail

        :param flags: command line flags
        :return: a gmail service object
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'gmail-u-grade.json')

        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            # get user input of gmail credential file
            api_creds = raw_input('Path to Gmail Credentials: ')
            flow = client.flow_from_clientsecrets(api_creds,
                                                  'https://www.googleapis.com'
                                                  + '/auth/gmail.send')
            flow.user_agent = 'CLI'
            credentials = tools.run_flow(flow, store, flags)

        http = credentials.authorize(httplib2.Http())

        return discovery.build('gmail', 'v1', http=http)

    def _send_message(self, message):
        """Send a message from logged in account.

        :param message: MIME message
        :return: message if successful, None if failed
        """
        try:
            message = (self._service.users()
                       .messages().send(userId='me', body=message).execute())
            return message
        except errors.HttpError as error:
            print('An error occurred: %s' % error)
            return None

    def _create_message(self, sender, to, subject, message_text):
        """Create a simple MIMEText message for an email.

        :param sender: sender's email address
        :param to: recipient's email address
        :param subject: subject line of the email
        :param message_text: message body
        """
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject

        return {'raw': base64.urlsafe_b64encode(
            message.as_string().encode('UTF-8')).decode('ascii')}
