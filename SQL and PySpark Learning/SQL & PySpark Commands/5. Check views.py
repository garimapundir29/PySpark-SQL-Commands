# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT * FROM v_race_results
# MAGIC -- Showing error because we are trying to access the temp view in another notebook.
# MAGIC -- We can also access the global temp view outside any notebook otherwise it will pop us error.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC   FROM global_temp.gv_race_results;