from pathlib import Path
import pandas as pd

# egt_failure_dataset, исходная ревизия wash-dashboard: 44dacb1
url = (
    "https://storage.yandexcloud.net/ecm-data/"
    "egt-failure-dataset/files/md5/7c/6504aba5264de19a84b068859c29c2"
)

source = pd.read_parquet(url)
dataset = source.loc[source.failure_value.eq(1)].copy()
dataset["type"] = pd.Series(
    "egt_indication", index=dataset.index, dtype="string"
)

keys = [
    "aircraft_id", "engine_position", "flight_phase",
    "flight_datetime", "type",
]
columns = [
    "aircraft_id", "engine_position", "engine_id", "type",
    "flight_phase", "flight_datetime", "failure_value",
]

assert not dataset[keys].isna().any().any()
assert not dataset.duplicated(keys).any()
assert dataset.failure_value.eq(1).all()
assert len(dataset) == 2784

target = Path("data/anomaly_labels.parquet")
target.parent.mkdir(exist_ok=True)
assert not target.exists(), "Начальная миграция уже выполнена"

dataset[columns].sort_values(keys).to_parquet(target, index=False)
print(f"Сохранено {len(dataset)} точек: {target}")


