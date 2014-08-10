import csv

def _read_csv(filename):
    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile)

        # Skip header
        next(csvreader, None)

        data = [row for row in csvreader]

    return data


def _avg(rows):
    return round(sum(rows) / float(len(rows)), 2)


def _avg_age(dataset):
    ages = [int(row[2]) for row in dataset]

    return _avg(ages)


def _sum_health_4_and_5(dataset):
    return [int(row[5]) + int(row[8]) for row in dataset]


def _filter_by(label, col_idx, dataset):
    return filter(lambda x: x[col_idx] == label, dataset)


def _average_male_and_female_ages(dataset):

    male_ages = [int(row[2])for row in _filter_by('M', 1, dataset)]
    female_ages = [int(row[2])for row in _filter_by('F', 1, dataset)]

    return _avg(male_ages), _avg(female_ages)


def _write_csv(data):

    with open('abhi_health_data.csv', 'wb') as f:
        w = csv.DictWriter(f, data[0].keys())
        w.writeheader()

        for row in data:
            w.writerow(row)

if __name__ == '__main__':

    dataset = _read_csv('health2.csv')

    print "Avg age is =>", _avg_age(dataset)
    print "Sum of health2 and health5 =>", _sum_health_4_and_5(dataset)

    avg_male_age, avg_female_age = _average_male_and_female_ages(dataset)
    print "Avg male age =>%s and Avg female age =>%s" % (avg_male_age, avg_female_age)

    _write_csv([{'sex': 'M', 'average_age': avg_male_age},
                {'sex': 'F', 'average_age': avg_female_age}])
