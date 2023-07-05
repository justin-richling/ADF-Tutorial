#!/usr/bin/env python
# coding: utf-8

# ## ADF Basics

# ### ADF Flow
# 
# A simple look at the flow of the ADF

#  - Create time series files from monthly history files (if they don’t exist or are being overwritten)
#  - Create climatology files from either ADF generated or pre-existing time series files (ie CMIP)
#  - Regrid Test case from Baseline case and vice-versa from climatology files
#  - Run Analysis scripts
#  - Run Plotting scripts
#  - Generate Website pages
# 
# 
# ** Most parts of the ADF are optional and can be turned off for your desired need:
#            Potential Examples:
#            
# If you only want regridded data, turn off plotting, analysis, website parts
#     
# If you want plotting and only need a few plot images, you can turn off the website part
#     
# If you only want time series files, you can turn off all other parts
#     
# If you don’t care about the statistics (AMWG) tables, turn off analysis part
#     
# etc.
# 
# 

# ### ADF Setup
# 
# A simple look at the flow of the ADF

# ```
# 0. Run CAM simulation          get history ( h0* ) file(s) 
#            *or other history files
#                                    
# 1. Configure yaml file(s) for the history files
# 
# 	NOTE:  Make copies of these files and modify/customize the copies!
# 
#     config_cam_baseline_example.yaml  (necessary, must change!)
# 
#     lib/adf_variable_defaults.yaml   (necessary, but optional to change)**
# 
#      - Additionally, you will need to change the defaults_file path in your copy of config_cam_baseline_example.yaml file
# 
# 
# 2. Run the ADF
# <p>Errors?  Check config files   Check error/logs   Check data/paths</p>
# <p>Success: Check output data/images</p>
# <p>Locally</p>
# <p>Via HTML files  (optional)</p>
# ```

# In[ ]:




