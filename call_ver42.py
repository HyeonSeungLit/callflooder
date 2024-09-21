import os
from twilio.rest import Client
import time

ACCOUNT_SID = ""
AUTH_TOKEN = ""
FROM="+"
CALLED="+"
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
#account_sid = os.environ['']
#auth_token = os.environ['']
#client = Client(account_sid, auth_token)

class Call:
    def __init__(self):
        self.FROM = FROM
        self.CALLED = CALLED
        self.ACCOUNT_SID = ACCOUNT_SID
        self.AUTH_TOKEN = AUTH_TOKEN
        self.callCounter = 0
        self.LIMIT = 100

    def makeCall(self):
        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)

        while self.callCounter < self.LIMIT:     
            call = client.calls.create(
            record=True,
            to=self.CALLED, from_ = self.FROM,
            url='mp3 file url')
            self.callCounter = self.callCounter + 1
            print("Call #" + str(self.callCounter) + " Calling number: " +str(self.CALLED))
            time.sleep(3)

def main():
    #print(call.sid)
    robo = Call()
    robo.makeCall()

if __name__ == "__main__":
    main()

