def read_population_data(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                name, area, population = line.split(',')
                data.append({
                    'country': name.strip(),
                    'area': float(area.strip()),
                    'population': int(population.strip())
                })
    return data

def sort_by_area(data):
    return sorted(data, key=lambda x: x['area'], reverse=True)

def sort_by_population(data):
    return sorted(data, key=lambda x: x['population'], reverse=True)