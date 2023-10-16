from abc import ABCMeta
import json
import re
import threading
import logging
import os
import sys

class MetaType(ABCMeta):

    def __new__(cls:type, 
                cls_name:str, 
                cls_bases:tuple[type], 
                cls_objects:dict) -> type:
        if cls_bases and '__init__' in cls_objects:
            derived_cls_init = cls_objects['__init__']
            def init(self, **kwargs):
                ProtoType.__init__(self, **kwargs)
                derived_cls_init(self, **kwargs)
            cls_objects['__init__'] = init
        return super().__new__(cls, cls_name, cls_bases, cls_objects)

class ProtoType(metaclass=MetaType):

    def __init__(self, **kwargs) -> None:
        for attribute_name, value in kwargs.items():
            setattr(self, attribute_name, value)
        class_path = str(self.__class__)
        path_pattern = r"<class '(.*?)'>"
        full_class_name: str = re.search( path_pattern, class_path).group(1)
        self.log_level: str = kwargs.get('log_level', 'INFO')
        self.log = LogBuild(name=full_class_name, level=self.log_level)
        self.data_lock = threading.Lock()
        if not hasattr(ProtoType, 'data'):
            ProtoType.data = SharedData()
        doc_gen = DocGen({**self.__dict__, **self.__class__.__dict__})
        with self.data_lock:
            if 'classes' not in ProtoType.data.config:
                ProtoType.data.config['classes'] = {}
            ProtoType.data.config['classes'][full_class_name] = doc_gen.doc

    @staticmethod
    def close() -> None:
        data_att = {attribue_name: type(val).__name__ 
                    for attribue_name, val in ProtoType.data.__dict__.items() 
                    if not callable(getattr(ProtoType.data, attribue_name)) 
                    and not attribue_name.startswith('_')}
        ProtoType.data.config['data'] = data_att
        with open(ProtoType.data.config_json_path, 'w') as json_file:
            json.dump(ProtoType.data.config, json_file, indent=4, 
                      ensure_ascii=False, separators=(',', ': '))

class LogBuild:
    
    def __init__(self, name:str, level:str) -> None:
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.propagate = False
        set_level = logging._nameToLevel[level]
        self.logger.setLevel(set_level)
        if not self.logger.handlers:
            msg = '%(levelname)s: %(asctime)s | %(message)s | %(name)s'
            formatter = logging.Formatter(msg)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def debug(self, message:str) -> None:
        self.logger.debug(message)
    def info(self, message:str) -> None:
        self.logger.info(message)
    def warning(self, message:str) -> None:
        self.logger.warning(message)
    def error(self, message:str) -> None:
        self.logger.error(message)
    def critical(self, message:str) -> None:
        self.logger.critical(message)

class DocGen:

    def __init__(self, attrs:dict):
        self.attrs = attrs
        self.doc = {
            'docstring': self._flatten_docstring(attrs.get('__doc__')),
            'attributes': {},
            'methods': {}
        }
        self._generate_doc_dict()

    def _generate_doc_dict(self) -> None:
        for attr_name, attr_value in self.attrs.items():
            if callable(attr_value) and attr_name != '__init__':
                self.doc['methods'][attr_name] = \
                    self._flatten_docstring(attr_value.__doc__)
            else:
                if not attr_name.startswith('_'):
                    self.doc['attributes'][attr_name] = \
                        type(attr_value).__name__

    def _flatten_docstring(self, docstring) -> str|None:
        if not docstring:
            return None
        return ' '.join(docstring.split())

class SharedData:

    def __init__(self) -> None:
        self.config_json_path:str = os.environ.get('CONFIG_JSON_PATH', '.')
        self.config:dict = self._generate_config()

    def _get_json(self, json_path) -> dict:
        with open(json_path, 'r') as file:
            return json.load(file)

    def _get_args(self) -> dict:
        arg_dict = {}
        for arg in sys.argv[1:]:
            if arg.startswith('--'):
                key, value = arg[2:].split('=')
                arg_dict[key] = value
        return arg_dict

    def _get_env(self, config_dict) -> dict:
        env_dict = {}
        for key in config_dict.keys():
            if os.environ.get(key.upper()):
                env_dict[key] = os.environ.get(key.upper())
        return env_dict

    def _generate_config(self) -> dict:
        config:dict = self._get_json(self.config_json_path)
        arg_dict = self._get_args()
        env_dict = self._get_env(config)
        output_config = {}
        for var_name, default_value in config.items():
            env_val = env_dict.get(var_name, default_value)
            final_val = arg_dict.get(var_name, env_val)
            output_config[var_name] = final_val
        return output_config