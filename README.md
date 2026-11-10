# xince-pptx-skill

> 深蓝工业科技风 · 可编辑 PowerPoint 商业计划书设计 Skill / An editable industrial-tech pitch-deck design skill.

将一份36页工业科技类商业计划书的**视觉语言**抽象为可重复使用的 Agent Skill。**本开源仓库不包含原始商业计划书、客户资料、知识产权文件、项目实拍和原始页面截图。** 示例内容均为占位文本和示意图，可编辑。

## 核心风格 / Visual DNA

- 深海军蓝大面积背景 + 科技蓝面板 / Deep navy foundation, tech-blue navigation
- 荧光青 HUD 细边框与轻量发光 / Cyan HUD outlines
- 电子蓝流程与数据 / Electric-blue metrics and flows
- 香槟金结论与大数字 / Champagne-gold claims and key metrics
- 冷白色中文无衬线字体 / Cool-white sans-serif text
- 真实设备、研发证据优先（无素材时使用占位） / Real engineering proof over decorative stock images

### 经过确认的8色 / Exact eight-color palette

| 色名 / Color | HEX | 用途 / Purpose |
|---|---|---|
| 深海军蓝 / Navy | `#081727` | Main background |
| 科技蓝 / Tech blue | `#174765` | Navigation and panels |
| 荧光青 / Cyan | `#24CDDF` | HUD lines and highlights |
| 电子蓝 / Electric blue | `#4C85D7` | Data and flow |
| 香槟金 / Champagne gold | `#DFC48C` | Key conclusions |
| 冷白色 / Cool white | `#F1F6FA` | Headlines and body text |
| 警示红 / Alert red | `#D62832` | Failures and risks |
| 验证绿 / Verified green | `#28AA83` | Validated or passed states |

主色板的单一可信来源是 [`assets/design-tokens.json`](assets/design-tokens.json) 中的 `canonical_palette`。

## 安装 / Install

```bash
git clone https://github.com/ggboyboyboy/xince-pptx-skill.git
```

把仓库目录添加至支持 Agent Skills 的工具（如 Codex 项目的 `.agents/skills/xince-pptx-skill/`），或让设计助手读取 [`SKILL.md`](SKILL.md)。仓库可以直接用来当技能目录；不必复制到 PPTX 文件里。

## 使用 / Usage

> 使用 `xince-pptx-skill` 的 `refined` 模式，按我提供的真实内容生成20页工业科技风融资路演PPT，严格使用八色主色板，输出可编辑的 `.pptx`。

- `faithful`：更接近原稿的多章节导航、技术 HUD 矩阵与结论条；仍限制文字过小。
- `refined`（默认）：保留视觉 DNA，降低元素密度，更适合成熟的 B2B/投资人演示。

## 文件结构 / Structure

```text
xince-pptx-skill/
├── SKILL.md                       # Agent Skill entrypoint
├── README.md                      # 中文/English usage
├── LICENSE                        # MIT
├── assets/
│   ├── design-tokens.json         # color, typography, spacing
│   ├── editable-starter.pptx      # 6-slide editable PowerPoint
│   ├── editable-starter-preview.jpg
│   └── style-reference-grid.jpg   # public demo imagery, NOT original deck
├── references/
│   ├── visual-spec.md
│   ├── layout-recipes.md
│   └── quality-gates.md
└── scripts/
    ├── build_starter.py
    └── validate_style.py
```

## 本地生成与校验 / Build and validate

需要 Python 3.9+ 和 `python-pptx`：

```bash
python -m pip install python-pptx
python scripts/build_starter.py
python scripts/validate_style.py assets/editable-starter.pptx
python scripts/check_palette.py
```

页面布局采用16:9；演示PPT以真实可编辑形状和文本实现，而不是用一张图片覆盖整页。

## 免责声明 / Disclaimer

本 Skill 提供**视觉设计规范**，不保证生成内容的数据真实性。公开版本中的图片和示意均来自公开可发布的原创模板；涉及知识产权、客户名单、合同金额、专利及企业商标的私人原始材料**没有上传**。按照用户提供的视觉风格抽象生成，不代表与任何半导体企业具有官方关联。

## 开源许可 / License

MIT — see [LICENSE](LICENSE).