# 2_code/ -源代码目录

**目的:** 存放所有用于模拟、分析和可视化的代码。代码的质量是评分的重要组成部分。

**内容:**
- **main_simulation.py:** 主程序。负责设置参数、调用其他模块的函数、控制整个模拟流程。
- **numerical_methods.py:** 核心算法。实现具体的数值方法，例如龙格-库塔法、Crank-Nicolson、Metropolis算法等。这个模块应该具有通用性，不依赖于特定的模拟场景。
- **data_analysis.py:** 数据分析。存放用于处理 raw_data 的函数，例如计算平均值、误差、傅里叶变换、拟合曲线等。
- **visualization.py:** 可视化。存放所有绘图函数。这些函数应该接收数据作为输入，然后生成图表。这使得绘图逻辑与计算逻辑分离。
- **utils.py (可选):** 存放一些通用的辅助函数，比如读取配置文件、计时等。
- **requirements.txt (可选):** 项目依赖。通过 pip freeze > requirements.txt 命令生成，确保任何人都可以在新环境中复现你们的计算环境。
- **README.md:** 代码说明书。必须清晰地说明：
  - 每个代码文件的功能。
  - 如何配置环境 (pip install -r requirements.txt)。
  - 如何运行主程序 (python main_simulation.py)。

功能说明
main_simulation.py：设置迭代次数、频率范围等参数，调用各模块完成模拟全流程
numerical_methods.py：实现谢尔宾斯基分形生成、矩量法（MoM）和边界元法（BEM）
data_analysis.py：计算分形维数、复杂度指数，拟合复杂度 - RCS 关系
visualization.py：生成分形动画、绘制 RCS 频响曲线和复杂度 - RCS 关系图
输出结果
动画文件：assets/sierpinski_animation.gif（分形生成过程）
图表文件：
results/rcs_frequency_response.png（RCS 频响曲线）
results/complexity_rcs_relationship.png（复杂度 - RCS 关系）
数据文件：
results/fractal_iteration_X_rcs.csv（各迭代次数的 RCS 频响数据）
results/fractal_dimension_rcs.csv（复杂度 - 分形维数 - RCS 关系）

## 注意：
你也可以不按照预设的目录结构，按照自己的喜好组织代码，只要能够清晰地说明每个文件的功能即可。
