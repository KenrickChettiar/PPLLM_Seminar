#Get the scoring prompts and pass to judges
import json
import judgeLlama3model

with open("scoringpromptsbaseQwen.json","r") as f:
    prompts = json.load(f)

#pass to Llama3 or Gemma

judgeLlama3model.judgeLlama3(prompts,"BaseQwentojudgeLlama3")

with open("BaseQwentojudgeLlama3.json","r") as f:
    all_scores = json.load(f)

scores = all_scores

# for e in all_scores:
#     scores.append(list(e.values())[0])


scores_int = list(map(int, scores))

average_of_scores = sum(scores_int)/len(scores_int)

with open("/home/ppllm26_team000/Seminar/results/10pointscoring/Qwen.txt","a+") as f:
    f.write(f"The average score of Qwen responses with Llama as judge is {average_of_scores}\n")
