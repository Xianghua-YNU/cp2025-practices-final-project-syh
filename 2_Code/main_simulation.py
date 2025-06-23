"""主程序：设置参数、调用模块函数、控制模拟流程"""
import numpy as np
from numerical_methods import calculate_rcs_mom, calculate_rcs_bem, sierpinski
from data_analysis import calculate_fractal_dimension, calculate_complexity_index, fit_complexity_rcs
from visualization import create_sierpinski_animation, plot_rcs_frequency_response, plot_complexity_rcs_relationship

def main():
    # 参数设置
    max_iterations = 4
    freq_range = (1e9, 5e9, 41)  # 1-5GHz，41个采样点
    
    # 1. 生成谢尔宾斯基分形动画
    create_sierpinski_animation(max_iterations, "assets/sierpinski_animation.gif")
    
    # 2. 计算不同迭代次数的RCS
    all_freqs, all_rcs_mom, all_rcs_bem = [], [], []
    for n in range(1, max_iterations + 1):
        print(f"计算迭代 {n}/{max_iterations}...")
        freqs, rcs_mom = calculate_rcs_mom(n, freq_range)
        _, rcs_bem = calculate_rcs_bem(n, freq_range)
        all_freqs.append(freqs)
        all_rcs_mom.append(rcs_mom)
        all_rcs_bem.append(rcs_bem)
    
    # 3. 分析分形维数与平均RCS的关系
    fractal_dims = [calculate_fractal_dimension(n) for n in range(1, max_iterations + 1)]
    complexity_indices = [calculate_complexity_index(n) for n in range(1, max_iterations + 1)]
    avg_rcs = [np.mean(rcs) for rcs in all_rcs_mom]
    
    # 4. 拟合复杂度与RCS的关系
    fit_params, fit_success = fit_complexity_rcs(complexity_indices, avg_rcs)
    
    # 5. 绘制RCS频响曲线
    plot_rcs_frequency_response(all_freqs, all_rcs_mom, all_rcs_bem)
    
    # 6. 绘制复杂度-RCS关系曲线
    plot_complexity_rcs_relationship(complexity_indices, avg_rcs, fit_params, fit_success)
    
    # 7. 保存数据文件
    save_simulation_data(all_freqs, all_rcs_mom, all_rcs_bem, complexity_indices, fractal_dims, avg_rcs)
    print("所有计算完成！结果已保存至 ./results/ 目录")

if __name__ == "__main__":
    main()
