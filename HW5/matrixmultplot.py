import matplotlib.pyplot as plt

#       4,      8,     16,     32,     64,    128,    256,    512,
# 0.00007,0.00024,0.00155,0.01507,0.07950,0.63463,4.31851,33.22417,
# 0.00507,0.00023,0.00142,0.01082,0.07822,0.54637,4.14101,62.58999,
# 0.01166,0.00058,0.00409,0.02717,0.15284,1.05783,6.06876,34.99945,


data = [
  (4, 0.00004, 0.00400, 0.00417),
  (8, 0.00013, 0.00012, 0.00012),
  (16, 0.00101, 0.00400, 0.00085),
  (32, 0.00988, 0.00640, 0.00774),
  (64, 0.08039, 0.05330, 0.05454),
  (128, 0.59022, 0.41712, 0.44878),
  (256, 4.63811, 3.39450, 3.49501),
  (512, 32.81978, 33.46625, 33.08475)
]

sizes = [item[0] for item in data]
many_dup_times = [item[1] for item in data]
moderate_dup_times = [item[2] for item in data]
rare_dup_times = [item[3] for item in data]

# 创建一个新的图形
plt.figure(figsize=(10, 5))

# 绘制三条曲线
plt.plot(sizes, many_dup_times, label='Many', marker='o')
plt.plot(sizes, moderate_dup_times, label='Square', marker='s')
plt.plot(sizes, rare_dup_times, label='Few', marker='^')

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