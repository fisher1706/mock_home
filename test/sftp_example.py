import pysftp

Hostname = "ftps.qa.integrationlogix.com"
Username = "test_edi_856"
Password = "Zapel_1706"

with pysftp.Connection(host=Hostname, username=Username, password=Password) as sftp:
    print("Connection successfully established ... ")