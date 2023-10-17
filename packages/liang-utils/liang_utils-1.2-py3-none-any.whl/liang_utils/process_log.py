import os.path
import re
from argparse import ArgumentParser
from ttp import ttp
from tqdm import tqdm


def split_log(content: str, prompt_pattern: str):
    """
    split log content by prompt_pattern
    :param content: log content
    :param prompt_pattern: command prompt regex pattern
    :return: dict of log content which key is command and value is the corresponding content
    """

    current_show_command = 'ORPHAN_LINES'
    show_dict = dict()
    show_dict[current_show_command] = ''

    for line in content.split('\n'):
        res = re.findall(prompt_pattern, line)
        if res:
            current_show_command = res[0].strip()
            show_dict[current_show_command] = ''
        else:
            show_dict[current_show_command] += line + '\n'
    return show_dict


def parse_log(data, template, hook=None):
    """
    parse log data by given template
    :param data: log content
    :param template: TTP template
    :param hook: function which will be used to process the result
    :return: list of dict
    """
    parser = ttp(data=data, template=template)
    parser.parse()
    result = parser.result()
    data = list()
    if result[0][0]:
        for item in result[0][0].values():
            data.extend(item)
    if hook:
        return hook(data)
    return data


def split_log_file(file_path: str, prompt_pattern: str, output_dir: str = None):
    """
    split log file by prompt pattern
    :param file_path: log file path or log folder path
    :param prompt_pattern: command prompt regex pattern
    :param output_dir: output folder path
    """

    if not output_dir:
        output_dir = './output/'

    # create the output dir if not exist
    if output_dir and not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    log_file_list = list()

    if os.path.isdir(file_path):
        for file_name in os.listdir(file_path):
            log_file_list.append(os.path.join(file_path, file_name))
    else:
        log_file_list.append(file_path)

    for log_file in tqdm(log_file_list):
        print(f'splitting log file <{log_file}> ...')
        with open(log_file, 'r') as f:
            content = f.read()
        show_dict = split_log(content, prompt_pattern)

        hostname = os.path.basename(log_file).rsplit('.', 1)[0]
        host_dir = os.path.join(output_dir, hostname)
        # create host folder in output dir if not exist
        if not os.path.exists(host_dir):
            os.makedirs(host_dir)

        for show_command, show_content in show_dict.items():
            with open(os.path.join(host_dir, f'{show_command.replace(" ", "_").replace("?", "_").replace("|", "_").replace("*", "_").replace("/", "_")}.log'), 'w') as f:
                f.write(show_content)


def main():
    parser = ArgumentParser()
    parser.add_argument('action', choices=['split', 'parse'], type=str, help='split or parse')
    parser.add_argument('-i', '--input', type=str, required=True, help='input log file or log folder')
    parser.add_argument('-p', '--pattern', type=str, required=True, help='prompt pattern')
    parser.add_argument('-o', '--output', type=str, default=None, help='output folder')
    args = parser.parse_args()
    action = args.action

    input_source = args.input
    prompt_pattern = args.pattern
    output_dir = args.output

    if action.lower() == 'split':
        split_log_file(input_source, prompt_pattern, output_dir)
    else:
        print('Invalid ACTION')


if __name__ == '__main__':
    main()
