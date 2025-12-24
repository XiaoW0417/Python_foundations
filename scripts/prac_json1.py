import json

from pathlib import Path

SCRIPT_FILE = Path(__file__).resolve()
print(SCRIPT_FILE)
SCRIPT_DIR = SCRIPT_FILE.parent.parent
print(SCRIPT_DIR)
file_path = SCRIPT_DIR / "data" / "stu_dict.json"
file_path.parent.mkdir(parents=True, exist_ok=True)

data = {"姓名": "张三", 
        "年龄": 18, 
        "课程列表": [{"名称": "语文", "分数": 90}, 
                    {"名称": "数学", "分数": 86},
                    {"名称": "历史", "分数": 0}
        ]
}

try:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    with open(file_path, "r", encoding="utf-8") as f:
        content = json.load(f)
    courses = content.get("课程列表")
    all_scores = []
    for cour in courses:
        all_scores.append(cour.get("分数", 0))
    
    print(f"0参与平均分计算：平均分{sum(all_scores) / len(all_scores)}")
    no_zero_scores = list(filter(lambda x: x != 0, all_scores))
    print(f"0不参与平均分计算： 平均分{sum(no_zero_scores) / len(no_zero_scores)}")

except Exception as e:
    print(f"Error:{e}")