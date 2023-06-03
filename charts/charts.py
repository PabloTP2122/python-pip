import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B','C']
    values = [4,5,6]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    #
    #plt.show()
    plt.savefig('pie.png')
    plt.close()
