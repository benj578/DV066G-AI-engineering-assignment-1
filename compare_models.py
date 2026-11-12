import ollama
import csv
import time

models = ["qwen2.5:0.5b", "gemma3:1b", "llama3.2:1b"]
prompt = "A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost? Answer briefly and explain your reasoning."

with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["model", "prompt", "response", "seconds"])

    for model in models:
        print("Asking", model, "...")
        start = time.time()
        response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
        seconds = round(time.time() - start, 2)

        answer = response["message"]["content"]
        print(answer)
        print("Time:", seconds, "seconds\n")

        writer.writerow([model, prompt, answer, seconds])

print("Done! Results saved in results.csv")