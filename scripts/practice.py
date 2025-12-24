import json
from pathlib import Path

data = [
    {
        "session_id":123,
        "video_info" : [
            {
                "name":"fFjv93ACGo8.mp4",
                "fps":29.97002997002997,
                "resolution": [1280, 720],
                "frame_index": [0,5,10], # 遍历视频所有的帧，抽取这些帧数到datacard
                "duration": 74.327075,
                "subtitle":[],
                "meta":"string"
            },
            {
                "name":"HwnB8aCn8yE.mp4",
                "fps":25.0,
                "resolution": [1280, 720],
                "frame_index": [0,5,10],
                "duration": 74.327075,
                "subtitle":["subtitle_of_frame_0", "ubtitle_of_frame_5", "ubtitle_of_frame_10"], # 每一帧对应的字幕信息
                "meta":"string"
            }
        ],
        "content" : [
                # 中间层：表示轮次，有两轮则list长度为2
                {
                    "role":"system",
                    "text":"你是一个问答机器人"
                },
                {
                    # 按照video和image list中的顺序，插入到prompt
                    "text": "看完这个视频<video_token_1>，在这张图片里找到答案<image_token_1>，再看这个视频<video_token_1>，结合这个图片给出分析<image_token_1>,最后听个音频<audio_token_1>",
                    "question_id": "001-1", #是否需要
                    "role": "user",
                    "type": "text",
                    "video": [
                        # 最内层：表示视频数量，比如一个问题要参考多个视频回答
                        "fFjv93ACGo8.mp4", # 对应video_info中的name
                        "HwnB8aCn8yE.mp4"
                    ],
                    "image": [
                        "image_1.jpg",
                        "image_2.jpg"
                    ],
                    "audio": [
                        "audio_1.wav"
                    ],
                    "question_type": "open",
                    "answer": "<think>我需要分析这个视频的内容</think> 这个视频真好看 <image_token_2>",
                    "option": [],
                    "extra_info": "" # 题目级别extra_info，写入datacard prompt字段中
                },
            ],
        "extra_info" : "", # session 粒度extra_info，写入datacard extra_info字段
        "tags": ["math"] # 自定义的额外字段
    }
]

SCRIPT_PATH = Path(__file__).resolve()

FILE_PATH = SCRIPT_PATH.parent.parent / "data" / "raw_data.json"

FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

with open(FILE_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
