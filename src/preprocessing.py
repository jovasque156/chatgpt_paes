
import pdfplumber
import re
from src.utils import *

def label_pdf(args):
    '''
    This function write a txt file with the labeled text extracted from the pdf.
    Input:
        args.in_path: path to the pdf file
        args.out_path: path to the txt file
        args.start_questions: page number with the first question
        args.end_questions: page number with the last question
        
    '''
    labels = []
    splitted_text = []
    
    pdf = pdfplumber.open(args.in_path)
    for pages in pdf.pages[args.start_questions-1:(args.end_questions)]:
        text = pages.extract_text()
        for line in text.split('\n'):
            if re.match(r'^–.*–$', line) or re.match(r'-.*-$', line) or re.match(r'FORMA.*', line):
                if len(labels)>0 and (labels[-1]=='<head_reading>' or labels[-1]=='<reading>'):
                    continue
            define_label(line, labels)
            splitted_text.append(line)

    with open(args.out_path, 'w') as f:
        f.writelines([label+text+'\n' for label,text in zip(labels, splitted_text)])

def fix_labels(args):
    '''
    This function writes a txt file with the text extracted from the pdf file.
    Input:
        args.in_path: path to the pdf file
        args.out_path: path to the txt file
        args.start_questions: page number with the first question
        args.end_questions: page number with the last question

    '''
    with open(args.in_path, 'r') as f:
        text = f.readlines()
    
    texts = []
    for line in text:
        parts = line.split ('>')
        if len(parts) == 2:
            txt = parts[1].strip()
            texts.append(txt)

    labels = []
    final_text = []
    for line in texts:
        if re.match(r'^–.*–$', line) or re.match(r'-.*-$', line) or re.match(r'FORMA.*', line):
                if len(labels)>0 and (labels[-1]=='<head_reading>' or labels[-1]=='<reading>'):
                    continue
        define_label(line, labels)
        final_text.append(line)

    with open(args.out_path, 'w') as f:
        f.writelines([label+text+'\n' for label,text in zip(labels, final_text)])

def only_questions(args):
    '''
    This function writes a txt file only with the questions and alternatives from the labeled text,
    removing the head and foot texts.
    Input:
        args.in_path: path to the pdf file
        args.out_path: path to the txt file
        args.start_questions: page number with the first question
        args.end_questions: page number with the last question

    '''
    with open(args.in_path, 'r') as f:
        text = f.readlines()
    
    final_text = []
    labels = []
    for line in text:
        parts = line.split ('>')
        if len(parts) == 2:
            l = parts[0]+'>'
            txt = parts[1].strip()
            final_text.append(txt)
            labels.append(l)

    if args.only_questions:
        final_text = [text 
                        for text, label in zip(final_text, labels) 
                        if not(label=='<other>' or label=='<head_foot>')] 
        
        labels = filter(lambda x: not(x=='<other>' or x=='<head_foot>'), labels)

    with open(args.out_path, 'w') as f:
        f.writelines([label+text+'\n' for label,text in zip(labels, final_text)])