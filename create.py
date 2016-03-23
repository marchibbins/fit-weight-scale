#!/usr/bin/env python

from fit import FitEncoder_Weight
from datetime import datetime


measures = [
    ['2016-01-01-06-00', 75.0, 10.0, 60.0, 65.0, 4000]
]

for measure in measures:
    values = {
        'weight': measure[1],
        'percent_fat': measure[2],
        'muscle_mass': measure[4],
        'bone_mass': None,
        'percent_hydration': measure[3],
        'active_met': measure[5],
        'metabolic_age': None,
        'basal_met': None,
        'visceral_fat_mass': None,
        'visceral_fat_rating': None,
        'physique_rating': None,
    }

    fat_weight = values['weight'] * values['percent_fat'] / 100
    calculated = values['weight'] - values['muscle_mass'] - fat_weight
    values['bone_mass'] = max(0, calculated)
    values['timestamp'] = datetime.strptime(measure[0], '%Y-%m-%d-%H-%M')

    fit = FitEncoder_Weight()
    fit.write_weight_scale(**values)
    fit.finish()

    a = open('weight-scale_%s.fit' %
             values['timestamp'].strftime('%Y-%m-%d-%H-%M'), 'w')

    a.write(fit.get_value())
