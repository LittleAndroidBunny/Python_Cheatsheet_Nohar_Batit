import argparse


parser = argparse.ArgumentParser('Describe your program here for help')
# # the positional argument, if placed is not optional and must appear
parser.add_argument('arg0')
parser.add_argument('arg1', type=str, default='test',)
parser.add_argument('--arg2', type=int,  default=10, help='describe which input is expected here (default=10)')
parser.add_argument('--arg3', type=float, dest='argFloat', default=1.5, help='describe which input is expected here (default=1.5)')


# use the given arguments
arg = parser.parse_args()
#arg = parser.parse_args(['hello', '5', '--arg2', '15', '--arg3', '12.3'])
print(arg.arg0)
print(arg.arg1)
print(arg.arg2 + 4)

