
def judgeQwen(all_prompts,file_name):
	from transformers import AutoTokenizer, AutoModelForCausalLM
	import re
	import json

	tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
	model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-3B-Instruct", device_map="auto")


	model_intentions = []

	for i in range (len(all_prompts)):

		messages = [
			{"role": "user", "content": all_prompts[i]},
		]
		inputs = tokenizer.apply_chat_template(
			messages,
			add_generation_prompt=True,
			tokenize=True,
			return_dict=True,
			return_tensors="pt",
		).to(model.device)

		outputs = model.generate(**inputs, max_new_tokens=256)
		resp = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:],skip_special_tokens=True)
		match = re.search(r'"score"\s*:\s*(\d+)', resp)
		score = int(match.group(1))
		model_intentions.append(score)

	with open(f"{file_name}.json","w") as f:
		json.dump(model_intentions,f, ensure_ascii=False, indent=4)