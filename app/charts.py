import matplotlib.pyplot as plt

def generate_bar_chart(name,labels, values):
  # variables propias de la librería
  # fig - para la figura
  # ax - para los ejes
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  #plt.show()
  plt.savefig(f'./img/{name}.png')
  plt.close()
def generate_pie_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  plt.axis('equal')
  #plt.show()
  plt.savefig(f'./img/{name}.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a','b','c']
  values = [100, 10, 56]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
