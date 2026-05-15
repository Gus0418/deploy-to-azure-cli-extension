# Web Artifact 建構器

建立可在瀏覽器直接運行的單一 HTML Artifact，支援 React 18 + TypeScript + Tailwind + shadcn/ui。

## 使用方式

```
/artifact [描述你想要的介面或功能]
```

範例：
- `/artifact 建立一個 todo list app，支援新增/刪除/標記完成`
- `/artifact 設計一個儀表板，顯示虛擬銷售數據圖表`
- `/artifact 做一個互動式倒數計時器，可自訂時間`

## 技術棧

- **框架**：React 18 + TypeScript
- **樣式**：Tailwind CSS
- **元件**：shadcn/ui（Button、Card、Input、Dialog 等）
- **圖表**：Recharts（若需要數據視覺化）
- **打包**：單一自包含 HTML 檔案（CDN 引入，無需 node_modules）

## 輸出格式

產出一個完整的 `artifact.html` 檔案，包含：
1. 所有依賴從 CDN 引入（unpkg / esm.sh）
2. React 元件用 Babel standalone 轉譯
3. Tailwind 從 CDN Play 引入
4. 可直接雙擊用瀏覽器開啟，無需任何建置步驟

## 設計原則

- 避免：過多置中排版、紫色漸層、千篇一律的圓角、預設 Inter 字體
- 要有視覺個性，不要 AI 制式感
- 互動體驗流暢，狀態管理清晰
- 行動裝置友善（RWD）

## 執行步驟

1. 理解用戶需求，確認功能範圍
2. 規劃元件結構與狀態設計
3. 實作完整的 HTML Artifact（一次輸出完整檔案）
4. 驗證所有 CDN 連結可用
5. 說明如何在瀏覽器開啟和使用
