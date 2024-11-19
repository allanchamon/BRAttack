from .punct_tokenizer import PunctTokenizer

def get_default_tokenizer(lang):
#    from ...tags import TAG_Portuguese
#    if lang == TAG_Portuguese:
    return PunctTokenizer()
