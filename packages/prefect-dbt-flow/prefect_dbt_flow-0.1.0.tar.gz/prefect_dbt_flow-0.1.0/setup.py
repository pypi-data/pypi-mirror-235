# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prefect_dbt_flow', 'prefect_dbt_flow.dbt', 'prefect_dbt_flow.utils']

package_data = \
{'': ['*']}

install_requires = \
['prefect>=2.13.2,<3.0.0']

setup_kwargs = {
    'name': 'prefect-dbt-flow',
    'version': '0.1.0',
    'description': 'Prefect - dbt integration',
    'long_description': '<p align="center">\n  <a href="https://datarootsio.github.io/prefect-dbt-flow"><img alt="logo" src="https://dataroots.io/assets/logo/logo-rainbow.png"></a>\n</p>\n<p align="center">\n  <a href="https://dataroots.io"><img alt="Maintained by dataroots" src="https://dataroots.io/maintained-rnd.svg" /></a>\n  <a href="https://pypi.org/project/prefect-dbt-flow/"><img alt="Python versions" src="https://img.shields.io/pypi/pyversions/prefect-dbt-flow" /></a>\n  <a href="https://pypi.org/project/prefect-dbt-flow/"><img alt="PiPy" src="https://img.shields.io/pypi/v/prefect-dbt-flow" /></a>\n  <a href="https://pepy.tech/project/prefect-dbt-flow"><img alt="Downloads" src="https://pepy.tech/badge/prefect-dbt-flow" /></a>\n  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg" /></a>\n  <a href="http://mypy-lang.org/"><img alt="Mypy checked" src="https://img.shields.io/badge/mypy-checked-1f5082.svg" /></a>\n</p>\n\n# prefect-dbt-flow\nPrefect-dbt-flow is a Python library that enables Prefect to convert dbt workflows into independent tasks within a Prefect flow. This integration simplifies the orchestration and execution of dbt models and tests using Prefect, allowing you to build robust data pipelines and monitor your dbt projects efficiently.\n\n**Active Development Notice:** Prefect-dbt-flow is actively under development and may not be ready for production use. We advise users to be aware of potential breaking changes as the library evolves. Please check the changelog for updates.\n\n## Table of Contents\n- [Introduction](#introduction)\n- [Why Use Prefect-dbt-flow?](#why-use-prefect-dbt-flow)\n- [How to Install](#how-to-install)\n- [Basic Usage](#basic-usage)\n- [Inspiration](#inspiration)\n- [License](#license)\n\n## Introduction\nPrefect-dbt-flow is a tool designed to streamline the integration of dbt workflows into Prefect. dbt is an immensely popular tool for building and testing data transformation models, and Prefect is a versatile workflow management system. This integration brings together the best of both worlds, empowering data engineers and analysts to create robust data pipelines.\n\n## Why Use Prefect-dbt-flow?\n### Simplified Orchestration\nWith Prefect-dbt-flow, you can orchestrate your dbt workflows with ease. Define and manage your dbt projects and models as Prefect tasks, creating a seamless pipeline for data transformation.\n\n[Simplified Orchestration]()\n\n### Monitoring and Error Handling\nPrefect provides extensive monitoring capabilities and error handling. Now, you can gain deep insights into the execution of your dbt workflows and take immediate action in case of issues.\n\n[Monitoring and Error Handling]()\n\n### Workflow Consistency\nEnsure your dbt workflows run consistently by managing them through Prefect. This consistency is crucial for maintaining data quality and reliability.\n\n[Workflow Consistency]()\n\n## How to Install\nYou can install Prefect-dbt-flow via pip:\n```shell\npip install prefect-dbt-flow\n```\n## Basic Usage\nHere\'s an example of how to use Prefect-dbt-flow to create a Prefect flow for your dbt project:\n```python\nfrom prefect_dbt_flow import dbt_flow\nfrom prefect_dbt_flow.dbt import DbtProfile, DbtProject, DbtDagOptions\n\nmy_flow = dbt_flow(\n        project=DbtProject(\n            name="my_flow",\n            project_dir="path_to/dbt_project",\n            profiles_dir="path_to/dbt_profiles",\n        ),\n        profile=DbtProfile(\n            target="dev",\n        ),\n        dag_options=DbtDagOptions(\n            run_test_after_model=True,\n        ),\n    )\n\nif __name__ == "__main__":\n    my_flow()\n```\nFor more information consult the [Getting started guide](GETTING_STARTED.md)\n\n## Inspiration\nPrefect-dbt-flow draws inspiration from various projects in the data engineering and workflow orchestration space, including:\n- [cosmos by astronomer](https://github.com/astronomer/astronomer-cosmos)\n- [anna-geller => prefect-dataplatform](https://github.com/anna-geller/prefect-dataplatform)\n- [dbt + Dagster](https://docs.dagster.io/integrations/dbt)\n\n# License\nThis project is licensed under the MIT License. You are free to use, modify, and distribute this software as per the terms of the license. If you find this project helpful, please consider giving it a star on GitHub.',
    'author': 'David Valdez',
    'author_email': 'david@dataroots.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://datarootsio.github.io/prefect-dbt-flow',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
