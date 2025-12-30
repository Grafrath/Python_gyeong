import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

data = pd.DataFrame({
    'color': ['red', 'green', 'blue', 'red'],
    'size': ['S', 'M', 'L', 'S'],
    'shape': ['circle', 'square', 'triangle', 'circle']
})

encoder = OneHotEncoder(sparse_output=False)

print(data.ndim)
print()

encoded = encoder.fit_transform(data)
print(encoded)
print()

encoded_df = pd.DataFrame (
    encoded,
    columns=encoder.get_feature_names_out(data.columns)
)

print(encoded_df)
print()

encoder_drop = OneHotEncoder(sparse_output=False, drop='first')
encoded_drop = encoder_drop.fit_transform(data)

print(encoder_drop.get_feature_names_out(data.columns))
print()

final_df = pd.concat([data, encoded_df], axis=1)

# 원본 문자열 컬럼은 이제 필요 없으니 삭제
final_df.drop(['color', 'size', 'shape'], axis=1, inplace=True)
print(final_df.head())
print()