#!/usr/bin/env python
# coding: utf-8

# # Running ADF Basics
# 
# Now that the environment is setup with the required modules loaded and the ADF cloned let's put it all together and do a CAM vs CAM comparison!

# ### Single Case Comparison
# 
# <p>Revisit (or reopen) your copy of the runtime configure file (ie )</p>
# 
# By default the ADF will run a single test CAM simulation (experiment) case vs baseline (control) case.

# ##### Available Comparison Cases
# 
# There are essentially 3 types of comparisons:
# 
# * CAM vs CAM
# * CAM vs Observations/Reanalysis
# * CAM vs CMIP
# 
# And each have their own requirements for the run-time config file (eg `config_cam_baseline_example`)

# 
