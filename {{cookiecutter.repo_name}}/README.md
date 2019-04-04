# {{ cookiecutter.project_name }}
{{ cookiecutter.project_short_description }}


Directory Structure
--------------------
    .
    ├── AUTHORS.md
    ├── LICENSE
    ├── README.md
    ├── models  <- compiled model .pkl or HDFS or .pb format
    ├── config  <- any configuration files
    ├── data
    	├── interim <- data in intermediate processing stage
    │   ├── interim <- data in intermediate processing stage
    │   ├── processed <- data after all preprocessing has been done
    │   └── raw <- original unmodified data acting as source of truth and provenance
    ├── docs  <- usage documentation or reference papers
    ├── notebooks <- jupyter notebooks for exploratory analysis and explanation 
    ├── reports <- generated project artefacts eg. visualisations or tables
    │   └── figures
    └── src
        ├── data <- scripts for processing data eg. transformations, dataset merges etc. 
        ├── models <- scripts for generating models 
        ├── tools <- additional tools
   		├── visualization <- for visualization
    |--- environment.yml <- file with libraries and library versions for recreating the analysis environment
    |--- Makefile
   
