# SPDX-FileCopyrightText: 2023 Ngô Ngọc Đức Huy <huyngo@disroot.org>
#
# SPDX-License-Identifier: GPL-3.0-only
"""Generic key-value storage handling library"""

from argparse import ArgumentParser

from rasc import cli

__version__ = '0.1.0'
__description__ = 'Generic key-value storage handling library'


def lax():
    parser = ArgumentParser(prog='rasc', description='Demo config command')
    subparsers = parser.add_subparsers()

    cli.add_to_parser(subparsers)
    args = parser.parse_args()
    args.func(args)


def strict():
    parser = ArgumentParser(prog='rasc-strict',
                            description='Demo config command with strict mode')
    subparsers = parser.add_subparsers()

    cli.add_to_parser(subparsers, 'rasc-strict',
                      default_config={'cfg_1': 'str_option',
                                      'cfg_2': {'cfg_a': 123,
                                                'cfg_b': False}},
                      strict=True)
    args = parser.parse_args()
    args.func(args)
