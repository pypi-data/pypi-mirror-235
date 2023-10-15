"""_summary_
"""
import argparse
import json
import os
import time

import requests


def init_command(args):
    """Initialize files 'dsl.txt' and 'theme.json' if they do not exist."""
    file_paths = ['dsl.txt', 'theme.json']
    
    for file_path in file_paths:
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8'):
                # Create the file if it does not exist
                pass

def delete_files_and_folders(directory=os.path.join(os.path.dirname(__file__), "src")):
    """_summary_

    Args:
        directory (_type_, optional): _description_. Defaults to os.path.join(os.path.dirname(__file__), "src").
    """
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                # print(f"Deleted file: {file_path}")
            except FileNotFoundError as exe:
                print(f"Error deleting file {file_path}: {exe}")

        for dire in dirs:
            dir_path = os.path.join(root, dire)
            try:
                os.rmdir(dir_path)
                # print(f"Deleted directory: {dir_path}")
            except FileNotFoundError as exe:
                print(f"Error deleting directory {dir_path}: {exe}")

def getcode_command(args):
    """_summary_

    Args:
        args (_type_): _description_
    """
    api_url = args.api_url
    rootpath = args.rootpath
    target_language = args.target_language

    dsl_payload = ''
    theme_payload = ''
    with open('dsl.txt', encoding='utf-8') as dsl:
        dsl_payload = dsl.read()

    dsl_payload = eval(dsl_payload)

    with open('theme.json', encoding='utf-8') as theme:
        theme_payload = json.load(theme)

    with open('theme.json', encoding='utf-8') as theme:
        theme_payload = json.load(theme)



    # Define the payload data you want to send as JSON (if needed)
    payload_data = {
        "dsl": dsl_payload,
        "theme_config": theme_payload,
        "target_language" : target_language
    }

    try:
    
        response = requests.post(api_url, json=payload_data, timeout=10)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and consume the API response (assuming it's JSON)
            api_response = json.loads(response.content)['response']

            delete_files_and_folders(os.path.join(rootpath,"demo_app"))
        
            for filename,_ in api_response.items():

            
                path = os.path.join(rootpath,"demo_app", filename)

                dir_name = os.path.dirname(path)

                if not os.path.exists(dir_name):
                    os.makedirs(dir_name)

                with open(path,"w", encoding='utf-8') as output:

                    if 'code' in api_response[filename]:
                        output.write(api_response[filename]['code'])
                    else:
                        output.write(api_response[filename])


                    time.sleep(1)

    
            print("wrote the files")
        

        else:
            print(f"Error: Request failed with status code {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    # Rest of the code remains the same...

def main():
    """_summary_
    """
    
    parser = argparse.ArgumentParser(description='My Python Package Commands')
    subparsers = parser.add_subparsers()

    # 'pc init' command
    init_parser = subparsers.add_parser('init', help='Create two empty files')
    init_parser.set_defaults(func=init_command)

    # 'pc getcode' command
    getcode_parser = subparsers.add_parser('getcode', help='Create a code directory')
    getcode_parser.set_defaults(func=getcode_command)
    getcode_parser.add_argument('--api-url', default="https://transpiledeploy.azurewebsites.net/transpile",
                                help='Specify the API URL (optional)')
    getcode_parser.add_argument('rootpath', help='Specify the root path (mandatory)')

    getcode_parser.add_argument('target_language', default="mui", help='Specify the target language for code (mui,tailwind,vanilla)')

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
