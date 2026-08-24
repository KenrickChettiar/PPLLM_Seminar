#Get the scoring prompts and pass to judges
import json

import judgeQwenmodel

with open("scoringpromptsbaseLlama.json","r") as f:
    prompts = json.load(f)

#pass to qwen or Gemma

judgeQwenmodel.judgeQwen(prompts,"BaseLlamatojudgeQwen")

with open("BaseLlamatojudgeQwen.json","r") as f:
    all_scores = json.load(f)

scores = all_scores

# for e in all_scores:
#     scores.append(list(e.values())[0][15])

scores_int = list(map(int, scores))

average_of_scores = sum(scores_int)/len(scores_int)

with open("/home/ppllm26_team000/Seminar/results/10pointscoring/Llama.txt","a") as f:
    f.write(f"The average score of Llama responses with Qwen as judge is {average_of_scores} and the list is {scores_int}")
