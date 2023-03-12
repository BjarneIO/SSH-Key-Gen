import os

PC_USER = os.environ['USERNAME']
PC_NAME = os.environ['COMPUTERNAME']
NAME = f'{PC_USER}@{PC_NAME}'


def generate_key(name='id_rsa', password='password', comment=NAME, save_to_ssh_folder=True):

    if save_to_ssh_folder:
        os.chdir(os.path.expanduser('~/.ssh'))

    os.system(
        f'ssh-keygen -t rsa -b 4096 -f {name} -N "{password}" -C "{comment}"')


if __name__ == '__main__':
    name = input('Name [id_rsa]: ')
    password = input('Password [password]: ')
    comment = input(f'Comment [{NAME}]: ')

    save_to_ssh_folder = input(
        'Save to SSH folder? (~/.ssh) [Y/n]: ').upper() == 'Y'

    generate_key(name, password, comment, save_to_ssh_folder)
