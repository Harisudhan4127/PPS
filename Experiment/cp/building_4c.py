material = ['cementbags', 'bricks', 'sand', 'steelbars','paint']
material.append('tiles')
material.insert(3, 'aggregates')
material.remove('sand')
material[5]='electrical'
print(material)

# tuple

material = ('cementbags', 'bricks','Aggregates', 'steelbars','paint','electrical')
print(material)
print('list of elements is =',material)
print('material[0]',material[0])
print('material[1:3]',material[1:3])
