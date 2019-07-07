from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

serviceUsername = "29870c79-ddac-489f-850b-f358ec75aa59-bluemix"
servicePassword = "92c010375c94e7f4dd1c9b9df8c51cb3739f4a35175764907c04b8f8e5e1b226"
serviceURL = "https://29870c79-ddac-489f-850b-f358ec75aa59-bluemix:92c010375c94e7f4dd1c9b9df8c51cb3739f4a35175764907c04b8f8e5e1b226@29870c79-ddac-489f-850b-f358ec75aa59-bluemix.cloudantnosqldb.appdomain.cloud"

client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()

databaseName = "watsoners"
myDatabaseDemo = client.create_database(databaseName)

if myDatabaseDemo.exists():
    print "'{0}' successfully created.\n".format(databaseName)