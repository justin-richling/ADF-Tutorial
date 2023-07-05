#!/usr/bin/env python
# coding: utf-8

# # Yaml Config Files
# 
# There are three yaml files included with the ADF

# ###### Run-time yaml config file 
# 
# Configure yaml file for ADF using the history (h0) files
# 
# Two are templates for the runtime config file. Chose one to copy and run with ./run_adf_diag
# 
# ` config_cam_baseline_example.yaml`
# 
# <p style="margin-top: -5px;">&ensp; General default file</p>
# 
# ` config_amwg_default_plots.yaml`
# 
# <p style="margin-top: -5px;">&ensp; This is meant for a subset of commonly used variables and plot types for the AMWG</p>
# 

# In[ ]:





# ###### Variable defaults yaml config file
# 
# Configure yaml file for ADF variables
# 
# And the third is for plotting and observational variable data to be used in the ADF. 
# 
# ` lib/adf_variable_defaults.yaml   (optional)**`
# 
# <p style="margin-top: -5px;">&ensp; This file makes plotting variables more flexible as you can tailor <em>each</em> variable of interst with plotting details and observational dataset information.</p>
# 
# <p style="margin-top: -5px;">&ensp; For examples of ways to setup variable defaults please refer back to the blahblahblah</p>

# In[ ]:




- config_cam_baseline_example.yaml  (necessary)
- lib/adf_variable_defaults.yaml   (optional)**    ** Additionally, you will need to change the [defaults_file](https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#defaults-file) path in your copy of [config_cam_baseline_example.yaml](https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html)
# <h2>YAML File Basics</h2>
# 
# YAML files are a special type of text file, which in our case (using Python) the information in the yaml file will become dictionaries in python scripts.
# 
# Here are a couple hints
# 
# 

# Some paths in the config yaml file are optional and some are **required**

# ### Using variables in the yaml file
# 
# 
# 
# ![Running on Cheyenne Image](../../images/Slide13.png)

# ### Using variables in sub sections
# 
# 
# ![Running on Cheyenne Image](../../images/Slide15.png)

# ```{figure} https://solarsystem.nasa.gov/system/resources/detail_files/2486_stsci-h-p1936a_1800.jpg
# ---
# height: 300px
# name: jupiter-figure
# ---
# The beautiful planet Jupiter! Source: [NASA](https://solarsystem.nasa.gov/resources/2486/hubbles-new-portrait-of-jupiter/?category=planets_jupiter).
# ```

# In[ ]:




