import sys
import os
import getopt
import yaml
import yqtb

def help(): 
    name = os.path.basename(sys.argv[0])
    print('Usage: %s -u <username> -p <password>' % name)
    print('   or: %s --username=<username> --password=<password>' % name)

def main(argv):
    username = ""
    password = ""

    try:
        opts, args = getopt.getopt(
            argv, "hu:p:", ["help", "username=", "password="])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
            sys.exit()
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg

    with open('config.yml', 'r', encoding = 'utf-8') as file:
        params = yaml.safe_load(file)
        yqtb.submit(username, password, params)


if __name__ == '__main__':
    main(sys.argv[1:])
