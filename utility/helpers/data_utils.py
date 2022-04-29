import random
import string
import pandas


def get_random_string():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(6))


def get_headers(data):
    if data:
        _ = [tuple(record.keys()) for record in data]
        headers = ", ".join([rec for rec in list(_[0])])
        return f"({headers})"


def form_strings(data):
    strings = ",".join(['%s ' for _ in list(data[0])])
    return f"({strings})"


def process_dataframe(list_of_dicts, type_):
    df = pandas.DataFrame(list_of_dicts)
    df.rename({'trans_id': 'trans_id', 'user_id': '', 'branch_id': '', 'company_code': '', 'terminal_id': '', 'merchant_id': 'inst_id',
               'product_id': '', 'service_code': '', 'payee_id': '', 'payee_name': '', 'dr_account_no': '',
               'cr_account_no': '',
               'trans_type': '', 'terminal_type': '', 'date_created': 'date_created', 'time_created': '', 'date_posted': 'date_processed',
               'time_posted': 'processing_time',
               'currency': 'currency', 'amount': 'amount', 'fee': '', 'payer_name': 'payer_name', 'payer_mobile': 'mobile', 'payer_email': 'email',
               'rev_status': '', 'rev_trans_id': '', 'trans_desc': '', 'rev_scope': '', 'ps_status': '',
               'up_status': 'up_status',
               'source_trans_id': 'bank_trans_id', 'accountcode': '', 'cb_retries': '', 'settle_status': ''

               }, axis=1, inplace=True)
    df['source_time_created'] = df['source_time_created'].astype('str').str.split().str[-1]
    df['source_id'] = ['MTN' for _ in range(len(df.index))]
    df['country'] = ['GH' for _ in range(len(df.index))]
    df['recon_type'] = [type_ for _ in range(len(df.index))]
    df.drop('created', axis=1, inplace=True)
    return df
