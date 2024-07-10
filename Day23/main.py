import numpy as np

def create_position_matrix(seq_length, embed_size):
  # chỉ số chẵn
  position_matrix = np.zeros((seq_length, embed_size))

  for pos in range(seq_length):
    inds_dimens = np.arange(embed_size)
    inds_even = inds_dimens[::2]
    inds_odd = inds_dimens[1::2]

    # Tính toán cho các chỉ số chẵn
    pe_even = 10000 ** ((2 * inds_even) / embed_size)
    position_matrix[pos, inds_even] = np.sin(pos / pe_even)

    print(pe_even)

    # Tính toán cho các chỉ số lẻ
    pe_odd = 10000 ** ((2 * inds_odd) / embed_size)
    position_matrix[pos, inds_odd] = np.cos(pos / pe_odd)

  return position_matrix

# def create_position_matrix(seq_length, embed_size):
#   position_matrix = np.zeros((seq_length, embed_size))
#   print("Position initial : \n", position_matrix)

#   for pos in range(seq_length):
#     for i in range(embed_size):
#       PE = 10000 ** ((2 * i) / embed_size)  # Công thức chuẩn
#       if i % 2 == 0:
#         position_matrix[pos, i] = np.sin(pos / PE)
#       else:
#         position_matrix[pos, i] = np.cos(pos / PE)
#   return position_matrix
def main():
  seq_length = 10
  embed_size = 16

  position_matrix = create_position_matrix(seq_length, embed_size)

  print(position_matrix)
  return position_matrix


if __name__ == "__main__":
  main()
