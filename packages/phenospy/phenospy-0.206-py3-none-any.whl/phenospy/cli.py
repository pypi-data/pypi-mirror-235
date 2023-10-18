# cli.py

from .phs_mainConvert import phsToOWL
import argparse
import os

import warnings
# Set the warning filter to suppress all warnings
warnings.filterwarnings("ignore")


def command1(args):
    # Implement logic for command 1
    print(f"Executing command 1 with arguments: {args.arg1}")

def phs2owl(args):
    print("Executing phs2owl ... ")
    # Split the path into directory and filename
    directory, filename = os.path.split(args.arg2)
    # Check if the output directory exists and create it if necessary
    if not os.path.exists(directory):
        os.makedirs(directory)
    #
    phs_file    = args.phs_file
    yaml_file   = 'phs-config.yaml'
    save_dir    = directory
    save_pref   = filename
    phsToOWL(phs_file, yaml_file, save_dir, save_pref)

def main():
    parser = argparse.ArgumentParser(description="Phenospy Command-Line Tools")
    
    subparsers = parser.add_subparsers(title="commands", dest="command")

    parser_command1 = subparsers.add_parser("phs2owl", help="Convert phs file to OWL")
    parser_command1.add_argument("phs_file", help="Input file phs file.")
    parser_command1.add_argument("output_base", help="Base name for output files. Note, two output files will be produced (xml and owl).")

    parser_command2 = subparsers.add_parser("owl2md", help="Convert OWL file to Markdown")
    parser_command2.add_argument("arg1", help="Argument for command 1")
    
    args = parser.parse_args()
    
    if args.command == "owl2md":
        command1(args)
    elif args.command == "phs2owl":
        phs2owl(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()




# #-----
# # Get the current directory
# current_dir = '/Users/taravser/Library/CloudStorage/OneDrive-UniversityofHelsinki/My_papers/PhenoScript_main/Phenoscript-Descriptions/phenoscript_grebennikovius/sergei-tests/for_Jim'

# current_dir = '/Users/taravser/Library/CloudStorage/OneDrive-UniversityofHelsinki/My_papers/PhenoScript_main/Phenoscript-Descriptions/phenoscript_grebennikovius/sergei-tests/for_Jim/Greb_toy.owl'
# os.path.dirname(current_dir)

# os.path.split('outf1')
# # -----------------------------------------
# # ARGUMENTS
# # -----------------------------------------
# phs_file    = os.path.join(current_dir, 'Grebennikovius_toy-example.phs')
# yaml_file   = os.path.join(current_dir, 'phs-config.yaml')
# save_dir    = os.path.join(current_dir, 'output/')
# #save_pref   = 'Greb_toy'
# save_pref   = 'Greb_toy_updated'

# # -----------------------------------------
# # Convert PHS to OWL and XML
# # -----------------------------------------
# phsToOWL(phs_file, yaml_file, save_dir, save_pref)

# # -----------------------------------------
# # OWL to Markdown
# # -----------------------------------------
# # get owl file
# owl_file = os.path.join(save_dir, save_pref + '.owl')

# # Make NL graph
# onto = owlToNLgraph(owl_file)


# # --------
# # cli.py

# import argparse

# def command1(args):
#     # Implement logic for command 1
#     print(f"Executing command 1 with arguments: {args.arg1}")

# def command2(args):
#     # Implement logic for command 2
#     print("Executing command 2")

# def main():
#     parser = argparse.ArgumentParser(description="My CLI Tool")
    
#     subparsers = parser.add_subparsers(title="commands", dest="command")
    
#     parser_command1 = subparsers.add_parser("command1", help="Description of command 1")
#     parser_command1.add_argument("arg1", help="Argument for command 1")
    
#     parser_command2 = subparsers.add_parser("command2", help="Description of command 2")
    
#     args = parser.parse_args()
    
#     if args.command == "command1":
#         command1(args)
#     elif args.command == "command2":
#         command2(args)

# if __name__ == "__main__":
#     main()
