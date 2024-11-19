from OpenAttack.utils import make_zip_downloader

NAME = "Victim.BERTimbau+TTSBR"

DOWNLOAD = make_zip_downloader("")


def LOAD(path):
    from transformers import BertForSequenceClassification, BertTokenizer
    model = BertForSequenceClassification.from_pretrained(path, num_labels=3)
    tokenizer = BertTokenizer.from_pretrained(path)

    from OpenAttack.victim.classifiers import TransformersClassifier
    return TransformersClassifier(model, tokenizer, embedding_layer=model.bert.embeddings.word_embeddings,
                                  max_length=512, batch_size=8, lang="english")
