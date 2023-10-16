# SPDX-FileCopyrightText: 2023 Ngô Ngọc Đức Huy <huyngo@disroot.org>
#
# SPDX-License-Identifier: GPL-3.0-only

import json
from argparse import Namespace
from typing import Callable

from rasc.storage import Configuration


def config(command: str, ext: str = 'json',
           default_config: dict = {},
           load_func: Callable = json.load,
           dump_func: Callable = json.dump,
           strict: bool = False,
           allowed_types: list = [str, int, bool]):
    def handle_config(args: Namespace) -> None:
        if args.get:
            action = 'get'
        elif args.set:
            if args.value is None:
                print('error: no value to set to the variable')
                return
            action = 'set'
        elif args.value is not None:
            action = 'set'
        else:
            action = 'get'
        config = Configuration(command, ext, default_config, load_func,
                               dump_func, strict, allowed_types)
        config.load()
        if action == 'get':
            print(config.get(args.key))
        elif action == 'set':
            try:
                config.set(args.key, args.value)
                config.save()
            except Exception as e:
                print('error:', e)
    return handle_config


def add_to_parser(sub: any, command: str = 'rasc',
                  config_command: str = 'config',
                  ext: str = 'json',
                  default_config: dict = {},
                  load_func: Callable = json.load,
                  dump_func: Callable = json.dump,
                  strict: bool = False,
                  allowed_types: list = [str, int, bool]) -> None:
    """Add 'config' as a subcommand."""
    config_parser = sub.add_parser(config_command)
    mutex_options = config_parser.add_mutually_exclusive_group()
    mutex_options.add_argument('--get', action='store_true')
    mutex_options.add_argument('--set', action='store_true')
    config_parser.add_argument('key')
    config_parser.add_argument('value', nargs='?')
    config_parser.set_defaults(func=config(command, ext, default_config,
                                           load_func, dump_func, strict,
                                           allowed_types))
