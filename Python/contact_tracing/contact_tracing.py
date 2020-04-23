#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def plot_contact_matrix(m,title,x_label,y_label,intensity=5,color_map=plt.cm.Greys):
    fig = plt.figure(figsize=(8.0,9.99))
    plt.clf()
    plt.title(title,fontsize = 20)
    ax = fig.add_subplot(111)
    for x in range(len(m)):
        for y in range(len(m[0])):
            text_color = 'black'
            val = m[x][y]
            if val > 0:
                m[x][y] = 1
            if (x + y) == 0:
                val = 'X'
                text_color = 'white'
            ax.annotate(val, xy=(y, x),color=text_color,horizontalalignment='center',verticalalignment='center')
    m = (intensity * 0.1) * m
    m[0][0] = 1
    ax.imshow(m, cmap=color_map) 
    label = range(contact_count)
    plt.xticks(x_label,x_label)
    plt.yticks(y_label,y_label)
    plt.tick_params(axis='both',which='both',bottom=False,top=False,right=False,left=False)
    plt.savefig('img/' + title.replace(' ','_') + '.png',dpi=100)

# Create a contact trace according to each person's encounters
contact_trace = {0:[1,3,4],1:[0,2,7,8,9],2:[1,9,11],3:[0,11,12],4:[0,13,14,15],5:[6,15,16],6:[5,7,18],7:[1,6,20],8:[1],9:[1,2,10],10:[9],11:[2,3,22,23],12:[3],13:[4],14:[4],15:[4,5],16:[5],17:[24],18:[6,19,24,25,26],19:[18,20],20:[7,19,21,27,28],21:[20],22:[11],23:[11],24:[17,18],25:[18],26:[18],27:[20],28:[20]}

# Count all persons in the contact trace
contact_count = len(contact_trace.keys())

# Translate the adjacency list to a matrix
contact_matrix = np.zeros((contact_count,contact_count),dtype=int)
for k in contact_trace:
    for v in contact_trace[k]:
        contact_matrix[k][v] = 1

# Set the contact persons as the labels
label = range(contact_count)

# Plot the contact matrix
plot_contact_matrix(contact_matrix,"Contact Matrix",label,label)

# Plot direct contacts
plot_contact_matrix(contact_matrix[[0]],"Quarantine",label,[0],intensity=6,color_map=plt.cm.Reds)

# Plot contacts of direct contacts
contact_matrix2 = contact_matrix.dot(contact_matrix)
plot_contact_matrix(contact_matrix2[[0]],"Isolation",label,[0],intensity=4,color_map=plt.cm.Reds)

# Plot contacts of contacts of direct contacts
contact_matrix3 = contact_matrix2.dot(contact_matrix)
plot_contact_matrix(contact_matrix3[[0]],"Monitoring",label,[0],intensity=2,color_map=plt.cm.Reds)
