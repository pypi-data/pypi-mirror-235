# SPDX-FileCopyrightText: 2023 Ngô Ngọc Đức Huy <huyngo@disroot.org>
#
# SPDX-License-Identifier: GPL-3.0-only

import os
import json
from typing import Callable


class Storage:
    """Generic class for read/write key-object stored data.

    Attributes:
        home        The directory where the data are stored
        paths       Map from file paths (relative to the home) to keys
        data        Map from keys to stored data objects
        load_func   Function to read from a file, default to ``json.load``,
                    should support similar interface to ``json.load``
        dump_func   Function to write to a file, default to `json.dump`,
                    should support similar interface to ``json.dump``
    """
    def __init__(self, home: str, paths: dict, data: dict,
                 load_func: Callable = json.load,
                 dump_func: Callable = json.dump):
        self.home = home
        self.paths = paths
        self.data = data
        self.load_func = load_func
        self.dump_func = dump_func

    def get(self, key: str) -> any:
        """Get data from ``self.data``."""
        return self.data.get(key)

    def set(self, key: str, data: any) -> None:
        self.data[key] = data

    def load(self) -> None:
        """Load data to ``self.data``."""
        for key in self.paths:
            self._load_file(key)

    def save(self) -> None:
        """Save data from ``self.data``."""
        for key in self.paths:
            self._save_file(key)

    def _load_file(self, key: str) -> None:
        file_path = os.path.join(self.home, self.paths[key])
        try:
            with open(file_path) as f:
                self.data[key] = self.load_func(f)
        except FileNotFoundError:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                self.dump_func({}, f)
                self.data[key] = {}

    def _save_file(self, key: str) -> None:
        file_path = os.path.join(self.home, self.paths[key])
        with open(file_path, 'w') as f:
            self.dump_func(self.data[key], f)


class Configuration(Storage):
    """Example class for read/write config object.

    Attributes:
        name            Name of the software that use config
        ext             File extension for config, default to ``"json"``
        config          Default config to be used
        load_func       Function to read from a file, default to ``json.load``,
                        should support similar interface to ``json.load``
        dump_func       Function to write to a file, default to `json.dump`,
                        should support similar interface to ``json.dump``
        strict          Whether to validate new config value.  If set to True,
                        one cannot add new value nor change value type.
        allowed_types   Types to be set to new values; only considered if
                        ``strict`` is ``False``
    """
    def __init__(self, name: str, ext: str = 'json', config: dict = {},
                 load_func: Callable = json.load,
                 dump_func: Callable = json.dump,
                 strict: bool = False,
                 allowed_types: list = [str, int, bool]) -> None:
        self.name = name
        self.ext = ext
        self.allowed_types = allowed_types
        self.strict = False
        if config:
            self.strict = strict
        elif strict:
            # TODO: should use logger instead
            print('Warning: no config structure is provided, '
                  'strict is set to False to allow adding configs')
        data_home = os.getenv('XDG_CONFIG_HOME')
        if data_home is None:
            data_home = os.path.join(os.getenv('HOME'), '.config')
        home = os.path.join(data_home, name)
        paths = {'config': f'config.{ext}'}
        data = {'config': config}
        super().__init__(home, paths, data, load_func, dump_func)

    def get(self, key: str) -> any:
        keys = key.split('.')
        current_object = self.data['config']
        for k in keys:
            current_object = current_object.get(k)
            if current_object is None:
                return current_object
        return current_object

    def set(self, key: str, data: any) -> None:
        if type(data) not in self.allowed_types:
            raise TypeError(f'{data} of type {type(data)} is not allowed')
        keys = key.split('.')
        current_object = self.data['config']
        for i, k in enumerate(keys):
            previous_object = current_object
            current_object = current_object.get(k)
            if current_object is None:
                if self.strict:
                    raise ValueError(f'Unknown config: {key}')
                else:
                    new_object = data
                    for kk in reversed(keys[i+1:]):
                        new_object = {kk: new_object}
                    previous_object[k] = new_object
                    return
        if current_object is not None:
            if self.strict:
                current_type = type(current_object)
                try:
                    if current_type is bool:
                        previous_object[k] = self.booleanize(data)
                    else:
                        previous_object[k] = current_type(data)
                except ValueError:
                    raise TypeError(f'Cannot set {data} to {key},'
                                    f'which is of type {current_type}')
            else:
                previous_object[k] = data

    def load(self):
        old_data = self.data['config']
        super().load()
        if not self.data['config']:
            self.data['config'] = old_data
            self.save()

    @staticmethod
    def booleanize(value: str | int | bool | None) -> bool:
        if type(value) is bool:
            return value
        elif type(value) is int:
            return bool(value)
        elif value.lower() in ['false', 'off', 'f', '0'] or value is None:
            return False
        return True

    def _save_file(self, key: str) -> None:
        if self.ext == 'json':
            file_path = os.path.join(self.home, self.paths[key])
            with open(file_path, 'w') as f:
                # Use indent to have nice, readable config file
                self.dump_func(self.data[key], f, indent=2)
        else:
            super()._save_file(key)
