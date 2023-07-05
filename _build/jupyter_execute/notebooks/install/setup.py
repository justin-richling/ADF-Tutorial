#!/usr/bin/env python
# coding: utf-8

# # Setting up ADF
# 
# Instructions on how to build the necessary environment for running the ADF.
# 
# Setting up the environment and getting the ADF will be done in the command line and with `git/GitHub`, this tutorial assumes working knowledge of both.
# 
# There are two steps (in this tutorial) to get the ADF up and running on your CISL machine:
#     
# 1) Setting up NCAR's conda environment for all ADF necessary libraries
# 2) Using git to clone the main branch of the ADF
# 
# ```{attention}
# <strong>For this tutorial you must be on a CISL machine</strong>
# 
# There are some instructions for non-CISL machines, but there can be many obstacles. 
# 
# For simplicity, this tutorial will only be geared towards users who have a CISL account and access to CISL machines, ie Casper/Cheyenne and JupyterHub
# ```
# 

# ## Setting up <code class="docutils literal notranslate"><span class="pre">conda</span></code> environment
# 
# If you are unfamiliar with `conda`
# 
# `conda` is a great package manager that allows installing different python packages. Usually, there can be conflicts between certain python packages and even between packages of different versions. To avoid this, `conda` is an industry leading package manager that the ADF will use to avoid any required python packages interfering with the packages you have installed on your machine.
# 
# You don't need to be an expert with `conda` to follow along with this tutorial, but please visit <a href="https://conda.io/projects/conda/en/latest/index.html"><code class="docutils literal notranslate"><span class="pre">conda</span></code>'s website</a> for more information and basics of working with `conda` if you want to read more.
# 
# `````{admonition} Conda cheat sheet for reference
# :class: tip, dropdown
# [conda](conda-cheatsheet.pdf)
# `````
<embed src="../images/conda-cheatsheet.pdf" width="800px" height="2100px" />

# ### CISL Computers
# 
# Setting up the ADF environment if on CISL (Cheyenne/Casper) machines
# 
# * More info can be found in the README on the GitHub: https://github.com/NCAR/ADF#required-software-environment

# ### Loading `modules`
# 
# CISL machines have a cluster of modules that are available to load/unload. Such modules include: conda, nco, python, etc.
# 
# To see a list of the available modules, in a terminal type:
# 
#     module avail
#     
# To see a list of the default modules, type:
# 
#     module --default avail
# 
# ###### Load `conda`
# 
# To make the ADF as flexible as possible, it is recommended that you run in an NCAR precompiled `conda` environment called `npl`
# 
# ---
# 
# <p>First load conda via <code class="docutils literal notranslate"><span class="pre">module</span></code> command</p>
# 
# <div class="highlight-default notranslate"><div class="highlight"><pre id="codecell0"><span></span>module load conda
# </pre><button class="copybtn o-tooltip--left" data-tooltip="Copy" data-clipboard-target="#codecell0">
#       <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-copy" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#000000" fill="none" stroke-linecap="round" stroke-linejoin="round">
#   <title>Copy to clipboard</title>
#   <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
#   <rect x="8" y="8" width="12" height="12" rx="2"></rect>
#   <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"></path>
# </svg>
#     </button></div>
# </div>
# 
# ```{attention}
# You may encounter a <code class="docutils literal notranslate"><span class="pre">module</span></code> <code class="docutils literal notranslate"><span class="pre">load</span></code> error.
# 
# Try unloading the python module: <code class="docutils literal notranslate"><span class="pre">module unload python</span></code> and re-try?
# ```
# 
# 
# ###### Load `nco`
# 
# <p>In addition to conda package, the <code class="docutils literal notranslate"><span class="pre">ncrcat</span></code> NetCDF Operator (NCO) is needed</p>
# 
# <div class="highlight-default notranslate"><div class="highlight"><pre id="codecell0"><span></span>module load nco
# </pre><button class="copybtn o-tooltip--left" data-tooltip="Copy" data-clipboard-target="#codecell0">
#       <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-copy" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#000000" fill="none" stroke-linecap="round" stroke-linejoin="round">
#   <title>Copy to clipboard</title>
#   <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
#   <rect x="8" y="8" width="12" height="12" rx="2"></rect>
#   <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"></path>
# </svg>
#     </button></div>
# </div>
# 
# ###### Load `ncl`
# 
# And if the CVDP is desired, NCL is also needed
# 
# <div class="highlight-default notranslate"><div class="highlight"><pre id="codecell0"><span></span>module load ncl
# </pre><button class="copybtn o-tooltip--left" data-tooltip="Copy" data-clipboard-target="#codecell0">
#       <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-copy" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#000000" fill="none" stroke-linecap="round" stroke-linejoin="round">
#   <title>Copy to clipboard</title>
#   <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
#   <rect x="8" y="8" width="12" height="12" rx="2"></rect>
#   <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"></path>
# </svg>
#     </button></div>
# </div>
# 
# That's it, all done. Wash up and go help with dinner

# <div><p style="font-size: 25px; font-weight: bold; color: #076E85;">Alright here we go</p></div>

# ## Cloning the ADF
# 
# <p style="font-size:16px">It is fairly straight forward to get the ADF. You will need to clone the <a style="color: blue;" href="https://github.com/NCAR/ADF" target="_blank">NCAR/ADF</a> repository to your machine</p>
#     
# <p>Navigate to some where you want to house the ADF root directory. An example would be to put the ADF in your <code class="docutils literal notranslate"><span class="pre">work</span></code> drive on <code class="docutils literal notranslate"><span class="pre">glade</span></code></p>
# 
#     cd /glade/work/{user}
# 
# <p>Next, just a simple <code class="docutils literal notranslate"><span class="pre">git clone</span></code> to copy the ADF to your current location:</p>
# 
# <div class="highlight-default notranslate"><div class="highlight"><pre id="codecell0"><span></span>git clone https://github.com/NCAR/ADF.git
# </pre><button class="copybtn o-tooltip--left" data-tooltip="Copy" data-clipboard-target="#codecell0">
#       <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-copy" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#000000" fill="none" stroke-linecap="round" stroke-linejoin="round">
#   <title>Copy to clipboard</title>
#   <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
#   <rect x="8" y="8" width="12" height="12" rx="2"></rect>
#   <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"></path>
# </svg>
#     </button></div>
# </div>
# 
# 
# <p>This will create a new folder called <strong>ADF</strong> and will be the root directory: <code class="docutils literal notranslate"><span class="pre">/glade/work/{user}/ADF/</span></code>  This will house all the necessary scripts for the ADF to run and where custom scripts would be added if desired!</p>
# 

# 
