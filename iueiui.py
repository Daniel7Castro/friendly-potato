class planeta:
    def __init__(self,name,objects,stars,puntos,colorespsicodelicos):
        self.name=name
        self.objects=objects
        self.stars=stars
        self.puntos=puntos
        self.colores=colorespsicodelicos
p1 = planeta ("Saturno psicodelico","cohete","estrellas","puntos","colores psicodelicos")
print(p1.name)
print(p1.objects)
print(p1.stars)
print(p1.puntos)
print(p1.colores)
