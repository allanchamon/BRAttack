from OpenAttack.tags import Tag, TAG_ALL_LANGUAGE

TAG_Tibetan = Tag("tibetan", "lang")
TAG_Portuguese = Tag("portugues", "lang")


def add_tags():
    TAG_ALL_LANGUAGE.append(TAG_Tibetan)
    TAG_ALL_LANGUAGE.append(TAG_Portuguese)
