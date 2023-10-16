import os
from yaml import safe_load
from json import loads
from typing import Dict
from pyspark import SparkConf

DEFAULT_CONFIG_PATH = os.path.expanduser("~/.spark")


def build_config(config_path: str = None, master: str = None, app_name: str = None, conf: Dict = None) -> SparkConf:
    if config_path is None:
        if os.path.exists(DEFAULT_CONFIG_PATH):
            config_path = next(
                (
                    "{}/{}".format(DEFAULT_CONFIG_PATH, k)
                    for k in os.listdir(os.path.expanduser("~/.spark"))
                    if os.path.basename(k).startswith("config")
                ),
                None,
            )
    if config_path is None:
        raise FileNotFoundError(
            "If the Spark configuration file is not located in the ~/.spark directory, "
            "then the path must be explicitly defined."
        )

    if config_path.endswith(".json"):
        confL = loads(open(config_path, "r").read())
    elif config_path.endswith(".yml") or config_path.endswith(".yaml"):
        confL = safe_load(open(config_path, "r"))
    else:
        raise NotImplementedError("The file type for {} is not supported".format(config_path))

    master0 = confL.get("master", None)
    if master is None:
        master = master0

    app_name0 = confL.get("app_name", None)
    if app_name is None:
        app_name = app_name0

    newConf = confL.get("conf", {})
    if conf is not None:
        newConf.update(conf)
    conf = newConf

    sparkConfig = SparkConf()
    for k, v in conf.items():
        if isinstance(v, list):
            v = ",".join(v)
        elif isinstance(v, str) and v.startswith("${{"):
            environment_variable_name = v[3:-2]
            value = os.environ.get(environment_variable_name, None)
            if value is None:
                raise KeyError(f"The environment variable {environment_variable_name} was not found.")
            v = value
        sparkConfig.set(k, v)

    sparkConfig.setAppName(app_name)
    if master is not None:
        sparkConfig.setMaster(master)
    return sparkConfig


