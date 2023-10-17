
"""Rx
"""
import argparse
from crocodile.toolbox import SSH
import crocodile.toolbox as tb


def main():
    parser = argparse.ArgumentParser(description='FTP client')

    parser.add_argument("machine", help=f"machine ssh address", default="")
    parser.add_argument("file", help="file/folder path.", default="")
    # parser.add_argument("--local", "-l", help="local file/folder path.", default=None)
    # FLAGS
    parser.add_argument("--recursive", "-r", help="Send recursively.", action="store_true")  # default is False
    parser.add_argument("--zipFirst", "-z", help="Zip before sending.", action="store_true")  # default is False

    parser.add_argument("-d", "--destination", help=f"destination folder", default=None)

    args = parser.parse_args()
    from paramiko.ssh_exception import AuthenticationException
    try:
        ssh = SSH(rf'{args.machine}')
    except AuthenticationException:
        print("Authentication failed, trying manually:")
        print(f"Caution: Ensure that username is passed appropriately as this exception only handles password.")
        import getpass
        pwd = getpass.getpass()
        ssh = SSH(rf'{args.machine}', pwd=pwd)

    received_file = ssh.copy_to_here(source=args.file, target=args.destination, z=args.zipFirst, r=args.recursive)
    # ssh.print_summary()

    if tb.P(args.file).is_dir(): print(f"Use: cd {repr(tb.P(args.file).expanduser())}")
    print(f"Received: {repr(received_file.parent), repr(received_file)}")


if __name__ == '__main__':
    main()
