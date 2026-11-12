# Ollama model comparison

A Python script that sends the same prompt to three local models with Ollama and saves the answers in `results.csv`.

## Models
- qwen2.5:0.5b
- gemma3:1b
- llama3.2:1b

I picked these because they are small and run fine on my laptop.

Laptop: MacBook Air, Apple M4, 16 GB RAM

## How to run
1. Install Ollama from https://ollama.com and pull the models:
   ollama pull qwen2.5:0.5b
   ollama pull gemma3:1b
   ollama pull llama3.2:1b
2. Install the Python library: pip install ollama
3. Run: python3 compare_models.py

## Prompt
"A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost? Answer briefly and explain your reasoning."

The right answer is $0.05.

## Results (second run, saved in results.csv)
| Model | Answer | Correct? | Time |
|---|---|---|---|
| qwen2.5:0.5b | $0.90 | No | 3.68 s |
| gemma3:1b | $0.05 | Yes | 2.29 s |
| llama3.2:1b | $0.05 | Yes | 2.21 s |

## Observations
- I ran the script twice. The first time all three models got the right answer ($0.05). The second time qwen2.5 said $0.90, which is wrong. It wrote a wrong equation at the start and then kept going even though the math didn't make sense. gemma3 and llama3.2 were correct both times.
- So the same model can give different answers to the same question. The smallest model (qwen2.5, 0.5B) seems the least reliable.
- Speed was fine, around 2-4 seconds per answer. qwen2.5 was slowest this time (3.7 s) because it wrote a much longer (and wrong) answer. In the first run gemma3 and llama3.2 took about 7-8 seconds, because they had to be loaded into memory first.
- This is a famous question, so the models have probably seen it before. A harder or more unusual question would probably show bigger differences.
- I didn't test a commercial model, but I would expect bigger models like ChatGPT to be more reliable than these small ones, especially the 0.5B model. The good thing about the local models is that they are free and run offline on my laptop.
