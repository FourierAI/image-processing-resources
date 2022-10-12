# # 向量化操作
# arr_test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i in range(len(arr_test)):
#     for j in range(len(arr_test)):
#         arr_test[i][j] = arr_test[i][j] + 1
#
# print(arr_test)
#
import numpy as np
#
# arr_test = np.array(arr_test)
# arr_test  = arr_test * 10
# print(arr_test)

# 求一个序列的sin波形 (采样频率)

# X = np.arange(0, 2*np.pi, 1)
# # print(X)
# Y = np.sin(X)
#
# print(X)
# print(Y)
#
# import matplotlib.pyplot as plt
# plt.plot(X,Y)
# plt.show()

# numpy生成随机数以及查找操作
# noise = np.random.randint(0, 256, (5,6))
# print(noise)
# import matplotlib.pyplot as plt
#
# plt.imshow(noise, cmap='gray')
# plt.show()
#
# print(noise > 126)
# plt.imshow((noise > 126).astype('int'), cmap='gray')
# plt.show()
#
# print(np.where(noise > 126))