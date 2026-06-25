# zeki
This repository contains supplemental code for the following paper:

> Sheikh Muhammad Farjad and Robin Gandhi. 2025.  
> **Zeki: A Containerized Pipeline for Deep Learning Deployment for Edge-based Structural Health Monitoring.**  
> In *Proceedings of the 12th ACM International Conference on Systems for Energy-Efficient Buildings, Cities, and Transportation*  
> (BuildSys '25). Association for Computing Machinery, New York, NY, USA, 456–460.  
> https://doi.org/10.1145/3736425.3772357

Please refer to the paper for a detailed description of the dataset, code, execution pipeline, and insights derived from this repository.

## Repository Structure

The directory names in this repository are intentionally kept the same as those used by the programs. Please do not rename or restructure the directories unless the corresponding program paths are updated accordingly.

Each experiment directory contains the scripts and folders required to execute that version of the deployment pipeline, including:

- `edgeOps.sh` — shell script for edge execution workflow
- `inference.py` — inference script
- `monitor.py` — monitoring script
- `models/` — directory for the corresponding model files
- `Images100/` — contains 100 images used for the classification task. These images are licensed under the [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/) and are attributed to Özgenel, Çağlar Fırat (2019), “Concrete Crack Images for Classification”, Mendeley Data, v2
http://dx.doi.org/10.17632/5y9wdsg2zt.2.
- `mem_record_cnn-bb.txt` and `new_folder` — recorded monitoring data (example data - For detailed data for each platform, please email: **sfarjad@unomaha.edu**)

## Models
The trained models are not included directly in this repository.

To obtain the trained models, please contact: **sfarjad@unomaha.edu**

A custom cloud storage link will be provided for downloading the required models.

The 100-image dataset is included in this repository under the corresponding `Images100/` directories.

Before running the programs, place each downloaded model into its appropriate models/ directory. Each experiment directory should contain the following folders:
```text
models/
Images100/
```

Please ensure that the required model files are placed in the correct `models/` directory before executing the scripts.

## Setup
Install the required Python dependencies using: `pip install -r requirements.txt`

## Running the Programs
After placing the required models and image datasets in their corresponding directories, navigate to the desired experiment directory and run the provided script.

Example:
```bash
cd buildsys1-lite
bash edgeOps.sh
```

Repeat the same process for other experiment directories as needed.

## Relationship to edgeOps
The `edgeOps.sh` script and edge execution workflow are related to the edgeOps deployment workflow.

If you use, modify, or extend this repository, please also refer to the edgeOps paper and/or repository where appropriate:

- **edgeOps repository:** https://github.com/smfarjad/edgeOps

- **edgeOps paper:** https://doi.org/10.1145/3696673.3723074



## Citation
Sheikh Muhammad Farjad and Robin Gandhi. 2025. Zeki: A Containerized Pipeline for Deep Learning Deployment for Edge-based Structural Health Monitoring. In Proceedings of the 12th ACM International Conference on Systems for Energy-Efficient Buildings, Cities, and Transportation (BuildSys '25). Association for Computing Machinery, New York, NY, USA, 456–460. https://doi.org/10.1145/3736425.3772357

Or, BibTex:

```bibtex
@inproceedings{10.1145/3736425.3772357,
author = {Farjad, Sheikh Muhammad and Gandhi, Robin},
title = {Zeki: A Containerized Pipeline for Deep Learning Deployment for Edge-based Structural Health Monitoring},
year = {2025},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3736425.3772357},
doi = {10.1145/3736425.3772357},
booktitle = {Proceedings of the 12th ACM International Conference on Systems for Energy-Efficient Buildings, Cities, and Transportation},
pages = {456–460},
location = {Golden, CO, USA},
series = {BuildSys '25}
}
```
