import pandas as pd
from random import randint


# test purpose
df = pd.DataFrame({'subject_uid': [randint(1, 9) for x in range(10)],
                   'audio_path': [randint(1, 9)*10 for x in range(10)],
                   'pcr_test_result_inferred': ['dddd' if randint(1, 9)==1 else 'positive' for x in range(10)],
                   'audio_type': [randint(1, 9)*100 for x in range(10)]})


def test_column_names(df):
    if not set(['subject_uid',
                'audio_path',
                'audio_type',
                'country',
                'source',
                'pcr_test_result',
                'pcr_test_result_inferred']).issubset(df.columns):
        return False
    return True

def test_label_values(df):
    string={'positive',
            'negative',
            'recovered',
            'unknown'}
    for s in df['pcr_test_result_inferred']:
        if not set([s]).issubset(string):
            return False
    return True
    
def test_all(df):
    if not test_column_names(df):
        print("Some columns are missing")
        return False
    if not test_label_values(df):
        print("Invalid string included")
        return False
    return True

if __name__ == '__main__':
    print(test_all(df))
