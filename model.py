
from transformers import BartTokenizer, BartForConditionalGeneration
import torch

# check if GPU is available
if torch.cuda.is_available():
   device = torch.device("cuda")
else:
   device = torch.device("cpu")


class Summary:
    def __init__(self):
        #creates a bart model object from the pretrained bart model on huggingface transformers library 
        self.bart_model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn").to(device)
        # creates a tokenizer object from the pretrained model and the vocab file
        self.bart_tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

    def summary(self,input_text): 

        input_text = ' '.join(input_text.split('+'))
        # tokenize the input text and convert it to a pytorch tensor 
        input_tokenized = self.bart_tokenizer.encode(input_text, return_tensors='pt').to(device)
        # generate the summary from the input tokenized text 
        summary_ids = self.bart_model.generate(input_tokenized,
                                            num_beams = 4,
                                            num_return_sequences = 1,
                                            no_repeat_ngram_size = 2,
                                            length_penalty = 1,
                                            min_length = 70,
                                            max_length = 150,
                                            early_stopping = True)
        # convert the generated summary to a string 
        output = [self.bart_tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
        return output[0]


