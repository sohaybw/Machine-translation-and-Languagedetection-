from transformers import MarianTokenizer, MarianMTModel
import torch


saved_model_directory = "static/Model_translation/"  
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def load_model(): 
    # Load the tokenizer
    tokenizer = MarianTokenizer.from_pretrained(saved_model_directory)

    # Load the model
    model = MarianMTModel.from_pretrained(saved_model_directory)

    # Ensure the model is on the desired device (GPU if available)
    model = model.to(device)

    return tokenizer , model 


def run_model (input_text):


    tokenizer , model  = load_model()

    tokenized = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True, max_length=64).to(device)

    # Translate from English to Arabic
    translated_arabic = model.generate(**tokenized, max_length=64, num_beams=4, early_stopping=True)

    # Decode and print the translated Arabic sentence
    result = tokenizer.decode(translated_arabic[0], skip_special_tokens=True)


    return result 
    

