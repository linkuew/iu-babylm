'''
TODO: finish setting up tokenizer code
TODO: create custom model code
'''

from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer

from tokenizers.pre_tokenizers import Whitespace


def build_tokenizer():
    tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
    trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])

    return tokenizer, trainer

def train_tokenizer(tokenizer, trainer):
    tokenizer.pre_tokenizer = Whitespace()

