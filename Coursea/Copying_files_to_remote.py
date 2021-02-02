import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.56.101',
            username='edureka',
            password='edureka',
            port=22)
sftp_client = ssh.open_sftp()
print(sftp_client.getcwd())
print(sftp_client.getcwd())
sftp_client.chdir("/home/edureka")
#print(dir(sftp_client))
print(sftp_client.getcwd())
#sftp_client.get('/home/edureka/fq.txt')
sftp_client.put("test1.txt", '/home/edureka/test.txt')

sftp_client.close()
ssh.close()