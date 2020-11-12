import time
import paramiko


class SSHBase(object):

    def __init__(self, host_dict):
        self.host = host_dict['host']
        self.port = host_dict['port']
        self.username = host_dict['username']
        self.pwd = host_dict['password']
        self.transport = None
        self.channel = None

    def connect(self):
        self.transport = paramiko.Transport((self.host, self.port))
        self.transport.start_client()
        self.transport.auth_password(self.username, self.pwd)
        self.channel = self.transport.open_session()
        self.channel.get_pty()
        self.channel.invoke_shell()

    def send_cmd(self, string):
        send_string = '%s\r' % string
        self.channel.send(send_string)

    def receive_message_from_terminal(self, size=1024):
        rst = self.channel.recv(size)
        rst = rst.decode('utf-8')
        print(rst)

    def root(self):
        self.channel.send(r'su - root')
        time.sleep(0.2)
        rst = self.channel.recv(1024)
        rst = rst.decode('utf-8')
        if 'Password' in rst:
            self.channel.send('%s\r' % self.pwd)
            time.sleep(0.5)
            ret = self.channel.recv(1024)
            ret = ret.decode('utf-8')
            print(ret)

    def __del__(self):
        self.channel.close()
        self.transport.close()


class SFTPOperation(SSHBase):

    def upload(self, local_path, target_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.put(local_path, target_path, confirm=True)
        sftp.chmod(target_path, 0o755)  # 注意这里的权限是八进制的，八进制需要使用0o作为前缀

    def download(self, target_path, local_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.get(target_path, local_path)

    def __del__(self):
        self.transport.close()
