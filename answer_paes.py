import argparse
from src.paes import *

if __name__ == '__main__':
    '''
    Example of use:
    python paes.py --in_path preprocessed/comprension_only_q.txt --out_path results/comprension.txt --verbose --model gpt-3.5-turbo
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_path', type=str, default='preprocessed/regular_2023/historia_only_q.txt', help='Path to the processed PAES test')
    parser.add_argument('--out_path', type=str, default='results/regular_2023/historia_gpt3.5.txt', help='Path to save the answer from the ChatGPT')
    parser.add_argument('--model', type=str, default='gpt-3.5-turbo', help='Model to use (gpt-3.5-turbo, gpt-4)')
    parser.add_argument('--verbose', action='store_true', help='Set to verbose the experiments')

    args = parser.parse_args()

    if args.verbose: print('Answering test...')
    answer_test(args)
    if args.verbose: print('Done!')