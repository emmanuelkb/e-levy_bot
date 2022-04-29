from utility.helpers import data_utils


def insert_transactions_from_queue(db_module, transactions):
    if transactions:
        headers, str_fmt, data = process_transactions(transactions)
        print(headers)
        print(str_fmt)
        print(data)
        # exit()
        rows = db_module.insert_records(data, headers, str_fmt)
        return rows


def process_transactions(transactions):
    headers = data_utils.get_headers(transactions)
    str_fmt = data_utils.form_strings(transactions)
    data = [tuple(record.values()) for record in transactions]
    return headers, str_fmt, data
