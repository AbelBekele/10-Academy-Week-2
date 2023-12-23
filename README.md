# Data Engineering: Data warehouse tech stack with MySQL/PostgreSQL, DBT, Airflow

## Overview

In response to the city traffic department's imperative for enhanced traffic data analytics, our collaborative efforts have resulted in the successful establishment of a scalable data warehouse tailored for the deployment of swarm UAVs and static roadside cameras. 

Operating within the Extract Load Transform (ELT) framework, powered by the Data Build Tool (DBT), the data warehouse serves as a robust repository for efficiently managing and querying vehicle trajectory data from diverse city locations. This strategic initiative not only addresses the immediate goal of improving traffic flow but also lays the foundation for undisclosed projects, offering adaptability through on-demand transformation workflows for analytic engineers within the city traffic department. The project underscores our commitment to advancing data-driven solutions and fortifying the city's traffic management capabilities.

## Table of Contents
- [Project Title](#data-engineering-data-warehouse-tech-stack-with-mysqlpostgresql-dbt-airflow)
  - [Overview](#overview)
  - [What this repository includes](#what-this-repository-includes)
  - [Installation](#installation)
  - [Getting started](#getting-started)
  - [Screenshots](#screenshots)
  - [Contributions](#contributions)
  - [License](#license)


## What this repository includes:

- Airflow DAGs
- Apache Airflow, dbt, redash  and a DWH
- ELT techniques to DWH
- Data pipelines and orchestration workflows

## Installation


1. **Clone this package**

    Clone this repository:
    ```bash 
    git clone https://github.com/AbelBekele/10-Academy-Week-2.git
    ```

    Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. **Python Environment:**
    ```bash
    python -m venv your_env_name
    ```

    Replace `your_env_name` with the desired name for your environment.
    
    **Activate the environment:**

    - On Windows:

    ```bash
    .\your_env_name\scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source your_env_name/bin/activate
    ```

## Where to find the datas?

- [Download site](https://open-traffic.epfl.ch/index.php/downloads/#1599047632450-ebe509c8-1330)
- [Records](https://zenodo.org/records/7426506)


## Understand how the data is generated

- [PIA15_poster.pdf (datafromsky.com)](https://datafromsky.com/wp-content/uploads/2015/03/PIA15_poster.pdf)
- [(PDF) Automatic vehicle trajectory extraction for traffic analysis from aerial video data (researchgate.net)](https://www.researchgate.net/publication/276857533_Automatic_vehicle_trajectory_extraction_for_traffic_analysis_from_aerial_video_data)

## Screenshots

- Navigate to screenshots folder to analyize all the 

## Contributions:

We welcome contributions to this repository. Please feel free to submit pull requests with improvements to the code, documentation, or visualizations.

## License:

This repository is licensed under the MIT license.