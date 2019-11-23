import nltk
import pandas as pd

from nltk.tokenize import word_tokenize

import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.tag import CRFTagger


from Sastrawi.Stemmer.StemmerFactory import StemmerFactory #Stemmer Bahasa Indonesia

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# create stopwordremover
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

#POS Tagger
ct = CRFTagger()
ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')

def strip_html(html_str):
    html_str = BeautifulSoup(html_str).get_text().replace('\n',' ')
    html_str = BeautifulSoup(html_str).get_text().replace('\xa0',' ')
    html_str_list = html_str.split()
    html_str = []
    for i in html_str_list:
        html_str.append(i.strip())
    html_str = ' '.join(html_str)
    return html_str


def stem_string(string_data):
    return stemmer.stem(string_data)
    
def stop_string(string_data):
    return stopword.remove(string_data)

def tokenize_string(string_data):
    return nltk.word_tokenize(string_data)

def pos_stop(tokens):
    return ct.tag_sents([tokens])

def omit_words(pos_stop):
    df_stopped = pd.DataFrame(columns = ['item','type'], data = pos_stop[0])
    omit = ['CD','NEG','Z','X','OD','WH','SYM']
    processed_df = df_stopped[~df_stopped['type'].isin(omit)]
    ranking = processed_df['item'].value_counts()
    return ranking

def find_content_keyword(string_data,n_keywords=20,output_type='dict'):    
    # stemming process
    string_data   = stemmer.stem(string_data)
    # stopword removing process
    string_data = stopword.remove(string_data)
    tokens = nltk.word_tokenize(string_data)
    pos_stop = ct.tag_sents([tokens])
    df_stopped = pd.DataFrame(columns = ['item','type'], data = pos_stop[0])
    omit = ['CD','NEG','Z','X','OD','WH','SYM']
    processed_df = df_stopped[~df_stopped['type'].isin(omit)]
    ranking = processed_df['item'].value_counts()
    
    data_dict = ranking[0:n_keywords]
    if output_type == 'dict':
        return data_dict
    elif output_type == 'list':
        keywords = data_dict.index.to_list()
        keywords_freq = data_dict.to_list()
        return keywords, keywords_freq
    else:
        raise ValueError('output_type not available, choose "dict" or "list" ')

def find_title_keyword(string_data, output_type='dict'):   
    # stemming process
    string_data   = stemmer.stem(string_data)

    tokens = nltk.word_tokenize(string_data)

    pos_stop = ct.tag_sents([tokens])
    df_stopped = pd.DataFrame(columns = ['item','type'], data = pos_stop[0])

    ranking = df_stopped['item'].value_counts()

    if output_type == 'dict':
        return ranking
    elif output_type == 'list':
        keywords = ranking.index.to_list()
        keywords_freq = ranking.to_list()
        return keywords, keywords_freq
    else:
        raise ValueError('output_type not available, choose "dict" or "list" ')

# title_string = '''Hati-Hati, Diet Tinggi Tingkatkan Risiko Penyakit Jantung'''
# string_data='''Jakarta - Diet mengurangi karbohidrat sedang ngetren belakangan ini. Banyak yang menggantinya dengan asupan tinggi lemak dan protein. Tapi awas, dokter jantung mengingatkan risikonya bagi jantung.Dokter jantung dari RS Awal Bross, dr Yudistira Panji Sentosa, SpPD-KKV, menyebut diet tinggi lemak bisa memicu penumpukan kolesterol. Bila berlanjut, dampaknya bisa meningkatkan risiko serangan jantung."Kita tidak tahu lemak yang kita konsumsi lemak jahat atau lemak baik, semua terkumpul di dalam tubuh kita. Kalau semakin meningkat di dalam darah lama-lama akan terjadi penimbunan," kata dr Yudis, ditemui di Jakarta Pusat, Selasa (2/10/2018).'''


# keyword_dict = find_content_keyword(string_data)
# print(keyword_dict)
# title_key = find_title_keyword(title_string)
# print(title_key)