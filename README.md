# 實時音頻處理項目

這個項目演示了如何使用 PyTorch 神經網絡進行實時音頻處理和播放。

## 安裝

1. 克隆此存儲庫
2. 安裝依賴項：`pip install -r requirements.txt`

## 使用方法

1. 生成測試音頻：
   ```
   python scripts/generate_sin_wave.py
   ```

2. 創建並保存簡單的神經網絡模型：
   ```
   python scripts/train_simple_network.py
   ```

3. 運行主程序進行實時音頻處理和播放：
   ```
   python main.py
   ```

## 文件結構

- `data/`: 存儲音頻文件
- `models/`: 包含神經網絡模型定義
- `utils/`: 包含輔助函數和工具
- `scripts/`: 包含獨立的腳本
- `main.py`: 主程序
- `requirements.txt`: 項目依賴項
- `README.md`: 項目說明文件

## 注意事項

- 確保您的系統已正確設置音頻設備。
- 調整 `main.py` 中的 `BUFFER_MAX_SIZE` 和 `FRAME_DURATION_MS` 可能會影響延遲和音頻質量。