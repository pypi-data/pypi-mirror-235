# **aimped**
![aimped](https://dev.aimped.ai/static/media/AimpedBirdLogo.0b3c7cc26d31afe7bd73db496acb01d1.svg)

**Aimped is a unique python library that provides classes and functions for only exclusively business-tailored AI-based NLP models.**   
In this version, we provide the following features:
Sound processing tools and functions, NLP tools and functions, and a pipeline class for NLP tasks. 

# Installation  
```python
pip install aimped
```

# Usage  
```python  
import aimped
print(aimped.__version__)
```
## Examples  

### Example 1

```python  
from aimped import nlp

result = nlp.sentence_tokenizer("Hi, welcome to aimped. Explore ai models.",language="english")
print(result)
# ['Hi, welcome to aimped.', 'Explore ai models.']
```

### Example 2
```python  
from aimped.sound.utils import get_audio_duration

duration = get_audio_duration(audio_path="/path/to/audio_file")
print(duration)

```

### Example 3
```python  
from aimped.nlp.pipeline import Pipeline

pipe = Pipeline(model=model, tokenizer=tokenizer, device='cpu')
result = pipe.ner_result(
                        text=text,
                        sents_tokens_list=sents_tokens_list,
                        sentences=sentences)
print(result)
```

### Example 4
```python  
from aimped.nlp.pipeline import Pipeline
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from aimped.nlp import translation

checkpoint = "/path/to/model_checkpoint"
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
device = 0
aimped = Pipeline(model=model, tokenizer=tokenizer, device=device)
aimped.translation_result(["text1_de","text2_de",...],source_language="german", output_language="english")
```
