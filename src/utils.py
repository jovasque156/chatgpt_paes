import re
import tiktoken
import openai

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    '''
    Returns the number of tokens of a string given an encoding
    
    Inputs
    string : str, String to be encoded
    encoding_name : str, Name of the encoding to be used

    Output
    num_tokens: int, Number of tokens of the string

    '''
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def obtain_answer(system_content, user_content, key_path, model):
    '''
    Returns the answer from the ChatGPT

    Inputs
    system_content : str, System content
    user_content : str, User content
    key_path : str, Path to the key
    model : str, Model to use (gpt-3.5-turbo, gpt-4)

    Output
    response : str, Answer from the ChatGPT

    '''
    with open(key_path, 'r') as f:
        key = f.read()

    openai.api_key = key

    response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "system", "content": system_content},
            {"role": "user", "content": user_content}]
        )
    return response

def define_label(line, labels):
    '''
    Defines the label of a line

    Inputs
    line : str, Line to be labeled
    labels : list, List of labels

    Output
    labels : list, List of labels
    
    '''
    if re.match(r'^–.*–$', line) or re.match(r'-.*-$', line) or re.match(r'FORMA.*', line):
        labels.append('<head_foot>')
    elif re.match(r'^\d+\.$', line):
        labels.append('<id_question>')
    elif re.match(r'^[A-Za-z]\)', line):
        labels.append('<choice>')
    elif (len(labels)>0) and (labels[-1]=='<head_reading>' or labels[-1]=='<reading>'):
        labels.append('<reading>')
    elif (len(labels)>0) and (labels[-1]=='<id_question>' or labels[-1]=='<prompt>'):
        labels.append('<prompt>')
    elif 'lectura' in line.lower():
        labels.append('<head_reading>')
    elif (len(labels)>0) and labels[-1]=='<choice>':
        labels.append('<choice>')
    else:
        labels.append('<other>')