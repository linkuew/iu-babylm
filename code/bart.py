'''
A starting script for the task of building a LLM using a 'developmentally accurate' corpus

TODO: finish setting up custom tokenizer code
TODO: create custom model code
'''

from library import *

def main():
    tokenizer, trainer = build_tokenizer()
    train_tokenizer(tokenizer, trainer)

if __name__ == "__main__":
    main()
