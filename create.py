from fit import FitEncoder_Weight
from datetime import datetime


def raw_float(message):
    str = raw_input(message)
    if str:
        try:
            return float(str)
        except ValueError:
            print '- Enter a number only'
            return raw_float(message)
    return None

values = {
    'weight': None,
    'percent_fat': None,
    'muscle_mass': None,
    'bone_mass': None,
    'percent_hydration': None,
    'active_met': None,
    'metabolic_age': None,
    'basal_met': None,
    'visceral_fat_mass': None,
    'visceral_fat_rating': None,
    'physique_rating': None,
}

for key, value in values.iteritems():
    values[key] = raw_float('Enter %s: ' % key.replace('_', ' '))

if (values['weight'] and values['percent_fat'] and values['muscle_mass']
        and not values['bone_mass']):
    calc_bone_mass = raw_input('Approximate bone mass'
                               ' from other settings? (y/N) ')
    if calc_bone_mass == 'y':
        fat_weight = values['weight'] * values['percent_fat'] / 100
        calculated = values['weight'] - values['muscle_mass'] - fat_weight
        values['bone_mass'] = max(0, calculated)

values['timestamp'] = datetime.now()

fit = FitEncoder_Weight()
fit.write_weight_scale(**values)
fit.finish()

a = open('weight-scale_%s.fit' % values['timestamp'].strftime('%y-%m-%d-%H-%I'), 'w')
a.write(fit.get_value())
