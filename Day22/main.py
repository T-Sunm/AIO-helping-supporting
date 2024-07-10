import numpy as np

def main():
  # Giúp kết quả giống nhau trên mọi máy khi tạo random
  np.random.seed(42)

  # Bước 1 Tạo từ điển và mã hóa từ
  vocab = {
      "Tôi": 0,
      "thích": 1,
      "AI": 2
  }

  # Số lượng từ vựng
  vocab_size = len(vocab)

# Kích thước vector embedding
  embedding_dim = 4


# Khởi tạo ma trận embedding ngẫu nhiên
# với số cột là = embedding_dim để có thể tích vô hướng
  embedding_matrix = np.random.rand(vocab_size, embedding_dim)

# chuỗi đầu vào đã được mã hóa thành các vector embedding
  input_seq = np.array([embedding_matrix[vocab[word]] for word in vocab])
  print("Chuỗi đầu vào (đã mã hóa):\n", input_seq)

 # Bước 2: Khởi tạo các ma trận trọng số cho Q, K, V
  w_q = np.random.rand(embedding_dim, embedding_dim)
  w_k = np.random.rand(embedding_dim, embedding_dim)
  w_v = np.random.rand(embedding_dim, embedding_dim)

  # Tính toán Q, K, V
  Q = np.dot(input_seq, w_q)
  K = np.dot(input_seq, w_k)
  V = np.dot(input_seq, w_v)

  print("Ma trận Query Q:\n", Q)
  print("Ma trận Key K:\n", K)
  print("Ma trận Value V:\n", V)

  # Bước 3: Tính toán Attetion score
  scores = np.dot(Q, K.T)
  # Chia cho căn bậc hai của kích thước chiều của vector key
  d_k = np.shape(K)[1]
  scores = scores / np.sqrt(d_k)

  print("Điểm số:\n", scores)

  # Bước 4: Áp dụng hàm softmax

  def softmax(x):
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)

  attention_weights = softmax(scores)

  print("Trọng số Attention :\n", attention_weights)
  output = np.dot(attention_weights, V)

  print("Đầu ra :\n", output)


if __name__ == "__main__":
  main()
