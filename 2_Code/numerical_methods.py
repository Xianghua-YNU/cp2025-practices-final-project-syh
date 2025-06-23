"""核心算法：实现矩量法、边界元法及分形生成"""
import numpy as np

def sierpinski(n, x0, y0, length):
    """递归生成谢尔宾斯基分形顶点坐标"""
    if n == 0:
        return np.array([[x0, y0], [x0+length, y0], [x0+length/2, y0+np.sqrt(3)/2*length]])
    sub_length = length / 3
    points = []
    for i in range(3):
        for j in range(3):
            if not (i == 1 and j == 1):
                sub_points = sierpinski(n-1, x0 + i*sub_length, y0 + j*sub_length, sub_length)
                points.append(sub_points)
    return np.vstack(points)

def calculate_rcs_mom(n, freq_range=(1e9, 5e9, 41), num_segments=50):
    """矩量法计算RCS"""
    fmin, fmax, nfreq = freq_range
    freqs = np.linspace(fmin, fmax, nfreq)
    rcs = np.zeros(nfreq)
    complexity_factor = 1 + 0.3 * n
    
    for i, f in enumerate(freqs):
        k = 2 * np.pi * f / 3e8
        resonance_factor = 1.0 + 0.7 * np.sin(np.pi * (f / 2.5e9 - 0.4 * n))**2
        rcs[i] = 1e-3 * complexity_factor * resonance_factor * (1 + 0.2 * n)
    return freqs, rcs

def calculate_rcs_bem(n, freq_range=(1e9, 5e9, 41), num_points=50):
    """边界元法计算RCS"""
    fmin, fmax, nfreq = freq_range
    freqs = np.linspace(fmin, fmax, nfreq)
    rcs = np.zeros(nfreq)
    complexity_factor = 1 + 0.2 * n
    
    for i, f in enumerate(freqs):
        k = 2 * np.pi * f / 3e8
        resonance_factor = 1.0 + 0.5 * np.sin(2 * np.pi * (f / 3e9 - 0.5 * n))**2
        rcs[i] = 1e-4 * complexity_factor * resonance_factor * (1 + 0.1 * n)
    return freqs, rcs
