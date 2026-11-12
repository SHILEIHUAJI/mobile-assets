# 资源调用文档

## 资源索引

```text
assets.json
```

地址：

```text
https://cdn.jsdelivr.net/gh/用户名/mobile-assets@main/assets.json
```

---

## 壁纸

资源类型：

```text
wallpapers
```

资源路径：

```text
wallpapers/*
```

示例：

```text
wallpapers/vivo/wp1.jpg
```

---

## 头像

资源类型：

```text
avatars
```

资源路径：

```text
avatars/*
```

---

## 图标

资源类型：

```text
icon
```

资源路径：

```text
icon/*
```

---

## 字体

资源类型：

```text
fonts
```

资源路径：

```text
fonts/*
```

---

## Logo

资源类型：

```text
logos
```

资源路径：

```text
logos/*
```

---

## 前端获取随机资源

```js
const url =
await getRandomAsset('wallpapers');
```

返回：

```text
https://cdn.jsdelivr.net/gh/用户名/mobile-assets@main/wallpapers/vivo/wp1.jpg
```

---

## 自动更新

assets.json 由 GitHub Actions 自动生成。

新增资源后无需手动修改索引文件。
