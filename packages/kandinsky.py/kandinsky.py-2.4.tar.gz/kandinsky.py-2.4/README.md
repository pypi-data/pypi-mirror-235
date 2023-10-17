# kandinsky.py
Reverse Engineered fusion-brain API

### Installation 
```
pip install kandinsky.py
```



### Example of usage
```python
from kandinsky import Kandinsky

pipe = Kandinsky(auth_token='your-authorization-token-from-headers')

job = pipe.create(prompt="cat")
result = pipe.wait(job) #b64 string
image = pipe.load(result) #BytesIO object
```


