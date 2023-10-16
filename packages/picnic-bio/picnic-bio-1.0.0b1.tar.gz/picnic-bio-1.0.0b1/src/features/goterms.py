import json

import pandas as pd
import requests


def get_go_from_api(uniprot_id: str) -> list:

    res_terms = []
    url = "https://rest.uniprot.org/uniprotkb/search?query=" + uniprot_id + "&format=json"
    all_fastas = requests.get(url).text

    obj = json.loads(all_fastas)

    for song in obj["results"]:
        for attribute, value in song.items():
            if attribute == "uniProtKBCrossReferences":
                for db in value:
                    if db["database"] == "GO":
                        res_terms.append(db["id"])

    return res_terms


def calculate_3dir_go_one(uniprot_id: str, input_file_dir: str) -> dict:

    go = {}
    prot = {}
    go["go_terms_molecular_functions"] = "mf_2500_freq_all.json"
    go["go_terms_biological_processes"] = "bp_2500_freq_all.json"
    go["go_terms_cellular_component"] = "cc_2000_freq_all.json"

    go2 = {}
    go2["go_terms_molecular_functions"] = "mf_2500_freq.txt"
    go2["go_terms_biological_processes"] = "bp_2500_freq.txt"
    go2["go_terms_cellular_component"] = "cc_2000_freq.txt"

    for k, v in go.items():
        mf = pd.read_csv(input_file_dir + go2[k], sep=" ")
        mft = set(mf["num"])
        with open(input_file_dir + v) as json_file:
            mf = json.load(json_file)
        for kel in mft:
            prot[kel] = 0

        mapterms = mf

        translated = set()
        goterms = get_go_from_api(uniprot_id)

        if type(goterms) is list:
            if len(goterms) > 0:
                for t in goterms:
                    t = t.strip()

                    if t in mapterms.keys():

                        for el in mapterms[t]:
                            translated.add(el)

            for t in sorted(mft):

                num = list(translated).count(t)

                prot[t] = num

    return prot


if __name__ == "__main__":
    print("GO terms")  # noqa: T201
