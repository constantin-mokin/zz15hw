pupils = [
  {
        'firstname': 'Masha',
        'group': '41',
        'physics': 7,
        'informatics': 6,
        'history': 8,
  },
  {
        'firstname': 'Evgen',
        'group': '42',
        'physics': 1,
        'informatics': 2,
        'history': 1,
  },
  {
        'firstname': 'Olga',
        'group': '43',
        'physics': 9,
        'informatics': 9,
        'history': 9,
  },
  {
        'firstname': 'Serg',
        'group': '44',
        'physics': 8,
        'informatics': 8,
        'history': 3,
  },
  {
        'firstname': 'Artem',
        'group': '45',
        'physics': 8,
        'informatics': 8,
        'history': 3,
  }]

for pupil in pupils:
    average = (pupil['physics'] + pupil['informatics'] + pupil['history']) / 3
    if average > 4:
        for key, value in pupil.items():
            print(f'{key}: {value}')
        print('*-*')


