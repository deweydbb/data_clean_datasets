

### Hospital

Data set from Holoclean (https://github.com/HoloClean)
Described in the paper as: "Errors amount to ∼ 5% of the total data. Ground truth in-
formation is available for all cells. This dataset exhibits significant
duplication across cells. *We use it to evaluate how effective Holo-
Clean is at leveraging duplicate information during cleaning.*


### Flights

Data set from Holoclean (https://github.com/HoloClean)
The majority of cells in Flights are noisy and the lineage of each tuple
is know. We use this dataset to examine how robust HoloClean is
in the presence of many errors, and to evaluate if HoloClean can
exploit conflicts across data sources to identify correct data repairs.

Seems like dataset isn't the best in term of the fact that a large majority of cells are incorrect

### Adults

Data set from fm_data_tasks/HazyResearch (https://github.com/HazyResearch/fm_data_tasks)
I took the clean data and then produced dirty data using error-generation (https://github.com/BigDaMa/error-generator)
The dirty data includes common typos on a qwerty keyboard, missing values and implicitly missing values
ex: age = 0, as well as values replaced with values from other columns