from pandas.api.types import CategoricalDtype

class AGE_BINDINGS:

    TOTAL = 'Total'
    AGE_00_04 = '(0-4)'
    AGE_05_09 = '(5-9)'
    AGE_10_14 = '(10-14)'
    AGE_15_19 = '(15-19)'
    AGE_20_24 = '(20-24)'
    AGE_25_29 = '(25-29)'
    AGE_30_34 = '(30-34)'
    AGE_35_39 = '(35-39)'
    AGE_40_44 = '(40-44)'
    AGE_45_49 = '(45-49)'
    AGE_50_54 = '(50-54)'
    AGE_55_59 = '(55-59)'
    AGE_60_64 = '(60-64)'
    AGE_65_69 = '(65-69)'
    AGE_70_74 = '(70-74)'
    AGE_75_79 = '(75-79)'
    AGE_80_84 = '(80-84)'
    AGE_85_89 = '(85-89)'
    AGE_GE90 = '(90+)'

INFOSTAT_DECODE_AGE_GROUPS = {
    AGE_BINDINGS.AGE_00_04: 5,
    AGE_BINDINGS.AGE_05_09: 5,
    AGE_BINDINGS.AGE_10_14: 5,
    AGE_BINDINGS.AGE_15_19: 5,
    AGE_BINDINGS.AGE_20_24: 5,
    AGE_BINDINGS.AGE_25_29: 5,
    AGE_BINDINGS.AGE_30_34: 5,
    AGE_BINDINGS.AGE_35_39: 5,
    AGE_BINDINGS.AGE_40_44: 5,
    AGE_BINDINGS.AGE_45_49: 5,
    AGE_BINDINGS.AGE_50_54: 5,
    AGE_BINDINGS.AGE_55_59: 5,
    AGE_BINDINGS.AGE_60_64: 5,
    AGE_BINDINGS.AGE_65_69: 5,
    AGE_BINDINGS.AGE_70_74: 5,
    AGE_BINDINGS.AGE_75_79: 5,
    AGE_BINDINGS.AGE_80_84: 5,
    AGE_BINDINGS.AGE_85_89: 5,
    AGE_BINDINGS.AGE_GE90: 9,
}


cat_age_order = CategoricalDtype(
    [AGE_BINDINGS.AGE_00_04, AGE_BINDINGS.AGE_05_09, AGE_BINDINGS.AGE_10_14, AGE_BINDINGS.AGE_15_19,
    AGE_BINDINGS.AGE_20_24, AGE_BINDINGS.AGE_25_29, AGE_BINDINGS.AGE_30_34, AGE_BINDINGS.AGE_35_39,
    AGE_BINDINGS.AGE_40_44, AGE_BINDINGS.AGE_45_49, AGE_BINDINGS.AGE_50_54, AGE_BINDINGS.AGE_55_59,
    AGE_BINDINGS.AGE_60_64, AGE_BINDINGS.AGE_65_69, AGE_BINDINGS.AGE_70_74, AGE_BINDINGS.AGE_75_79,
    AGE_BINDINGS.AGE_80_84, AGE_BINDINGS.AGE_85_89, AGE_BINDINGS.AGE_GE90], 
    ordered=True
)