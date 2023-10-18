# cli.py

import argparse

def command1(args):
    # Implement logic for command 1
    print(f"Executing command 1 with arguments: {args.arg1}")

def main():
    parser = argparse.ArgumentParser(description="Phenospy CLI Tool")
    
    subparsers = parser.add_subparsers(title="commands", dest="command")
    
    parser_command1 = subparsers.add_parser("command1", help="Description of command 1")
    parser_command1.add_argument("arg1", help="Argument for command 1")
    
    args = parser.parse_args()
    
    if args.command == "command1":
        command1(args)

if __name__ == "__main__":
    main()
