# Traffic Data Analytics Data Warehouse

## Overview

This collaborative project addresses the imperative need for enhanced traffic data analytics within the city traffic department. The successful establishment of a scalable data warehouse, tailored for the deployment of swarm UAVs and static roadside cameras, marks a significant stride in improving traffic flow. Operating within the Extract Load Transform (ELT) framework, powered by the Data Build Tool (DBT), our data warehouse serves as a robust repository for efficiently managing and querying vehicle trajectory data from diverse city locations.

This initiative not only achieves the immediate goal of traffic management but also lays the foundation for undisclosed projects. The adaptability through on-demand transformation workflows for analytic engineers underscores our commitment to advancing data-driven solutions.

## Table of Contents

- [Traffic Data Analytics Data Warehouse](#traffic-data-analytics-data-warehouse)
  - [Overview](#overview)
  - [What's Included](#whats-included)
  - [Installation](#installation)
  - [Getting Started](#getting-started)
  - [Data Sources](#data-sources)
  - [Data Generation](#data-generation)
  - [Screenshots](#screenshots)
  - [Contributions](#contributions)
  - [License](#license)

## What's Included

- Airflow DAGs
- Apache Airflow, dbt, redash, and a Data Warehouse
- ELT techniques for Data Warehouse
- Data pipelines and orchestration workflows

## Installation

1. **Clone this Repository:**

    Clone this repository:
    ```bash 
    git clone https://github.com/AbelBekele/10-Academy-Week-2.git
    ```

    Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. **Set Up Python Environment:**

    ```bash
    python -m venv your_env_name
    ```

    Replace `your_env_name` with the desired name for your environment.
    
    **Activate the Environment:**

    - On Windows:

    ```bash
    .\your_env_name\scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source your_env_name/bin/activate
    ```

## Getting Started

Explore the repository to understand the project structure and components. Refer to the [Installation](#installation) section for setup instructions. Detailed documentation for each component is available within their respective folders.

## Data Sources

The project relies on data from the following sources:

- [Download Site](https://open-traffic.epfl.ch/index.php/downloads/#1599047632450-ebe509c8-1330)
- [Records](https://zenodo.org/records/7426506)

## Data Generation

Understand how the data is generated:

- [PIA15 Poster (datafromsky.com)](https://datafromsky.com/wp-content/uploads/2015/03/PIA15_poster.pdf)
- [(PDF) Automatic Vehicle Trajectory Extraction (researchgate.net)](https://www.researchgate.net/publication/276857533_Automatic_vehicle_trajectory_extraction_for_traffic_analysis_from_aerial_video_data)

## Screenshots

Navigate to the `screenshots` folder to view visual representations of the project.

## Contributions

We welcome contributions to this repository. Please submit pull requests with improvements to code, documentation, or visualizations. Refer to the [Contribution Guidelines](CONTRIBUTING.md) for details.

## License

This repository is licensed under the [MIT License](LICENSE).
