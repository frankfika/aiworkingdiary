# PPT制作提示词模版

## 基本要求

请帮我创建一个HTML格式的演示文稿(PPT),要求如下:

### 1. 设计参考
- **参考模版**: `/Users/fangchen/Baidu/常规信息/课程和短视频制作/Ap2&402协议/AP2与x402协议-完整版.html`
- **设计风格**: 现代化、高端、科技感的PPT风格
- **语言要求**: 中文内容,保留必要的英文专业术语
- **响应式设计**: 内容必须自适应屏幕,绝对不能出现滚动条

### 2. 内容来源
本次演示的素材位于以下文件夹中:
- **文件夹路径**: [在此填写你的文件夹路径]
- **包含内容**:
  - 截图/图片 (./截图/ 或 ./images/ 文件夹)
  - 视频素材 (如有)
  - 内容大纲 (markdown或word文档)
  - 参考资料

请先阅读文件夹中的所有内容,理解主题和结构后再开始制作。

### 3. 核心主题
[在此简要描述你的PPT主题,例如:]
- 主题: [例如: AI支付协议、区块链技术、Web3应用等]
- 目标受众: [例如: 技术人员、投资者、普通用户等]
- 核心卖点: [3-5个关键信息点]

---

## 设计规范(必须遵循)

### CSS架构

```css
/* 核心布局 - 必须使用这些值 */
.slide {
    padding: 30px 50px;  /* 不要超过这个值 */
    overflow: hidden;     /* 禁止滚动 */
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.slide-content {
    transform: scale(0.95);  /* 整体缩放5%确保不溢出 */
    max-height: 100%;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

/* 字体层级系统 */
h1 { font-size: 56px; }
h2 { font-size: 38px; }
h3 { font-size: 20px; }
p { font-size: 15px; }
.subtitle { font-size: 18px; }

/* 组件间距 */
.feature-grid {
    gap: 20px;
    margin: 25px 0;
}

.stats-row {
    gap: 25px;
    margin: 25px 0;
}

/* 图片约束 - 非常重要! */
.screenshot, img {
    max-width: 85%;
    max-height: 400px;
    object-fit: contain;
}
```

### 颜色系统

```css
:root {
    --bg-dark: #0a0a0a;
    --bg-lighter: #1a1a1a;
    --accent: #00d9ff;
    --accent-glow: rgba(0, 217, 255, 0.3);
    --text-primary: #ffffff;
    --text-secondary: #a0a0a0;
    --border-color: rgba(255, 255, 255, 0.1);
}
```

### 响应式优化策略

如果某个页面出现内容溢出,按以下顺序调整:

1. **第一步**: 给该slide的内容添加inline style缩小字体
   ```html
   <h2 style="font-size: 32px; margin-bottom: 10px;">标题</h2>
   <p style="font-size: 13px;">内容</p>
   ```

2. **第二步**: 减少组件间距
   ```html
   <div class="feature-grid" style="gap: 15px; margin: 15px 0;">
   ```

3. **第三步**: 缩小图片尺寸
   ```html
   <img src="./截图/xx.png" style="max-width: 75%; max-height: 350px;">
   ```

4. **第四步**: 如果还不够,整体再scale一次
   ```html
   <div class="slide-content" style="transform: scale(0.9);">
   ```

---

## 内容结构建议

### 典型幻灯片结构(28页标准)

1. **封面** (1页)
   - 主标题 + 副标题
   - 视觉冲击力强的背景或图片

2. **目录/概览** (1页)
   - 简洁的章节列表
   - 使用icon增强视觉效果

3. **背景介绍** (2-3页)
   - 问题定义
   - 市场现状
   - 为什么重要

4. **核心技术/产品介绍** (8-10页)
   - 技术架构
   - 核心特性(使用feature-grid布局)
   - 技术优势对比
   - 官方截图展示

5. **应用案例** (5-7页)
   - 真实案例分析
   - 数据展示(使用stats-row布局)
   - 场景演示

6. **生态系统** (3-4页)
   - 合作伙伴
   - 技术栈
   - 社区支持

7. **未来展望** (2-3页)
   - 发展路线图
   - 市场预测
   - 机会分析

8. **总结** (1-2页)
   - 核心要点回顾
   - Call to Action

---

## 特殊元素使用指南

### 1. 数据统计卡片
```html
<div class="stats-row">
    <div class="stat-card">
        <div class="stat-number">8,218%</div>
        <div class="stat-label">7天涨幅</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">$30M</div>
        <div class="stat-label">峰值市值</div>
    </div>
</div>
```

### 2. 特性网格
```html
<div class="feature-grid">
    <div class="feature-item">
        <div class="feature-icon">⚡</div>
        <h3>极速结算</h3>
        <p>200毫秒内完成支付验证</p>
    </div>
</div>
```

### 3. 两栏布局
```html
<div class="two-col">
    <div>
        <h3>左侧标题</h3>
        <p>左侧内容</p>
    </div>
    <div>
        <h3>右侧标题</h3>
        <p>右侧内容</p>
    </div>
</div>
```

