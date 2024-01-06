# 1. Using command-line arguments involves the sys module. Review the docs for this
# module and using the information in there write a short program that when run
# from the command-line reports what operating system platform is being used.


# Importing sys module to access the command line arguments
import sys


def report_platform():
    platform = sys.platform
    print(f"The operating system platform is: {platform}")

report_platform()