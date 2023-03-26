## Install or update the AWS CLI in Windows

1. Download and run the AWS CLI MSI installer for Windows (64-bit):

  [Download Here](https://awscli.amazonaws.com/AWSCLIV2.msi)

  Alternatively, you can run the msiexec command in cmd .
``` 
C:\> msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
```

2. To confirm the installation, open the Start menu, search for cmd to open a command prompt window, and at the command prompt use the aws --version command.

```
C:\> aws --version
aws-cli/2.10.0 Python/3.11.2 Windows/10 exe/AMD64 prompt/off
```

