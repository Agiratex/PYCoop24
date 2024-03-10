import cowsay
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Python implementation of cowsay')
    parser.add_argument('message', nargs='?', default='Hello, World!', help='The message to be displayed by the cow')
    parser.add_argument('-c', '--cow', action='store', help='Which cow to use')
    parser.add_argument('-e', '--eye', help='Specify the cow\'s eye')
    parser.add_argument('-f', '--file', help='Specify a cowfile')
    parser.add_argument('-l', '--list', action='store_true', help='Call cowsay.list_cows()')
    parser.add_argument('-T', '--tongue', help='Specify the cow\'s tongue')
    parser.add_argument('-W', '--wrap', type=int, help='Specify maximum column width for output')
    parser.add_argument('-n', '--no-wrap', action='store_true', help='Do not use word-wrapping')
    
    return parser.parse_args()

def main():
    args = get_args()

    if args.list:
        print(cowsay.list_cows())
    else:
        cow = 'default'

        if args.cow:
            cow = args.cow

        eye = args.eye if args.eye else 'oo'
        file = args.file if args.file else None
        
        tongue = args.tongue if args.tongue else '  '
        wrap = args.wrap if args.wrap else 40
        
        no_wrap = False if args.no_wrap else True
        
        print(cowsay.cowsay(message=args.message, cowfile=file, cow=cow, eyes=eye, wrap_text=no_wrap, tongue=tongue, width=wrap))

if __name__ == '__main__':
    main()