import os
connection = {
    'address': os.environ['AMI_IP'],
    'port': os.environ['AMI_PORT'],
    'timeout': 180,
}

login = {
    'username': os.environ['AMI_LOGIN'],
    'secret': os.environ['AMI_PASSWORD']
}