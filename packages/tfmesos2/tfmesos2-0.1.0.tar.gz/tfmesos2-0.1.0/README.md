# Tensorflow V2 for Mesos

## Requirements

- Apache Mesos minimum 1.6.x

## How to use

Tensorflow for Mesos need some environment variables to know how and which Mesos it should use.

```bash

export MESOS_SSL=true
export MESOS_MASTER=localhost:5050
export MESOS_USERNAME=<MESOS_PRINCIPAL>
export MESOS_PASSWORD=<MESOS_SECRET>

python examples/plus.py

```
