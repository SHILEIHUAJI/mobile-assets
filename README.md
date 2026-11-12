## 当前资源统计

本仓库资源索引由 GitHub Actions 自动维护。

资源清单：

- assets.json

资源分类：

- wallpapers（壁纸）
- avatars（头像）
- fonts（字体）
- icon（图标）
- logos（Logo）
- temp（临时文件）

---

## 目录结构

```text
.
├── wallpapers
├── avatars
├── fonts
├── icon
├── logos
├── temp
└── assets.json
```

---

## 资源说明

### wallpapers

项目背景图和壁纸资源。

可用于：

- 主页背景
- 音乐台背景
- 启动页背景
- 锁屏样式背景

支持按品牌或主题分类：

```text
wallpapers/
├── vivo/
├── xiaomi/
├── samsung/
├── anime/
└── nature/
```

---

### avatars

默认头像资源。

用于：

- 用户头像
- 游客头像
- 评论头像

---

### fonts

项目字体资源。

支持：

- ttf
- otf
- woff
- woff2

---

### icon

图标资源。

用于：

- 导航栏
- 菜单
- 控制按钮
- 状态图标

推荐优先使用 SVG。

---

### logos

项目 Logo。

用于：

- 网站标识
- PWA 图标
- 分享卡片

---

### temp

临时测试目录。

不保证长期保留。

---

## 自动索引

仓库通过 GitHub Actions 自动生成：

```text
assets.json
```

每次提交资源后自动更新。

前端无需维护资源列表。

---

## 前端调用示例

随机获取壁纸：

```js
const data = await fetch(assetsJsonUrl)
  .then(r => r.json());

const list = data.wallpapers.files;

const file =
  list[Math.floor(Math.random() * list.length)];

const url =
  cdnPrefix +
  '/wallpapers/' +
  file;
```

---

## 说明

本仓库主要服务于：

- 个人项目/工具
- 导航页
- PWA应用
- 实验性前端项目

仅作为静态资源仓库使用。
