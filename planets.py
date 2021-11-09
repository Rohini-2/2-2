planet_type_values=[] 

for planet_data in planet_data_rows:
  planet_type_values.append(planet_data[6])
  
print(list(set(planet_type_values)))  

planet_masses=[]
planet_radiuses=[]

for planet_data in low_gravity_planets:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])

fig=px.scatter(x=planet_radiuses,y=planet_masses)  
fig.show()

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
X=[]
for index,planet_mass in enumerate(planet_masses):
  temp_list=[
             planet_radiuses[index],
             planet_mass
  ]
  X.append(temp_list)
wcss=[]  
for i in range(1,11):
  kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)
plt.figure(figsize=(10,5))
sns.lineplot(range(1, 11), wcss, marker='o', color='red')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()  

