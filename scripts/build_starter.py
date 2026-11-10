#!/usr/bin/env python3
"""Build a six-slide fully editable Xince-style demonstration PPTX.

Requires: python-pptx
Usage: python scripts/build_starter.py
"""
import json
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

ROOT = Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "assets/design-tokens.json").read_text(encoding="utf-8"))
P = TOKENS["canonical_palette"]
OUT = ROOT / "assets/editable-starter.pptx"

def color(name):
    return RGBColor.from_string(P[name].lstrip("#"))

def rect(slide, x, y, w, h, fill="tech_blue", outline=None, radius=False):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,
        Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = color(fill)
    if outline:
        shape.line.color.rgb = color(outline)
        shape.line.width = Pt(1.25)
    else:
        shape.line.fill.background()
    if radius:
        try: shape.adjustments[0] = 0.08
        except (IndexError, ValueError): pass
    return shape

def text(slide, value, x, y, w, h, size=18, fg="cool_white", bold=False, align=None):
    obj = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = obj.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.04)
    tf.margin_top = tf.margin_bottom = 0
    paragraph = tf.paragraphs[0]
    if align is not None: paragraph.alignment = align
    run = paragraph.add_run()
    run.text = value
    run.font.name = "Microsoft YaHei"
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color(fg)
    return obj

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]

def base(section, title, takeaway=None):
    s = prs.slides.add_slide(blank)
    rect(s, 0, 0, 13.333, 7.5, "navy")
    rect(s, 0, 0, 13.333, 0.49, "tech_blue")
    text(s, "XINCE / INDUSTRIAL TECH", .46, .10, 4.3, .31, 14, "cool_white", True)
    text(s, section.upper(), 10.1, .10, 2.65, .30, 13, "cyan", True, PP_ALIGN.RIGHT)
    text(s, title, .56, .77, 12.0, .62, 30, "cool_white", True)
    rect(s, .57, 1.49, 1.25, .045, "cyan")
    if takeaway:
        rect(s, .42, 6.67, 12.49, .55, "tech_blue")
        text(s, takeaway, .68, 6.76, 11.9, .38, 18, "champagne_gold", True)
    return s

def card(s, x, y, w, h, heading, body, metric=None):
    rect(s, x, y, w, h, "tech_blue", "cyan", True)
    text(s, heading, x+.23, y+.22, w-.46, .43, 20, "cyan", True)
    if metric is not None:
        text(s, metric, x+.23, y+.77, w-.46, .72, 36, "champagne_gold", True)
        text(s, body, x+.23, y+1.66, w-.46, h-1.83, 16)
    else:
        text(s, body, x+.23, y+.90, w-.46, h-1.07, 18)

# Slide 1: cover
s = prs.slides.add_slide(blank)
rect(s, 0, 0, 13.333, 7.5, "navy")
rect(s, 8.65, .0, 4.68, 7.5, "tech_blue")
for i in range(5):
    rect(s, 9.13+i*.61, 1.03+i*.53, .09, 3.3, "cyan")
rect(s, 9.04, 3.02, 3.5, 2.1, "navy", "cyan", True)
text(s, "ENGINEERING", 9.30, 3.46, 2.9, .42, 19, "cyan", True)
text(s, "[Editable device visual]", 9.31, 4.07, 3.0, .45, 15)
text(s, "工业硬科技\n商业演示", .69, 1.65, 7.6, 2.18, 47, "cool_white", True)
text(s, "Industrial Technology Pitch Deck", .75, 4.13, 7.4, .55, 23, "cyan")
text(s, "XINCE STYLE  /  DESIGN SYSTEM DEMO", .76, 6.45, 8.1, .38, 15, "champagne_gold", True)

# Slide 2: trend
s = base("01 / opportunity", "市场趋势与机会", "用真实的数据、单位和来源证明机会，而不是装饰性曲线。")
card(s, .56, 1.96, 3.48, 3.93, "市场规模", "[Placeholder: add verified market data and year]", "XX 亿")
card(s, 4.30, 1.96, 3.48, 3.93, "增长趋势", "[Placeholder: add period and reliable source]", "XX%")
card(s, 8.04, 1.96, 4.66, 3.93, "商业意义", "客户正在解决什么真实问题？\n\n给出一个有证据支持的需求驱动因素。")

# Slide 3: pain points
s = base("02 / pain", "工业客户的三项核心痛点", "痛点 → 成本与效率损失 → 可以测量的改进空间。")
card(s, .56, 1.95, 3.95, 3.92, "01 / 人工流程", "描述当前操作瓶颈。\n\n[现场照片占位]")
card(s, 4.69, 1.95, 3.95, 3.92, "02 / 质量风险", "描述不良率与损伤风险。\n\n[现场照片占位]")
card(s, 8.82, 1.95, 3.95, 3.92, "03 / 交付瓶颈", "描述产能和交付周期。\n\n[现场照片占位]")

# Slide 4: architecture
s = base("03 / solution", "技术架构：软硬件协同", "方案设计 → 工程实现 → 实测验证")
card(s, .60, 2.08, 3.75, 3.80, "SOFTWARE", "上位机控制 / 识别 / 数据分析\n\n[待填真实功能]")
card(s, 4.80, 2.08, 3.75, 3.80, "HARDWARE", "电子控制 / PCB / 电气接口\n\n[待填真实器件]")
card(s, 9.00, 2.08, 3.75, 3.80, "MECHANICAL", "设备结构 / 执行机构\n\n[待填真实测试结果]")
for x in (4.42, 8.62):
    rect(s, x, 3.86, .31, .09, "cyan")

# Slide 5: KPI
s = base("04 / proof", "性能验证与经营指标", "只使用有来源、可复核的测试与经营数据。")
card(s, .56, 2.01, 3.70, 3.89, "效率提升", "以测试条件为准", "XX 倍")
card(s, 4.42, 2.01, 3.70, 3.89, "良率验证", "以样本量为准", "XX%")
card(s, 8.28, 2.01, 4.43, 3.89, "客户价值", "把技术性能转换为可衡量的成本、质量或交付收益。\n\n[验证证据占位]")

# Slide 6: closing
s = prs.slides.add_slide(blank)
rect(s, 0, 0, 13.333, 7.5, "navy")
rect(s, 0, 6.42, 13.333, .05, "cyan")
text(s, "用工程能力创造\n可验证的产业价值", .85, 1.86, 11.9, 2.15, 43, "cool_white", True)
text(s, "XINCE-STYLE  /  INDUSTRIAL TECH", .87, 5.25, 10.3, .48, 21, "champagne_gold")

OUT.parent.mkdir(parents=True, exist_ok=True)
prs.save(str(OUT))
print(f"Created {OUT} ({len(prs.slides)} slides, editable objects)")
