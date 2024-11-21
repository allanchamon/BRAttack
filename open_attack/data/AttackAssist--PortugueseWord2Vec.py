from OpenAttack.utils import make_zip_downloader
import gensim

NAME = "AttackAssist.PortugueseWord2Vec"

DOWNLOAD = make_zip_downloader("")


def LOAD(path):
    import os
    import numpy as np
    from OpenAttack.attack_assist import WordEmbedding

    word2id = {}
    embeddings = []

    model = gensim.models.KeyedVectors.load_word2vec_format(
        "cbow_s300.txt",
        binary=False,
        unicode_errors='ignore')
    print(model.vector_size)  # Dimensionality of the embeddings
    return WordEmbedding(word2id, embeddings)

"""
    with open(os.path.join(path, "cbow_s300.txt"), "r", encoding="utf-8") as f:
        for index, line in enumerate(f.readlines()):
            tmp = line.strip().split(" ")
            word = tmp[0]
            embedding = np.array([float(x) for x in tmp[1:]])
            word2id[word] = index
            embeddings.append(embedding)
        embeddings = np.stack(embeddings)
"""        
