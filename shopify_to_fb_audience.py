# -----------------------------
# Imports
# -----------------------------

import glob
import pandas as pd

# -----------------------------
# Original customer DataFrame created
# -----------------------------

path = 'exports/' # use your path
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []

# -----------------------------
# Setting dtypes for each column
# -----------------------------
my_dtypes = {
    "Name": str,"Email": str,"Financial Status": str,"Paid at": str,"Fulfillment Status": str,"Fulfilled at": str,"Accepts Marketing": str,"Currency": str,"Subtotal": float,"Shipping": float,"Taxes": float,"Total": float,"Discount Code": str,"Discount Amount": float,"Shipping Method": str,"Created at": str,"Lineitem quantity": float,"Lineitem name": str,"Lineitem price": float,"Lineitem compare at price": str,"Lineitem sku": str,"Lineitem requires shipping": str,"Lineitem taxable": str,"Lineitem fulfillment status": str,"Billing Name": str,"Billing Street": str,"Billing Address1": str,"Billing Address2": str,"Billing Company": str,"Billing City": str,"Billing Zip": str,"Billing Province": str,"Billing Country": str,"Billing Phone": str,"Shipping Name": str,"Shipping Street": str,"Shipping Address1": str,"Shipping Address2": str,"Shipping Company": str,"Shipping City": str,"Shipping Zip": str,"Shipping Province": str,"Shipping Country": str,"Shipping Phone": str,"Notes": str,"Note Attributes": str,"Cancelled at": str,"Payment Method": str,"Payment Reference": str,"Refunded Amount": str,"Vendor": str,"Outstanding Balance": str,"Employee": str,"Location": str,"Device ID": float,"Id": float,"Tags": str,"Risk Level": str,"Source": str,"Lineitem discount": str,"Tax 1 Name": str,"Tax 1 Value": float,"Tax 2 Name": str,"Tax 2 Value": float,"Tax 3 Name": str,"Tax 3 Value": float,"Tax 4 Name": str,"Tax 4 Value": float,"Tax 5 Name": str,"Tax 5 Value": float,"Phone": str
}

# -----------------------------
# Parse Dates
# -----------------------------
my_parse_dates = ['Paid at', 'Fulfilled at', 'Created at', 'Cancelled at']

# -----------------------------
# Frame
# -----------------------------

for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0, dtype=my_dtypes, parse_dates=my_parse_dates)
    list_.append(df)
frame = pd.concat(list_, ignore_index=True)

#sliced DataFrame to clean and filter on
df1 = frame[['Email', 'Financial Status', 'Paid at', 'Fulfillment Status', 'Fulfilled at', 'Accepts Marketing', 'Currency', 'Subtotal', 'Shipping', 'Taxes', 'Total', 'Discount Code', 'Discount Amount', 'Shipping Method', 'Created at', 'Lineitem quantity', 'Lineitem name', 'Lineitem price', 'Lineitem compare at price', 'Lineitem sku', 'Lineitem requires shipping', 'Lineitem taxable', 'Lineitem fulfillment status', 'Billing Name', 'Billing Street', 'Billing Address1', 'Billing Address2', 'Billing Company', 'Billing City', 'Billing Zip', 'Billing Province', 'Billing Country', 'Billing Phone', 'Cancelled at', 'Payment Method', 'Payment Reference', 'Refunded Amount', 'Vendor']] 

df1

# -----------------------------
# Cleaning
# -----------------------------

# Remove ' from zip
df1['Billing Zip'] = df1['Billing Zip'].str.replace("'", "")

# -----------------------------
# Filters
# -----------------------------
# Todo create a function or class for filters

# Example Filters -------

# # Accepts Marketing
Accepts_Marketing = df1['Accepts Marketing'].str.contains("yes", na=False)

# # Billing Country
Billing_Country = df1['Billing Country'].str.contains("US", na=False)

# # Billing Province
Billing_Province = df1['Billing Province'].str.contains("WA", na=False)

# # Vendor
Vendor = df1['Vendor'].str.contains("Vendor Name", na=False)

# # Subtotals
Subtotals = df1['Subtotal']  > 50

df2 = df1[Billing_Country & Billing_Province & Subtotals]
df2



# -----------------------------
# Facebook audience creation w/ col_map
# -----------------------------

facebook_audience_keys = ['Email', 'Billing City', 'Billing Zip', 'Billing Province','Billing Country','Billing Phone']
facebook_audience = pd.DataFrame(df2, columns=facebook_audience_keys)
col_mapping = {'Email' : 'email',
               'Billing City' : 'ct',
               'Billing Zip' : 'zip',
               'Billing Province' : 'st',
               'Billing Country' : 'country',
               'Billing Phone' : 'phone'}
facebook_audience = facebook_audience.rename(columns=col_mapping, copy=False)
facebook_audience


# -----------------------------
# Facebook to CSV
# -----------------------------
path=r'FacebookAudiences/' # use your path
audience_name = "my_fb_audience" # name your audience
facebook_audience.to_csv(path+audience_name, sep='\t', encoding='utf-8')
