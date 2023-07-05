#!/usr/bin/env python
# coding: utf-8

# # ADF Layout
# 
# A simple look at how the ADF works

# ```
# .
# |-- config_amwg_default_plots.yaml
# |-- config_cam_baseline_example.yaml
# |-- env
# |   `-- conda_environment.yaml
# |-- jupyter_sample.ipynb
# |-- lib
# |   |-- adf_base.py
# |   |-- adf_config.py
# |   |-- adf_diag.py
# |   |-- adf_info.py
# |   |-- adf_obs.py
# |   |-- adf_variable_defaults.yaml
# |   |-- adf_web.py
# |   |-- plotting_functions.py
# |   |-- test
# |   |   |-- pylintrc
# |   |   `-- unit_tests
# |   |       |-- pytest.ini
# |   |       |-- test_adf_base.py
# |   |       |-- test_adf_config.py
# |   |       `-- test_files
# |   |           |-- config_cam_double_nested.yaml
# |   |           |-- config_cam_keywords.yaml
# |   |           `-- config_cam_unset_var.yaml
# |   `-- website_templates
# |       |-- adf_diag.css
# |       |-- NCAR.gif
# |       |-- template.html
# |       |-- template_index.html
# |       |-- template_mean_diag.html
# |       |-- template_mean_tables.html
# |       |-- template_multi_case_index.html
# |       |-- template_table.html
# |       `-- template_var.html
# |-- LICENSE
# |-- README.md
# |-- run_adf_diag
# `-- scripts
#     |-- analysis
#     |   `-- amwg_table.py
#     |-- averaging
#     |   `-- create_climo_files.py
#     |-- plotting
#     |   |-- cam_taylor_diagram.py
#     |   |-- global_latlon_map.py
#     |   |-- global_latlon_vect_map.py
#     |   |-- meridional_mean.py
#     |   |-- polar_map.py
#     |   |-- qbo.py
#     |   |-- regional_map_multicase.py
#     |   `-- zonal_mean.py
#     `-- regridding
#         `-- regrid_and_vert_interp.py
# ```
