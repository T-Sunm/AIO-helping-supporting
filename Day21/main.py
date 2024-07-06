import numpy as np
import math

def vocab_bag(docs):
  terms = set(term for doc in docs for term in doc.split())
  return list(terms)

# Bước 2: tính tần số
def compute_tf(vocabs, doc: str):
  tf_ans = []
  words = doc.split()
  len_words = len(words)
  for vocab in vocabs:
    c_w = words.count(vocab)
    tf_ans.append(c_w / len_words)
  return np.array(tf_ans)

# Bước 3: Tính toán IDF và trả về mảng NumPy
def compute_idf(vocabs, docs):
  idf_dict = {}
  len_docs = len(docs)
  # Tính idf từng từ
  for term in vocabs:
    c_w = sum(1 for doc in docs if term in doc.split())
    idf_dict[term] = math.log((len_docs) / (1 + c_w))

  # Tạo mảng NumPy cho IDF
  idf_ans = np.zeros(len(vocabs))
  for index, vocab in enumerate(vocabs):
    idf_ans[index] = idf_dict[vocab]
  return idf_ans

# Bước 4: Tính toán TF-IDF
def compute_tf_idf(tf, idf):
  return tf * idf

def main():
  documents = ["Tôi thích học AI", "AI là trí tuệ nhân tạo",
               "AGI là siêu trí tuệ nhân tạo"]

  vocabs = vocab_bag(documents)
  print(f"Vocabulary: {vocabs}\n")

  tf = []
  for doc in documents:
    tf.append(compute_tf(vocabs, doc))
  tf = np.array(tf)
  print(f"TF: {tf}\n")

  idf = compute_idf(vocabs, documents)
  print(f"IDF: {idf}\n")

  tf_idf = []
  for tf_doc in tf:
    tf_idf.append(compute_tf_idf(tf_doc, idf))
  tf_idf = np.array(tf_idf)
  print(f"TF-IDF: {tf_idf}")

  for doc_index, document in enumerate(documents):
    words = document.split()
    print(f"Tài liệu {doc_index + 1}:")
    for vocab, tf_idf_value in zip(vocabs, tf_idf[doc_index]):
      if vocab in words:
        print(f"{vocab}: {tf_idf_value:.4f}")
        print()


if __name__ == "__main__":
  main()
