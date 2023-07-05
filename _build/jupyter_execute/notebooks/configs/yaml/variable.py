#!/usr/bin/env python
# coding: utf-8

# # adf_variable_defaults.yaml
# 
# Location for many plotting, unit, etc defualts for any/all CAM output variables
# 
# ```{Warning}
# Note:  Please do not modify this file unless you plan to push your changes back to the ADF repo.
#              
# If you would like to modify this file for your personal ADF runs then it is recommended to make a copy of this file, make modifications in that copy, and then point the ADF to it using the "defaults_file" config variable in the <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#defaults-file"><code class="docutils literal notranslate"><span class="pre">your_config_cam.yaml</span></code> (copy of config_cam_example.yaml)</a>.
# 
# 
# Example:
# --------
# 
# From the ADF root directory
# 
#     cp lib/adf_variable_defaults.yaml lib/my_variable_defaults.yaml
# 
# ```
# 

# # Configuring Variable Defaults

# ## Variable Default Settings

# ### ADF Default Set
# 
# <p>If you want to use the ADF default values you need to set <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#use-defaults"><code class="docutils literal notranslate"><span class="pre">use_defaults</span></code></a> in your copy of the config_yaml to true
# </p>

# ### Custom Set
# 
# <p>If you plan on using a modified file for your custom values you need to set <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#use-defaults"><code class="docutils literal notranslate"><span class="pre">use_defaults</span></code></a> in your copy of the config_yaml to false and set the path to the custom variable default file with <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#defaults-file"><code class="docutils literal notranslate"><span class="pre">defaults_file</span></code></a>
# </p>
# 
# 
# 
# 
# 
# 

# ```
# U:
#   colormap: "Blues"
#   contour_levels_range: [-10, 90, 5]
#   diff_colormap: "BrBG"
#   diff_contour_range: [-15, 15, 2]
#   scale_factor: 1
#   add_offset: 0
#   new_unit: "ms$^{-1}$"
#   mpl:
#     colorbar:
#       label : "ms$^{-1}$"
#   obs_file: "U_ERA5_monthly_climo_197901-202112.nc"
#   obs_name: "ERA5"
#   obs_var_name: "U"
#   vector_pair: "V"
#   vector_name: "Wind"
#   category: "State"
# ```

# These are the values that can be set for each variable. Non are required.
