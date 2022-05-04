from utility.helpers import data_utils
import pandas


def insert_transactions_from_queue(db_module, transactions):
    if transactions:
        columns, values = process_dataframe(transactions)
        headers, str_fmt, data = process_transactions(columns, values)
        rows = db_module.insert_records(data, headers, str_fmt)
        return rows


def process_transactions(columns, values):
    headers = ",".join([f"`{s}`" for s in list(columns)])
    headers = f"({headers})"
    str_fmt = data_utils.form_strings(columns)
    data = [tuple(record) for record in values]
    return headers, str_fmt, data


def process_dataframe(list_of_dicts):
    fields = ['trans_id', 'merchant_id', 'product_id', 'service_code', 'payee_id', 'payee_name', 'cr_account_no',
              'trans_type', 'date_created', 'date_posted', 'time_posted', 'currency', 'amount', 'fee',
              'payer_mobile', 'payer_email', 'trans_desc', 'up_status', 'source_trans_id', 'accountcode']
    df = pandas.DataFrame(list_of_dicts, columns=fields)
    df.rename({'trans_id': 'trans_id', 'merchant_id': 'inst_id', 'product_id': 'desc_id', 'service_code': 'alt5',
               'payee_id': 'alt1', 'payee_name': 'payer_name', 'cr_account_no': 'account_no',
               'trans_type': 'alt4', 'date_created': 'date_created','date_posted': 'date_processed',
               'time_posted': 'processing_time', 'currency': 'currency',
               'amount': 'amount', 'fee': 'subscription', 'payer_mobile': 'mobile', 'payer_email': 'email',
               'trans_desc': 'alt2', 'up_status': 'up_status', 'source_trans_id': 'bank_trans_id', 'accountcode': 'alt3'
               }, axis=1, inplace=True)
    columns = df.columns.values.tolist()
    values = df.values.tolist()
    return columns, values