### 4. 案例研究卡片
```html
<div class="case-study">
    <h4>🔒 案例标题</h4>
    <p>案例描述内容</p>
    <div class="case-result">结果: 具体数据</div>
</div>
```

### 5. 截图展示
```html
<div style="text-align: center; margin: 30px 0;">
    <img src="./截图/文件名.png"
         alt="描述"
         class="screenshot"
         style="max-width: 85%; max-height: 400px; object-fit: contain;">
</div>
```

---

## 交互功能(必须包含)

### 1. 导航控制
```javascript
// 键盘导航
- 左箭头 ←: 上一页
- 右箭头 →: 下一页
- F键: 全屏切换
- ESC: 退出全屏
```

### 2. 全屏按钮
```html
<button id="fullscreenBtn" class="fullscreen-btn" onclick="toggleFullscreen()">
    ⛶ 全屏
</button>

<script>
document.addEventListener('fullscreenchange', function() {
    const btn = document.getElementById('fullscreenBtn');
    if (document.fullscreenElement) {
        btn.style.display = 'none';  // 全屏时隐藏按钮
    } else {
        btn.style.display = 'block';
    }
});
</script>
```

### 3. 进度指示器
```html
<div class="slide-number">
    <span id="currentSlide">1</span> / <span id="totalSlides">28</span>
</div>
```

---

## 注意事项

### ✅ 必须做的
1. **测试所有页面**: 确保每一页内容都不溢出屏幕
2. **图片优化**: 所有图片必须设置max-width和max-height
3. **数据准确**: 只使用已验证的数据,不确定的内容要标注或删除
4. **统一风格**: 所有页面使用一致的字体大小、间距、颜色
5. **响应式检查**: 在不同屏幕尺寸下测试(建议1920x1080为基准)

### ❌ 禁止做的
1. **不要添加滚动**: 任何情况下都不应该出现滚动条
2. **不要猜测数据**: 没有来源的数据不要编造
3. **不要过大图片**: 图片如果导致溢出必须缩小
4. **不要保留导航提示**: 底部的"Press → to continue"要删除
5. **不要用emoji过度**: 除非明确要求,否则适度使用

### 🔍 需要验证的内容
- 人名、公司名、具体日期
- 数据来源(市值、涨幅、用户数等)
- 技术规格(速度、费用、性能指标)
- 引用和声明

---

## 文件输出要求

### 文件命名
- 主文件: `[主题名称]-完整版.html`
- 单一HTML文件,包含所有CSS和JavaScript

### 文件结构
```
[项目文件夹]/
├── [主题]-完整版.html       # 主演示文件
├── 截图/                     # 图片素材文件夹
│   ├── 截图1.png
│   ├── 截图2.png
│   └── ...
├── 视频/                     # 视频素材(如有)
└── 大纲.md                   # 参考大纲
```

### 代码质量
- 代码缩进统一(2空格)
- CSS按模块组织(Layout → Typography → Components → Utilities)
- JavaScript功能模块化
- 添加必要的注释

---

## 最终检查清单

在交付前,请确认:

- [ ] 所有28页内容都不会溢出屏幕
- [ ] 图片都已正确显示并设置了尺寸限制
- [ ] 全屏功能正常,按钮在全屏时隐藏
- [ ] 键盘导航(← →)正常工作
- [ ] 页码显示正确(1/28 到 28/28)
- [ ] 所有数据都有来源或已标注为估算
- [ ] 颜色、字体、间距风格统一
- [ ] 没有拼写错误和格式问题
- [ ] 删除了底部导航提示文字
- [ ] 在1920x1080分辨率下测试通过

---

## 示例使用场景

**场景1**: 我要做一个关于AI Agent的演示
```
主题: AI Agent自主交易系统
文件夹: /Users/xxx/AI-Agent项目/
内容:
- 截图文件夹包含5张产品截图
- 大纲.md包含完整内容结构
- 参考资料.docx有详细技术说明

请按照上述模版制作一个28页的HTML演示文稿。
```

**场景2**: 我要做一个技术分享
```
主题: 区块链跨链桥技术深度解析
文件夹: /Users/xxx/跨链桥PPT/
素材:
- 架构图3张
- 对比表格2个
- 官网截图5张
- 内容大纲已在outline.md中

请制作一个技术风格的演示文稿,重点展示技术架构和性能对比。
```

---

## 后续优化建议

如果需要进一步定制,可以考虑:

1. **动画效果**: 添加slide进入/退出动画
2. **主题切换**: 支持亮色/暗色主题
3. **视频嵌入**: 直接在幻灯片中播放视频
4. **互动元素**: 添加可点击的热区或弹窗
5. **导出功能**: 添加PDF导出或截图功能

---

**参考文件**: `/Users/fangchen/Baidu/常规信息/课程和短视频制作/Ap2&402协议/AP2与x402协议-完整版.html`

**更新日期**: 2025-10-25
