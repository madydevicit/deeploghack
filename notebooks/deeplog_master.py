# Databricks notebook source
# MAGIC %md __Installing dependencies__

# COMMAND ----------

!pip install spellpy
!pip install torch
!pip install boto3

# COMMAND ----------

# MAGIC %cd /Workspace/Repos/mvuribi@gap.com/deeplog/example

# COMMAND ----------

!python preprocess.py

# COMMAND ----------

import pandas as pd

output_dir = '/Workspace/Repos/mvuribi@gap.com/deeplog/example/openstack_result'
df = pd.read_csv(f'{output_dir}/openstack_abnormal.log_structured.csv')
df.display()
list(enumerate(df['EventId']))

# COMMAND ----------

df['EventId'].unique().shape

# COMMAND ----------

!python train.py --num-class 1143 --num-candidates 114 --epochs 35 --window-size 3 --local True

# COMMAND ----------

# MAGIC %ls /Workspace/Repos/mvuribi@gap.com/deeplog/example/model

# COMMAND ----------

!python predict.py --threshold 25

# COMMAND ----------

# MAGIC %md __Appendix__

# COMMAND ----------

# import sys
# sys.path.append('/content/deeplog')

# import os
# cwd = os.getcwd()    
# print(cwd)
