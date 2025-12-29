from pathlib import Path
import pandas as pd
import json
import re  # 新增：用于提取非数字部分

# 路径设置
data_dir = Path(__file__).absolute().parent.parent / "data" / "beidong_v0.5_output_csv"
file_paths = list(data_dir.glob("*.csv"))

# 用字典收集，每个 key 是 uttid 的非数字部分（忽略数字）
missing_groups = {}

for file_path in file_paths:
    df = pd.read_csv(file_path)

    for _, row in df.iterrows():
        uttid = str(row["uttid"]).strip()  # 确保是字符串
        # 提取非数字部分作为 key：移除所有数字，保留其他字符
        key_no_digits = re.sub(r'\d+', '', uttid)  # 替换所有数字为空字符串

        text_raw = row["text"]
        asr_raw = row["asr_result"]

        # 分割并清理 text 段落
        segments = [t.strip() for t in text_raw.split("｜") if t.strip()]

        try:
            asr_list = json.loads(asr_raw)
            asr_texts = {item["asr_result"].strip() for item in asr_list}
        except Exception as e:
            asr_texts = set()
            print(f"JSON 解析失败: {uttid} → {asr_raw[:100]}... 错误: {e}")

        # 找出这个 uttid 缺失的文本
        missing_texts = [seg for seg in segments if seg not in asr_texts]

        # 如果有缺失，且这个 key 还没记录过
        if missing_texts:
            if key_no_digits not in missing_groups:
                missing_groups[key_no_digits] = {
                    "group_key": key_no_digits,
                    "example_uttid": uttid,                    # 展示一个代表性的完整 uttid
                    "missing_texts": missing_texts,            # 所有缺失（取第一个发现的）
                    "missing_count": len(missing_texts),
                    "total_segments": len(segments),
                    "asr_result_raw_example": asr_raw,         # 第一个遇到的 asr
                }
            else:
                # 如果这个组已经记录过，可以选择不追加（保持唯一），或合并更多缺失
                # 这里保持保守：只记录第一次发现的缺失内容
                pass

# 转为 DataFrame
results = list(missing_groups.values())

if results:
    result_df = pd.DataFrame(results)
    # 按 group_key 排序
    result_df = result_df.sort_values("group_key").reset_index(drop=True)
    
    print(f"共发现 {len(results)} 个 uttid 组（忽略数字） 有文本缺失")
    print(result_df[["group_key", "example_uttid", "missing_count", "missing_texts"]])
    
    # 保存结果
    output_path = Path(__file__).absolute().parent.parent / "data" / "missing_uttid_no_digits_groups.csv"
    result_df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"结果已保存到: {output_path}")
else:
    print("没有发现任何 uttid 有文本缺失")