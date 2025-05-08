import pandas as pd
import requests
import time

# 定义Silicon API的请求函数
def ask_silicon(question):
    url = "https://api.siliconflow.cn/v1/chat/completions"
    payload = {
        "model": "Pro/deepseek-ai/DeepSeek-V3",
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "stream": False,
        "max_tokens": 1000,
        "stop": ["null"],
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "response_format": {"type": "text"},
    
    }
    headers = {
        "Authorization": "Bearer sk-vvdcfuscekqgyfnomfzpjbvoovipmhflygqlcitumbjgczpq",
        "Content-Type": "application/json"
    }
    
    response = requests.request("POST", url, json=payload, headers=headers)
    try:
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error: {e}")
        return "N/A"

def main():
    start_time = time.perf_counter_ns()

    # 读取Excel
    df = pd.read_excel("question.xlsx", engine='openpyxl')

    # 遍历每个问题
    for index, row in df.iterrows():
        if pd.isnull(row['answers']):  # 仅处理未回答的问题
            question = row['questions']
            answer = ask_silicon(question)
            df.at[index, 'answers'] = answer
            time.sleep(1)  # 控制API调用频率
            
            # 实时保存（可选）
            df.to_excel("questions_processed.xlsx", index=False)

    end_time = time.perf_counter_ns()
    elapsed_time = end_time - start_time
    print(f"处理完成！总耗时: {elapsed_time} 纳秒")

    # 保存运行时间到日志文件
    with open("D:/Desktop/using LLM to data extract/log/runtime_log.txt", "a") as log_file:
        log_file.write(f"处理完成！总耗时: {elapsed_time} 纳秒\n")

if __name__ == "__main__":
    main()