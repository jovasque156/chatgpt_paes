from src.utils import *

def answer_test(args):
    """
    Answer a test from a file with the following format:
    <label> <text>
    <label> <text>
    ...

    Input:
        args.in_path: path to the file with the test
        args.out_path: path to the file where the answers will be saved
        args.model: model to use for the answers
        args.model_type: type of the model
    Output:
        None
    """

    if args.model =='gpt-3.5-turbo':
        max_tokens = 4096
    elif args.model =='gpt-4':
        max_tokens = 4096
    
    with open(args.in_path, 'r') as f:
        text = f.readlines()

    with open('system.txt', 'r') as f:
        system = f.read()

    query = ''
    tokens = num_tokens_from_string(system+query, 'cl100k_base')
    num_questions = 0
    last_label = ''
    answers = ''
    query_temp = ''

    lecture = False
    for l in text:
        label, text = l.replace('\n', ' ').split('>')
        if any([ x in label for x in ['id_question', 'prompt', 'choice', 'reading', 'head_reading']]):
            test = (('head_reading' in label) and ('choice' in last_label) and (lecture==True)) or (('id_question' in label) and ('choice' in last_label) and (lecture==False))
            if test:
                if tokens+num_tokens_from_string(query_temp, 'cl100k_base')+num_questions*4+4<=max_tokens:
                    query = query+query_temp
                    tokens = tokens + num_tokens_from_string(query_temp, 'cl100k_base')+num_questions*4
                    lecture=False
                else:
                    answer = obtain_answer(system, query, 'key.txt', args.model)
                    answers = answers+answer['choices'][0]['message']['content'] + '\n'
                    query = query_temp
                    tokens = num_tokens_from_string(system+query, 'cl100k_base')
                    last_label = ''

                num_questions = 0
                query_temp = ''
                    
            if 'head_reading' in label:
                query_temp = query_temp + '\n'+text+'\n'
                lecture=True
            if ('reading' in label) and ('head_reading' in last_label or 'reading' in last_label):
                query_temp = query_temp + text
            elif ('id_question' in label):
                query_temp = query_temp + '\n-Preguntas-\n'+text if 'reading' in last_label else query_temp + '\n'+text
                num_questions += 1
            elif ('prompt' in label) and ('id_question' in last_label or 'prompt' in last_label):
                query_temp = query_temp + text
            elif ('choice' in label) and ('choice' in last_label or 'prompt' in last_label):
                query_temp = query_temp+'\n'+text if any([alt in text[:2] for alt in ['A)', 'B)', 'C)', 'D)']]) else query_temp+text
            last_label = label

    if (len(query)>0 or len(query_temp)>0):
        if tokens+num_tokens_from_string(query_temp, 'cl100k_base')+num_questions*4+4<=max_tokens:
            query = query+query_temp        
        else:
            answer = obtain_answer(system, query, 'key.txt', args.model)
            answers = answers+answer['choices'][0]['message']['content'] + '\n'
            query = query_temp
        answer = obtain_answer(system, query, 'key.txt', args.model)
        answers = answers+answer['choices'][0]['message']['content'] + '\n'

    with open(args.out_path, 'w') as f:
        f.write(answers)
