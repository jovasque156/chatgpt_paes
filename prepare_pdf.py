import argparse
from src.preprocessing import *

import ipdb

if __name__ == '__main__':
    '''
    Example of use:
    python prepare_pdf.py --in_path ensayos/regular_2023/2023-22-03-31-modelo-historia.pdf --out_path preprocessed/regular_2023/historia.txt --label --verbose
    
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_path', type=str, default='ensayos/regular_2023/2023-22-11-30-paes-oficial-historia-p2023.pdf', help='Path to the PDF file with the PAES test')
    parser.add_argument('--out_path', type=str, default='preprocessed/regular_2023/historia.txt', help='Path to save the processed file')
    parser.add_argument('--start_questions', type=int, default=3, help='Page number where questions start')
    parser.add_argument('--end_questions', type=int, default=47, help='Page number where questions end')
    parser.add_argument('--label', action='store_true', help='Set to labeling the pdf')
    parser.add_argument('--fix', action='store_true', help='Set to fix teh labeling')
    parser.add_argument('--only_questions', action='store_true', help='Set to remove useless labels')
    parser.add_argument('--verbose', action='store_true', help='Set to verbose the processing')

    args = parser.parse_args()

    checker = iter([args.label, args.fix, args.only_questions])
    assert any(checker) and not any(checker), 'Only one must be set: --label, --fix, or --only_questions'

    if args.label:
        if args.verbose: print('Labeling pdf...')
        label_pdf(args)
        if args.verbose: print('Done!')
        print()

    if args.fix:
        if args.verbose: print('Fixing...')
        fix_labels(args)
        if args.verbose: print('Done!')

    if args.only_questions:
        if args.verbose: print('Getting only questions...')
        only_questions(args)
        if args.verbose: print('Done!')

