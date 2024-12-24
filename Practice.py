
# try:
#     inputNum = input('Enter a number:')

#     if inputNum == '0':
#         raise ValueError('Invalid number')
#     elif inputNum == '1':
#         raise NameError('inputNum is ')
# except ValueError:
#     print('Invalid value')
# except NameError:
#     print('Invalid Name')
# except: 
#     print('unexpected Error')
    
#     print('Code Finished')

# Without requirement to run the python File    
import argparse 
parser =argparse.ArgumentParser()
parser.add_argument('-i', '--input')

args = parser.parse_args()

if args.input:
    print(args.input)

# With requirement to run the python File version 
# import argparse 
# parser =argparse.ArgumentParser()
# parser.add_argument('-i', '--input', required=True)

# args = parser.parse_args()

# if args.input:
#     print(args.input)
