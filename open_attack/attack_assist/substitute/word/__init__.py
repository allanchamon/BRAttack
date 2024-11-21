from .tibetan_word2vec import TibetanWord2VecSubstitute
from .portuguese_word2vec import PortugueseWord2VecSubstitute

def get_default_substitute(lang):
    from ....tags import TAG_Tibetan, TAG_Portuguese
    if lang == TAG_Tibetan:
        return TibetanWord2VecSubstitute()
    if lang == TAG_Portuguese:
        return PortugueseWord2VecSubstitute()
    return PortugueseWord2VecSubstitute()
