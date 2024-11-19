import sys
import os
import ssl

sys.path.append(os.getcwd())

import OpenAttack
import open_attack
from datasets import load_dataset

"""
def dataset_mapping(data):
    return {
        "x": data.strip().split('\t')[1],
        "y": data.strip().split('\t')[0]
    }
"""
def dataset_mapping(data):
    return {
        "x": data["text"],
        "y": data["label"]
    }

def main():
    print("Loading Attacker...")
    ssl._create_default_https_context = ssl._create_unverified_context

    attacker = open_attack.attackers.TextFoolerAttacker(lang="english")

    print("Loading Victim ...")
    victim = OpenAttack.loadVictim("BERTimbau+TTSBR")
  
    print("Loading Dataset ...")
    path_var=os.path.join(os.getcwd(), "data", "Dataset.Loader", "TU_SA.py")
    print("path_var:" + path_var )
    #dataset = load_dataset('csv', data_files='C:/Users/allan/Documents/TSAttack/data/Dataset.TTSBR/test.txt', delimiter='\t', column_names=['label', 'text'])
    dataset = load_dataset(path=path_var, split="test",trust_remote_code=True).map(function=dataset_mapping)
    #print(dataset['train'][:5])  # Print the first 5 rows


    print("Start Attack!")
    attack_eval = open_attack.AttackEval(attacker, victim, "english", metrics=[])
    attack_eval.eval(dataset, visualize=True, progress_bar=True)


if __name__ == "__main__":
    main()
