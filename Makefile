install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py\
		 hugging-face/zero_shot_classification.py hugging-face/hf_whisper.py

refactor: format lint
