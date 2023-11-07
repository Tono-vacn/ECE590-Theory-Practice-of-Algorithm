import matplotlib.pyplot as plt

data = [
  (4096,0.00128, 0.00043, 0.00358),
  (8192,0.00090, 0.00143, 0.00227),
  (16384,0.00118, 0.00200, 0.00547),
  (32768,0.00173, 0.00234, 0.00864),
  (65536,0.00342, 0.00841, 0.01361),
  (131072,0.00688, 0.01239, 0.02791),
  (262144,0.01385, 0.02668, 0.06755),
  (524288,0.02631, 0.06083, 0.16712),
  (1048576,0.06140, 0.16168, 0.42303),
  (2097152,0.13161, 0.50594, 0.89401),
  (4194304,0.33982, 1.28853, 1.96349)
    ]

sizes = [item[0] for item in data]
many_dup_times = [item[1] for item in data]
moderate_dup_times = [item[2] for item in data]
rare_dup_times = [item[3] for item in data]

# 创建一个新的图形
plt.figure(figsize=(10, 5))

# 绘制三条曲线
plt.plot(sizes, many_dup_times, label='Many Duplicates', marker='o')
plt.plot(sizes, moderate_dup_times, label='Moderate Duplicates', marker='s')
plt.plot(sizes, rare_dup_times, label='Rare Duplicates', marker='^')

# 添加图例
plt.legend()

# 设置坐标轴的标签
plt.xlabel('Size')
plt.ylabel('Time (seconds)')

# 添加一个标题
plt.title('Performance of rmdup function')

# 显示网格
plt.grid(True)

# 显示图形
plt.show()