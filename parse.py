#!/usr/bin/env python

from fitparse.base import FitFile


fit_file = FitFile('example.fit')
fit_file.parse()

records = fit_file.get_records_as_dicts()

for record in records:
    print '\nRecord:'

    for key, value in record.iteritems():
        print ' - %s: %s' % (key.replace('_', ' ').capitalize(), value)
