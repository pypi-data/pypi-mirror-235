import torch
from transformers import AutoTokenizer

def identify(hex):  
    try:
        # get path to model and tokenizer from C: di
        model_path = 'C:/neural-av/identifibert.pt'
        tokenizer_path = 'C:/neural-av/tokenizer'
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        model = torch.load(model_path, map_location=torch.device('cpu'))
        tokens = tokenizer(hex, padding=True, truncation=True, return_tensors='pt')
        with torch.no_grad():
            outputs = model(tokens['input_ids'], tokens['attention_mask'])
        return "Benign" if torch.argmax(outputs[0], dim=1).numpy()[0] == 1 else "Malicious"
    except Exception as e:
        return e

def classify(hex):
    try:
        model_path = 'C:/neural-av/classifibert.pt'
        tokenizer_path = 'C:/neural-av/tokenizer'
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        model = torch.load(model_path, map_location=torch.device('cpu'))
        tokens = tokenizer(hex, padding=True, truncation=True, return_tensors='pt')
        with torch.no_grad():
            outputs = model(tokens['input_ids'], tokens['attention_mask'])
        return str(outputs[0].tolist()[0])
    except Exception as e:
        return e
