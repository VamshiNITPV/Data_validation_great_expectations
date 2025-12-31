import great_expectations as ge
import pandas as pd
import sys

DATA_PATH = "data/customer_data.csv"
GE_CONTEXT_PATH = "gx"
CHECKPOINT_NAME = "customer_checkpoint"

def run_etl_validation():
    df = pd.read_csv(DATA_PATH)

    context = ge.data_context.DataContext(GE_CONTEXT_PATH)

    result = context.run_checkpoint(
        checkpoint_name=CHECKPOINT_NAME,
        batch_request={
            "datasource_name": "my_datasource",
            "data_connector_name": "default_runtime_data_connector_name",
            "data_asset_name": "customer_data",
            "runtime_parameters": {"batch_data": df},
            "batch_identifiers": {"default_identifier_name": "default"},
        },
    )

    if result["success"]:
        print("Data validation successful. ETL can proceed.")
    else:
        print("Data validation failed. Review expectations.")
        sys.exit(1)

if __name__ == "__main__":
    run_etl_validation()
