# 🗂️ 静态资源库

统一管理个人项目所需的公共静态资源。

适用于：

- 网站
- 导航页
- PWA 应用
- WebView 项目
- 浏览器主页
- 工具页
- 实验项目

---

## 📦 资源分类

```text
wallpapers   壁纸
avatars      头像
fonts        字体
icon         图标
logos        标识
temp         临时资源
```

---

## 📁 仓库结构

```text
.
├── wallpapers
├── avatars
├── fonts
├── icon
├── logos
├── temp
├── assets.json
└── build_assets.py
```

---

## 🖼️ wallpapers

壁纸与背景图片资源。

示例结构：

```text
wallpapers/
├── vivo/
├── xiaomi/
├── samsung/
├── anime/
├── nature/
└── abstract/
```

适用于：

- 网站背景
- 启动页背景
- 首页背景
- 欢迎页背景
- 全屏展示页面

---

## 👤 avatars

头像资源。

适用于：

- 默认头像
- 游客头像
- 用户资料图片

---

## 🔤 fonts

字体资源。

支持格式：

```text
ttf
otf
woff
woff2
```

---

## 🎯 icon

图标资源。

适用于：

- 功能按钮
- 导航菜单
- 控制面板
- 状态图标

推荐格式：

```text
svg
png
```

---

## 🏷️ logos

项目标识资源。

适用于：

- 网站 Logo
- 应用 Logo
- PWA 图标
- 分享封面

---

## 🧪 temp

临时测试资源。

该目录内容可能随时调整或清理。

不建议正式项目长期依赖。

---

## 📋 资源索引

所有资源自动生成索引文件：

```text
assets.json
```

示例：

```json
{
  "wallpapers": {
    "count": 18,
    "files": [
      "vivo/wp1.jpg",
      "vivo/wp2.jpg"
    ]
  }
}
```

---

## 🌐 CDN访问

推荐使用 jsDelivr：

```text
https://cdn.jsdelivr.net/gh/用户名/仓库名@main
```

示例：

```text
https://cdn.jsdelivr.net/gh/用户名/仓库名@main/wallpapers/vivo/wp1.jpg
```

---

## 🚀 使用示例

获取资源清单：

```js
const data = await fetch(
  'https://cdn.jsdelivr.net/gh/用户名/仓库名@main/assets.json'
).then(r => r.json());
```

随机获取壁纸：

```js
const list = data.wallpapers.files;

const file =
  list[Math.floor(Math.random() * list.length)];

const url =
  `https://cdn.jsdelivr.net/gh/用户名/仓库名@main/wallpapers/${file}`;
```

---

## 🔄 自动更新

仓库资源索引由 GitHub Actions 自动维护。

新增、修改或删除资源后：

```text
提交资源
    ↓
GitHub Actions
    ↓
自动生成 assets.json
    ↓
索引同步更新
```

无需手动维护资源列表。

---

## 📌 仓库定位

本仓库仅用于存放和分发静态资源。

特点：

- 统一管理
- 自动索引
- CDN 加速
- 多项目共用
- 零业务耦合

可作为任何项目的公共资源仓库直接使用。
