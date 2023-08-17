import argparse
from src.paes import *

if __name__ == '__main__':
    '''
    Example of use:
    python answer_paes.py --in_path preprocessed/admision_2023/regular/historia_only_q.txt --out_path results/admision_2023/regular/historia_gpt3.5.txt --model gpt-3.5-turbo --verbose
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_path', type=str, default='preprocessed/admision_2023/regular/historia_only_q.txt', help='Path to the processed PAES test')
    parser.add_argument('--out_path', type=str, default='results/admision_2023/regular/historia_gpt3.5.txt', help='Path to save the answer from the ChatGPT')
    parser.add_argument('--model', type=str, default='gpt-3.5-turbo', help='Model to use (gpt-3.5-turbo, gpt-4)')
    parser.add_argument('--verbose', action='store_true', help='Set to verbose the experiments')

    args = parser.parse_args()

    if args.verbose: print('Answering test...')
    answer_test(args)
    if args.verbose: print('Done!')