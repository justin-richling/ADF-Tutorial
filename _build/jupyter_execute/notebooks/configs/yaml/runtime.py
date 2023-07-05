#!/usr/bin/env python
# coding: utf-8

# # config_cam_example.yaml
# 
# Please refer back to the ADF Reference page for more info on these variables and for other optional variables
# 
# ```{Warning}
# Note:  Please do not modify this file.
#              
# It is recommended to make a copy of this file, make modifications in that copy, and then point the ADF to it in <a href="https://justin-richling.github.io/ADF-Tutorial/notebooks/configs/yaml/runtime.html#defaults-file"><code class="docutils literal notranslate"><span class="pre">your_config_cam.yaml</span></code> (copy of config_cam_example.yaml)</a>.
# 
# Example:
# 
# From the ADF root directory
# 
#     cp config_cam_example.yaml config_adf_tutorial.yaml
# 
# ```
You will need to open the your custom config runtime yaml file (config_adf_tutorial.yaml) with your favorite editor
# ##
# ###

# 
# ##### diag_basic_info
# 
# <h6>Edit the following variables</h6>
# 
# <p style="margin-top: -5px;">&ensp; compare_obs: <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
# <p style="margin-top: -5px;">&ensp; cam_regrid_loc: <code class="docutils literal notranslate"><span class="pre">/glade/scratch/${user}/ADF/regrid</span></code></p>
# <p style="margin-top: -5px;">&ensp; cam_diag_plot_loc: <code class="docutils literal notranslate"><span class="pre">/glade/scratch/${user}/ADF/plots</span></code></p>
# <p style="margin-top: -5px;">&ensp; use_defaults: <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
# 
# ##### diag_cam_climo
# 
# <h6>Edit the following variables</h6>
# 
# <p style="margin-top: -5px;">&ensp; cam_case_name: <code class="docutils literal notranslate"><span class="pre">f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
# <p style="margin-top: -5px;">&ensp; cam_hist_loc: <code class="docutils literal notranslate"><span class="pre">/glade/scratch/richling/ADF/tutorials/data/f.cam6_3_106.FLTHIST_v0a.ne30.dcs_effgw_rdg.001</span></code></p>
# <p style="margin-top: -5px;">&ensp; cam_climo_loc: <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
# <p style="margin-top: -5px;">&ensp; start_year: <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
# <p style="margin-top: -5px;">&ensp; end_year: <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
# <p style="margin-top: -5px;">&ensp; cam_ts_loc: <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
# 
# ##### diag_cam_baseline_climo
# 
# <h6>Edit the following variables</h6>
# 
# <p style="margin-top: -5px;">&ensp; cam_case_name: <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
# <p style="margin-top: -5px;">&ensp; cam_hist_loc: <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
# <p style="margin-top: -5px;">&ensp; cam_climo_loc: <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
# <p style="margin-top: -5px;">&ensp; start_year: <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
# <p style="margin-top: -5px;">&ensp; end_year: <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
# <p style="margin-top: -5px;">&ensp; cam_ts_loc: <code class="docutils literal notranslate"><span class="pre">false</span></code></p>

# In[ ]:





# In[ ]:




# Single Case Comparison
# ## Diagnostic Scripts "Subsections"
# 
# <p>Each of the following sets are also considered subsections. These are all components of the actual diagnostics workflow of the ADF.</p>
## $\color{#117284}{\textit{time_averaging_scripts}}$

# ## time_averaging_scripts

# This section allows for any time averaging scripts
# 
# * Must be located in scripts/averaging!
# 
#       - scripts/averaging/create_climo_files.py
# 
## $\color{#117284}{\textit{regridding_scripts}}$

# ## regridding_scripts

# This section allows for any regridding scripts
# 
# * Must be located in scripts/regridding!
# 
#       - scripts/regridding /regrid_and_vert_interp.py
# 
## $\color{#117284}{\textit{analysis_scripts}}$

# ## analysis_scripts

# This section allows for a broad spectra of data analysis scripts
# 
# * Must be located in scripts/analysis!
#     
#       - scripts/analysis/amwg_table.py
#       
#       Possible addition examples:
#       - scripts/analysis/amwg_chem_table.py
#       - scripts/analysis/amwg_aerosol_table.py
# 
## $\color{#117284}{\textit{plotting_scripts}}$

# ## plotting_scripts

# Set of plotting scripts, both ADF default as well as any custom scripts
# 
# * Must be located in scripts/plotting!
# 
#      - scripts/averaging/cam_taylor_diagram.py
#      - scripts/averaging/global_latlon_map.py
#      - scripts/averaging/…
# 
#      Possible addition examples:
#      - scripts/averaging/tem.py
#      - scripts/averaging/time_series.py
# 
## $\color{#117284}{\textit{diag_var_list}}$

# ## diag_var_list

# List of variables to be executed in the ADF
# 
## $\color{#117284}{\textit{region_multicase}}$

# ## region_multicase

# ---

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
