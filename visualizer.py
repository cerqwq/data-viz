"""
Data Viz - AI数据可视化工具
自动生成图表代码和可视化建议
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class DataVisualizer:
    """
    AI数据可视化工具
    支持：图表生成、可视化建议、数据洞察
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def suggest_chart(self, data_description: str, goal: str = "") -> Dict:
        """建议图表类型"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为以下数据建议可视化方案：

数据描述：{data_description}
目标：{goal or '展示数据特征'}

请返回JSON格式：
{{
    "charts": [
        {{
            "type": "图表类型",
            "name": "图表名称",
            "description": "适用场景",
            "library": "推荐库（matplotlib/plotly/echarts）",
            "code": "Python代码示例"
        }}
    ],
    "best_practices": ["最佳实践1", "最佳实践2"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except Exception as e:
            return {"error": str(e)}

        return {"suggestion": content}

    def generate_chart_code(self, data: Any, chart_type: str, library: str = "matplotlib") -> str:
        """生成图表代码"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{library}代码，创建{chart_type}图表：

数据：{json.dumps(data[:10] if isinstance(data, list) else data, ensure_ascii=False)}

要求：
1. 完整可运行的代码
2. 中文标签
3. 美观的样式
4. 包含图例和标题"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def analyze_data(self, data: Any) -> Dict:
        """分析数据并提供洞察"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析以下数据并提供洞察：

数据：{json.dumps(data[:20] if isinstance(data, list) else data, ensure_ascii=False)}

请返回JSON格式：
{{
    "summary": "数据概述",
    "patterns": ["发现的模式1", "模式2"],
    "anomalies": ["异常点1", "异常点2"],
    "insights": ["洞察1", "洞察2"],
    "recommendations": ["建议1", "建议2"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except Exception as e:
            return {"error": str(e)}

        return {"analysis": content}

    def generate_dashboard(self, data_description: str, metrics: List[str] = None) -> str:
        """生成仪表板代码"""
        if not self.client:
            return "LLM客户端未配置"

        metrics = metrics or ["指标1", "指标2", "指标3"]
        metrics_text = "、".join(metrics)

        prompt = f"""请生成一个Streamlit仪表板代码：

数据描述：{data_description}
展示指标：{metrics_text}

要求：
1. 使用Streamlit
2. 包含多个图表
3. 支持交互筛选
4. 美观的布局"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4000
        )

        return response.choices[0].message.content

    def generate_report(self, data: Any, analysis: Dict) -> str:
        """生成数据报告"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请根据以下数据和分析生成报告：

数据：{json.dumps(data[:10] if isinstance(data, list) else data, ensure_ascii=False)}
分析：{json.dumps(analysis, ensure_ascii=False)}

请生成Markdown格式的报告，包含：
1. 执行摘要
2. 数据概述
3. 关键发现
4. 可视化建议
5. 结论和建议"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content


def create_visualizer(**kwargs) -> DataVisualizer:
    """创建数据可视化工具"""
    return DataVisualizer(**kwargs)


if __name__ == "__main__":
    viz = create_visualizer()

    print("Data Visualization Tool")
    print()

    # 测试数据
    test_data = [
        {"month": "1月", "sales": 100, "profit": 20},
        {"month": "2月", "sales": 120, "profit": 25},
        {"month": "3月", "sales": 90, "profit": 18},
        {"month": "4月", "sales": 150, "profit": 35},
    ]

    print("Suggesting charts...")
    result = viz.suggest_chart("月度销售数据", "展示销售趋势")
    print(json.dumps(result, ensure_ascii=False, indent=2)[:500] + "...")
