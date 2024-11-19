from .tibetan import TIBETAN_FILTER_WORDS


def get_default_filter_words(lang):
    #modification start
    #from ...tags import TAG_Tibetan
    #if lang == TAG_Tibetan:
    #modification end
    return TIBETAN_FILTER_WORDS
