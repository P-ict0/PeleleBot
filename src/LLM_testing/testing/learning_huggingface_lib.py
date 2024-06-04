from transformers import pipeline

classifier = pipeline("sentiment-analysis")
res = classifier("I hate you")[0]
print(res)