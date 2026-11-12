# 🚀 Mobile Assets 使用文档

## 仓库地址

```text
https://github.com/SHILEIHUAJI/mobile-assets
```

---

## CDN根地址

```text
https://cdn.jsdelivr.net/gh/SHILEIHUAJI/mobile-assets@main
```

---

## 资源索引

```text
https://cdn.jsdelivr.net/gh/SHILEIHUAJI/mobile-assets@main/assets.json
```

---

# 📦 资源分类

当前支持：

```text
wallpapers
avatars
fonts
icon
logos
temp
```

---

# 🖼️ 文件访问规则

格式：

```text
https://cdn.jsdelivr.net/gh/SHILEIHUAJI/mobile-assets@main/{分类}/{文件路径}
```

示例：

```text
https://cdn.jsdelivr.net/gh/SHILEIHUAJI/mobile-assets@main/wallpapers/vivo/wp1.jpg
```

---

# 📋 assets.json 示例

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

字段说明：

```text
count  当前资源数量
files  当前资源列表
```

---

# ✅ 通用调用代码

可直接复制到任何前端项目。

```js
const CDN =
'https://cdn.jsdelivr.net/gh/SHILEIHUAJI/mobile-assets@main';

const INDEX =
`${CDN}/assets.json`;

let assetsCache = null;

async function getAssets(){

    if(assetsCache)
        return assetsCache;

    assetsCache =
        await fetch(
            INDEX,
            {
                cache:'no-cache'
            }
        ).then(r=>r.json());

    return assetsCache;
}

async function getRandomAsset(type){

    const data =
        await getAssets();

    const files =
        data[type]?.files || [];

    if(!files.length)
        return null;

    const file =
        files[
            Math.floor(
                Math.random()*files.length
            )
        ];

    return `${CDN}/${type}/${file}`;
}
```

---

# 🖼️ 随机壁纸

```js
async function getRandomWallpaper(){

    return await getRandomAsset(
        'wallpapers'
    );

}
```

使用：

```js
const url =
await getRandomWallpaper();

console.log(url);
```

返回示例：

```text
https://cdn.jsdelivr.net/gh/SHILEIHUAJI/mobile-assets@main/wallpapers/vivo/wp8.jpg
```

---

# 🔄 随机壁纸（避免连续重复）

```js
const CDN =
'https://cdn.jsdelivr.net/gh/SHILEIHUAJI/mobile-assets@main';

const INDEX =
`${CDN}/assets.json`;

let assetsCache = null;
let currentWallpaper = '';

async function getAssets(){

    if(assetsCache)
        return assetsCache;

    assetsCache =
        await fetch(
            INDEX,
            {
                cache:'no-cache'
            }
        ).then(r=>r.json());

    return assetsCache;
}

async function getRandomWallpaper(){

    const data =
        await getAssets();

    const files =
        data.wallpapers.files;

    if(!files.length)
        return null;

    let next;

    do{

        next =
            files[
                Math.floor(
                    Math.random()*files.length
                )
            ];

    }while(
        files.length > 1 &&
        next === currentWallpaper
    );

    currentWallpaper = next;

    return `${CDN}/wallpapers/${next}`;
}
```

---

# ⏰ 自动更换壁纸

每10分钟自动切换一次。

```js
async function applyWallpaper(){

    try{

        const url =
            await getRandomWallpaper();

        document.body.style.backgroundImage =
            `url("${url}")`;

    }catch(err){

        console.error(err);

    }

}

applyWallpaper();

setInterval(
    applyWallpaper,
    10 * 60 * 1000
);
```

---

# 🎨 指定背景容器

如果页面存在：

```html
<div id="wall"></div>
```

使用：

```js
async function applyWallpaper(){

    try{

        const url =
            await getRandomWallpaper();

        const wall =
            document.getElementById(
                'wall'
            );

        wall.style.backgroundImage =
            `url("${url}")`;

    }catch(err){

        console.error(err);

    }

}
```

---

# 📂 指定分类随机

仓库结构：

```text
wallpapers/
├── vivo
├── xiaomi
├── anime
├── nature
└── game
```

调用：

```js
async function getRandomWallpaper(category){

    const data =
        await getAssets();

    let files =
        data.wallpapers.files;

    if(category){

        files =
            files.filter(
                x=>x.startsWith(
                    category + '/'
                )
            );

    }

    if(!files.length)
        return null;

    const file =
        files[
            Math.floor(
                Math.random()*files.length
            )
        ];

    return `${CDN}/wallpapers/${file}`;
}
```

全部随机：

```js
await getRandomWallpaper();
```

只随机 vivo 分类：

```js
await getRandomWallpaper('vivo');
```

---

# 🤖 自动索引

仓库资源索引由 GitHub Actions 自动生成。

流程：

```text
上传资源
    ↓
GitHub Actions
    ↓
自动生成 assets.json
    ↓
自动提交更新
```

新增资源后无需修改代码。

---

# 📌 适用场景

```text
个人主页
导航页
音乐站
PWA
启动页
浏览器主页
WebView项目
展示页
实验项目
```

本仓库为通用静态资源仓库，可供多个项目共享使用。
