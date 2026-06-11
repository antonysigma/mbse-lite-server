# IT infrastructure for MBSE-lite

> [!NOTE]
> Completely optional for open-source MBSE projects. Skip this if your
> organization permits access to `https://plantuml.com` and the online diagram rendering APIs.

This repository houses the self-documenting deployment scripts for the
MBSE-lite's diagram rendering services.

## Minimum system requirements

- Ubuntu Desktop
- Python >= 3.10

## Quick start

Assuming you have [UV: the python-pip
accelerator](https://docs.astral.sh/uv/#installation) installed, download the Ansible toolbox:

```shell
uv venv --python=3.12
source .venv/bin/activate
uv pip install -r requirements.txt
```

Next, perform sanity checks of the Ansible deployment scripts

```shell
source .venv/bin/activate
ansible-lint deploy-everything.playbook.yml
```

Now, execute the following script, and then provide Administrator password when prompted.
```shell
source .venv/bin/activate
ansible-playbook -K deploy-everything.playbook.yml
```

> [!NOTE]
> If you are new to Ansible and concerned about sharing Admin/Root password to
> the Ansible local tool, please remove the argument `-K` from the command, the
> Ansible tool will in turn explain the key deployment step(s) requiring
> Administrator permissions.

## Contributing

Prefer microservice architecture over monolithic. Each diagram rendering service
is supposed to be a separate process owning a separate TCP/IP port, e.g.
PlantUML server at port 8000, and IDEF0 server at port 5000.

In other words, for new diagrams, e.g. railroad diagram, we prefer a new Restful
service (e.g. with Nodejs runtime) serving through a new TCP/IP port.

## Folder structure

Informally known as the PHP, aka "kitchen sink" architecture, the MBSE-lite
infrastructure primarily use Python and Restful API as the glue logic of the a
number of internal services backends. This hides the software logic from the
non-technical authors, minimizing distractions for them to capture hardware /
software / firmware / electrical / optics /  Algorithm / GPU system
requirements, sub-system requirements, design constraints, and performance
constraints.

Specifically, the Python language act as a glue to interate the following projects:

- IDEF0SVG text-to-SVG converter, written in Ruby;
- High-level abstraction of the IDEF0 diagramming language, written in PEG/Python;
- Restful web server to accept IDEF0 rendering requests, written in FastAPI/Python;
- Self-documenting, continuous deployment script of the IT infrastructure, written in Ansible/Python.
- Various sanity checking scripts in TOML, Ruff, NodeJs, and Mypy.

The project folder structure is in accordance to the Ansible standards: instead
of individual module and folders "my_project1-src/" at the root adjacent to the
global "install_scripts/" folder, Ansible prefers all software modules to be
embedded in the nested path: `roles/idef0svg-server/files/my_project1-src/`. The
master deployment script `deploy-everything.playbook.yml` then collects and
executes individual IT server "roles" in the folder `roles/` in sequence.
