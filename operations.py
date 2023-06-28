"""
THIS FILE IS PART OF THE OPS PACKAGE.
"""

import os
import csv
import socket
from datetime import datetime


def ops(func):
    """
    Decorator to log operations.

    The decorator will log the following information in a CSV file.

    Args:
        func (function): The function to be decorated.
    """
    def wrapper(*args, **kwargs):
        op_data = {}
        op_data = _prepare_op_data(op_data, func.__name__)
        op_data['hora_início'] = datetime.now()
        try:
            op_data['resultado'] = func(*args, **kwargs)
        except Exception as e:
            op_data['erros'] = str(e)
            OpsRecorder.add_erro(op_data['processo'], op_data['processo'], str(e))
        op_data['hora_fim'] = datetime.now().strftime('%H:%M:%S')
        op_data['tempo_execucao'] = str(datetime.now() - op_data['hora_início'])
        csv_file_path = _get_csv_file_path(op_data['processo'])
        _create_logs_folder()
        existing_data = _read_csv(csv_file_path)
        _update_existing_op(existing_data, op_data)
        _write_csv(csv_file_path, existing_data)
    return wrapper


class OpsRecorder:
    @staticmethod
    def add_erro(nome_processo, nome_op, erro_descricao):
        csv_file_path = _get_csv_file_path(nome_processo)
        _create_logs_folder()
        existing_data = _read_csv(csv_file_path)
        _add_erro_to_op(existing_data, nome_op, erro_descricao)
        _write_csv(csv_file_path, existing_data)


def _prepare_op_data(op_data, nome_op):
    op_data.setdefault('data', datetime.now().date())
    op_data.setdefault('hora_início', datetime.now())
    op_data.setdefault('hora_fim', '')
    op_data.setdefault('erros', '')
    op_data.setdefault('tempo_execucao', '')
    op_data.setdefault('resultado', '')  # Adicionado o campo "resultado"
    op_data.setdefault('ip', _get_ip())
    op_data.setdefault('hostname', socket.gethostname())
    op_data.setdefault('conexão', _check_internet_connection())
    op_data['processo'] = nome_op
    return op_data


def _get_csv_file_path(nome_processo):
    return f'logs/{nome_processo}.csv'


def _create_logs_folder():
    if not os.path.exists('logs'):
        os.makedirs('logs')


def _read_csv(csv_file_path):
    try:
        with open(csv_file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        return data
    except FileNotFoundError:
        return []


def _write_csv(csv_file_path, data):
    fieldnames = ['data', 'hora_início', 'hora_fim', 'processo', 'ip', 'hostname', 'conexão', 'erros',
                  'tempo_execucao', 'resultado']
    mode = 'a' if os.path.exists(csv_file_path) else 'w'
    with open(csv_file_path, mode, newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(data[0])


def _update_existing_op(existing_data, op_data):
    for existing_op in existing_data:
        if existing_op['processo'] == op_data['processo']:
            existing_op.update(op_data)
            return
    existing_data.append(op_data)


def _add_erro_to_op(existing_data, nome_op, erro_descricao):
    for existing_op in existing_data:
        if existing_op['processo'] == nome_op:
            existing_op['erros'] = erro_descricao  # Substituído o campo "erros" pela descrição do erro
            return


def _get_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        return ''


def _check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False
