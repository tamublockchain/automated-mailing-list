from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

#set scopes for access
SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

#boilerplate code from the Google Form API to authorize access
store = file.Storage('token.json')
creds = None
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    flags = tools.argparser.parse_args(args=[]) #I found this online because the original boilerplate code didn't work
    creds = tools.run_flow(flow, store, flags) #Same comment as above
service = discovery.build('forms', 'v1', http=creds.authorize(Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)
print("succesfully connected")

#access the form ID from the url when you are in edit mode
form_id = '1Is7U0kFZ7sxJJXxxWPEUHLZJzCUPDaOhbAPS5BNIPtc'
result = service.forms().responses().list(formId=form_id).execute()
print("succesfully pulled data")

#get list of emails entered into the form
# im not sure if the 1092fe79 will be constant every time. test this with new emails 
email_list = []
for i in range(len(result["responses"])):
    email_list.append(result["responses"][i]["answers"]['1092fe79']["textAnswers"]["answers"][0]["value"])

#processing step1: remove emails without an @
correct_syntax = []
for e in email_list:
    if len(e.split("@")) == 2:
        correct_syntax.append(e)

#processing step2: validate emails that dont end in tamu.edu or gmail.com
validated = []
for e in correct_syntax:
    if e.split("@")[1] != "gmail.com" and e.split("@")[1] != "tamu.edu":
        #print(e)
        validation = input("Is the following email valid? Type y or n" + e)
        if validation == "y":
            print("Confirmed")
            validated.append(e)
        else:
            print("This email will not move on to further checks")
    else:
        validated.append(e)

#format all the emails in an easy to copy/paste format and dump in txt file
with open("add.txt", "a+") as myfile:
    myfile.write(",".join(map(str, validated)))

