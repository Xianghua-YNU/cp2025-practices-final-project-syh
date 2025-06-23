"""可视化：绘图函数与动画生成"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False  # 正确显示负号

def create_sierpinski_animation(max_iterations, filename):
    """生成谢尔宾斯基分形生成动画"""
    from numerical_methods import sierpinski
    fig, ax = plt.subplots(figsize=(8, 8))
    
    def update(frame):
        ax.clear()
        points = sierpinski(frame, 0, 0, 1)
        ax.fill(points[:, 0], points[:, 1], 'k')
        ci = calculate_complexity_index(frame)
        ax.set_title(f'迭代次数: {frame}, 复杂度指数: {ci:.2f}')
        ax.set_xlim(-0.1, 1.1), ax.set_ylim(-0.1, 1.1)
        ax.axis('off')
    
    ani = FuncAnimation(fig, update, frames=range(max_iterations + 1), interval=1000)
    ani.save(filename, writer='pillow', fps=1)
    plt.close()

def calculate_complexity_index(n):
    """计算复杂度指数（供可视化模块调用）"""
    return n * (n + 1) / 2

def plot_rcs_frequency_response(all_freqs, all_rcs_mom, all_rcs_bem):
    """绘制RCS频响曲线"""
    plt.figure(figsize=(12, 8))
    for i, (freqs, rcs_mom, rcs_bem) in enumerate(zip(all_freqs, all_rcs_mom, all_rcs_bem)):
        n = i + 1
        plt.plot(freqs/1e9, 10*np.log10(rcs_mom), label=f'迭代 {n} (MoM)', linewidth=2)
        plt.plot(freqs/1e9, 10*np.log10(rcs_bem), '--', label=f'迭代 {n} (BEM)', linewidth=1.5)
    
    plt.xlabel('频率 (GHz)'), plt.ylabel('RCS (dBsm)')
    plt.title('谢尔宾斯基分形的RCS频响特性')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(), plt.tight_layout()
    plt.savefig("results/rcs_frequency_response.png", dpi=300)
    plt.close()

def plot_complexity_rcs_relationship(complexity_indices, avg_rcs, fit_params, fit_success):
    """绘制复杂度与RCS的关系曲线"""
    plt.figure(figsize=(12, 8))
    plt.scatter(complexity_indices, 10*np.log10(avg_rcs), color='red', s=80, label='模拟数据')
    
    if fit_success:
        a, b, c = fit_params
        x_fit = np.linspace(min(complexity_indices), max(complexity_indices), 100)
        rcs_fit = a * np.exp(-b * x_fit) + c
        plt.plot(x_fit, 10*np.log10(rcs_fit), 'blue', linewidth=2,
                 label=f'拟合曲线: y = {a:.2f}e${{-{b:.2f}x}}$ + {c:.2f}')
    
    plt.xlabel('结构复杂度指数'), plt.ylabel('平均RCS (dBsm)')
    plt.title('谢尔宾斯基分形复杂度与RCS的关系')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(), plt.tight_layout()
    plt.savefig("results/complexity_rcs_relationship.png", dpi=300)
    plt.close()
