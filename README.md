A general setup which can be used for the baby-lm project found here: https://babylm.github.io/index.html

General information
- Do not attempt to upload the babylm dataset, instead, copy it from the paper onto your machine/cloud system from the following URL: https://github.com/babylm/babylm.github.io/raw/main/babylm_data.zip
- Keep all datasets inside of the 'dataset' directory

The general structure:
- Clone this repo
- Clone the evaluation pipeline repo somewhere else (https://github.com/babylm/evaluation-pipeline)
- Using a python venv, install the necessary packages for creating our model
- Train a model on the data
- Save the model and the model tokenizer
- Using a python venv, run the evaluation pipeline on the data
