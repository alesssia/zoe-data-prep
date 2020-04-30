import dataset
import pipeline
import utils

filename = 'test_patients.csv'
with open(filename) as f:
    ds = dataset.Dataset(f)

for ir in range(ds.row_count()):
    utils.print_diagnostic_row(f'{ir}', ds, ir,
                               ('id', 'weight_kg', 'height_cm', 'bmi', 'weight_clean', 'height_clean', 'bmi_clean'))
