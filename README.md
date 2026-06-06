# 📊 Data Viz

AI数据可视化工具，自动生成图表代码和可视化建议。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Matplotlib-Chart-green" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📈 图表类型建议
- 🎨 图表代码生成
- 📊 数据分析洞察
- 📋 仪表板生成
- 📄 数据报告生成

## 🚀 快速开始

```bash
pip install openai

python visualizer.py
```

## 📖 使用

```python
from data_viz import create_visualizer

viz = create_visualizer()

# 建议图表
suggestion = viz.suggest_chart("月度销售数据", goal="展示趋势")

# 生成图表代码
code = viz.generate_chart_code(data, "折线图", library="matplotlib")

# 分析数据
analysis = viz.analyze_data(data)

# 生成仪表板
dashboard = viz.generate_dashboard("销售数据", ["销售额", "利润", "增长率"])

# 生成报告
report = viz.generate_report(data, analysis)
```

## 📁 项目结构

```
data-viz/
├── visualizer.py  # 数据可视化核心
└── README.md
```

## 📄 许可证

MIT License
