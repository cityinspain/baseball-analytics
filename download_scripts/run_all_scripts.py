#!/usr/bin/env python3

"""Run all scripts"""

__author__ = 'Stephen Diehl'

import argparse
import sys
import subprocess


def get_parser():
    """Args Description"""

    # current_year = datetime.datetime.today().year
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("--data-dir", type=str, help="baseball data directory", default='../data')
    parser.add_argument("--start-year", type=int, help="start year", default='1955')
    parser.add_argument("--end-year", type=int, help="end year", default='2019')

    return parser


def run_cmd(cmd):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    for line in proc.stdout:
        sys.stdout.buffer.write(line)
        sys.stdout.buffer.flush()


def main():
    parser = get_parser()
    args = parser.parse_args()
    data_dir = f'--data-dir={args.data_dir}'
    start_year = f'--start-year={args.start_year}'
    end_year = f'--end-year={args.end_year}'

    print('Running lahman_download:')
    cmd = ['./lahman_download.py', '-v', '--log=INFO', data_dir]
    run_cmd(cmd)

    print('Running lahman_wrangle:')
    cmd = ['./lahman_wrangle.py', '-v', '--log=INFO', data_dir]
    run_cmd(cmd)

    print('Running retrosheet_download:')
    cmd = ['./retrosheet_download.py', '-v', '--log=INFO', data_dir]
    run_cmd(cmd)

    print('Running retrosheet_parse:')
    cmd = ['./retrosheet_parse.py', '-v', '--log=INFO', '--run-cwevent', data_dir, start_year, end_year]
    run_cmd(cmd)

    print('Running retrosheet_collect:')
    cmd = ['./retrosheet_collect.py', '-v', '--log=INFO', '--use-datatypes', data_dir]
    run_cmd(cmd)

    print('Running retrosheet_wrangle:')
    cmd = ['./retrosheet_wrangle.py', '-v', '--log=INFO', data_dir]
    run_cmd(cmd)

    print('Running pytest:')
    cmd = ['pytest', '-v', data_dir]
    run_cmd(cmd)
    print('All scripts have run.')


if __name__ == '__main__':
    main()