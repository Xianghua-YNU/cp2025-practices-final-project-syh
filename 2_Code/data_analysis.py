"""数据分析：分形维数计算、曲线拟合、数据处理"""
import numpy as np
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=UserWarning)

def calculate_fractal_dimension(n):
    """计算带扰动项的有效分形维数"""
    theoretical_dim = np.log(8) / np.log(3)
    perturbation = 0.05 * np.sin(n)
    return theoretical_dim + perturbation

def calculate_complexity_index(n):
    """计算分形复杂度指数 CI = n(n+1)/2"""
    return n * (n + 1) / 2

def fractal_rcs_model(x, a, b, c):
    """分形复杂度-RCS指数拟合模型"""
    return a * np.exp(-b * x) + c

def fit_complexity_rcs(complexity_indices, avg_rcs):
    """拟合复杂度与RCS的关系"""
    try:
        popt, _ = curve_fit(fractal_rcs_model, complexity_indices, avg_rcs, p0=[1e-2, 1, 1e-2])
        return popt, True
    except:
        return None, False

def save_simulation_data(all_freqs, all_rcs_mom, all_rcs_bem, complexity_indices, fractal_dims, avg_rcs):
    """保存模拟数据至CSV文件"""
    import os
    os.makedirs("results", exist_ok=True)
    
    # 保存各迭代次数的RCS频响数据
    for i, (freqs, rcs_mom, rcs_bem) in enumerate(zip(all_freqs, all_rcs_mom, all_rcs_bem)):
        iteration = i + 1
        data = np.column_stack((freqs/1e9, 10*np.log10(rcs_mom), 10*np.log10(rcs_bem)))
        np.savetxt(f"results/fractal_iteration_{iteration}_rcs.csv", 
                   data, delimiter=',', header='Frequency (GHz), RCS_MoM (dBsm), RCS_BEM (dBsm)')
    
    # 保存复杂度-分形维数-RCS关系数据
    data = np.column_stack((complexity_indices, fractal_dims, avg_rcs))
    np.savetxt("results/fractal_dimension_rcs.csv", 
               data, delimiter=',', header='Complexity Index, Fractal Dimension, Average RCS (m²)')
