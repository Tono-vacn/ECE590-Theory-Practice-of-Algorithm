import matplotlib.pyplot as plt


data = [
  (512, 0.00010, 0.01716, 0.00255),
  (1024, 0.00013, 0.29560, 0.06226),
  (2048, 0.00036, 0.56760, 0.02407),
  (4096, 0.00073, 1.84010, 0.11372),
  (8192, 0.00105, 8.37546, 0.63015),
  (16384, 0.00290, 43.57670, 2.91763)
]

sizes = [item[0] for item in data]
many_dup_times = [item[1] for item in data]
moderate_dup_times = [item[2] for item in data]
rare_dup_times = [item[3] for item in data]

# 创建一个新的图形
plt.figure(figsize=(10, 5))

# 绘制三条曲线
plt.plot(sizes, many_dup_times, label='best', marker='o')
plt.plot(sizes, moderate_dup_times, label='worst', marker='s')
plt.plot(sizes, rare_dup_times, label='random', marker='^')

# 添加图例
plt.legend()

# 设置坐标轴的标签
plt.xlabel('Size')
plt.ylabel('Time (seconds)')

# 添加一个标题
plt.title('Performance of substr function')

# 显示网格
plt.grid(True)

# 显示图形
plt.show()