The KCL covid19 joinzoe data preparation pipeline.

# Cleaning scripts

Current version: v0.1.9

---
## `pipeline.py`

### Running the pipeline
```
python pipeline.py -t <territory> -p <input patient csv> -a <input assessor csv> -po <output patient csv -ao <output assessor csv>
```

#### options
 * `-t` / `--territory`: the territory to filter the dataset on (runs on all territories if not set)
 * `-p` / `--patient_data`: the location and name of the patient data csv file
 * `-a` / `--assessment_data`: the location and name of the assessment data csv file
 * `-po` / `--patient_data_out`: the location and name of the output patient data csv file
 * `-ao` / `--assessment_data_out`: the location and name of the output assessment data csv file
 * `-ps` / `--parsing_schema`: the schema number to use for parsing and cleaning data

### Pipeline help
```
python pipeline.py --help
```

### Pipeline version
```
python pipeline.py --version
```

#### parsing schema
There are currently 2 parsing schema versions:
* 1: The baseline cleaning behaviour, intented to match the R script
* 2 (in progress): Improved cleaning for height/weight/BMI and covid symptom progression

#### Including in a script

Use the function `pipeline()` from `pipeline.py`.

Proper documentation and packaging to follow

---
## `split.py`

### Running the split script
```
python split.py -t <territory> -p <input patient csv> -a <input assessor csv> -b <bucket size>
```

The output of the split script is a series of patient and assessment files with the following structure:
```
<filename>.csv -> <filename>_<index>.csv
```
where index is the padded index of the subset (0000, 0001, 0002...).

#### options
 * `-p` / `--patient_data`: the location and name of the patient data csv file
 * `-a` / `--assessment_data`: the location and name of the assessment data csv file
 * `-b` / `--bucket_size`: the maximum number of patients to include in a subset

### Split script help
```
python split.py --help
```

### Split script version
```
python split.py --version
```

---
## Changes

### v0.1.8 -> v0.1.9
* Feature: provision of the `split.py` script to split the dataset up into subsets of patients
  and their associated assessments
* Fix: added `treatments` and `other_symptoms` to cleaned assessment file. These fields are
  concatenated during the merge step using using csv-style delimiters and escapes

### v0.1.7 -> v0.1.8
* Fix: `had_covid_test` was not being patched up along with `tested_covid_positive`'
* Breaking change: output fields renamed
  * Fixed up `had_covid_test` is output as `had_covid_test_clean`
  * Fixed up `tested_covid_positive` is output as `tested_covid_positive_clean`
  * `had_covid_test` and `tested_covid_positive` contain the un-fixed-up data (although rows may
    still be modified as a result of quantising assessments by day)

### v0.1.6 -> v0.1.7
* Fix: `height_clean` contains weight data and `weight_clean` contains height data.
  This has been the case since they were introduced in v0.1.5

### v0.1.5 -> v0.1.6
* Performance: reduced memory usage
* Addition: provision of `-ps` flag for setting parsing schema

### v0.1.4 -> v0.1.5
* Fix: `health_status` was not being accumulated during the assessment compression phase of cleanup

### v0.1.3 -> v0.1.4
* Fix: added missing value `rarely_left_the_house_but_visit_lots` to `level_of_isolation`
* Fix: added missing fields `weight_clean`, `height_clean` and `bmi_clean`

### v0.1.2 -> v0.1.3
* Fix: `-po` and `-ao` options now properly export patient and assessment csvs respectively

### v0.1.1 -> v0.1.2
* Fix: `day` no longer overwriting `tested_covid_positive` on assessment export
* Fix: `tested_covid_positive` output as a label instead of a number

### v0.1 -> v0.1.1
* Change: Converted `'NA'` to `''` for csv export


